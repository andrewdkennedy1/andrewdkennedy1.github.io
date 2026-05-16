#!/usr/bin/env python3
"""Static PS4 6.72 host with local Linux payload helper endpoints."""

from __future__ import annotations

import argparse
import os
import socket
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


DEFAULT_DELAYS = (18.0, 28.0, 40.0, 55.0)
BINLOADER_DELAYS = (6.0, 10.0, 15.0, 22.0, 32.0, 45.0, 65.0, 90.0)


def parse_delays(value: str | None) -> tuple[float, ...]:
    if not value:
        return DEFAULT_DELAYS
    delays: list[float] = []
    for part in value.split(","):
        try:
            delay = float(part.strip())
        except ValueError:
            continue
        if 0 <= delay <= 180:
            delays.append(delay)
    return tuple(delays[:120]) or DEFAULT_DELAYS


def parse_retry_delays(params: dict[str, list[str]], default_delays: tuple[float, ...]) -> tuple[float, ...]:
    explicit_delays = params.get("delays", [""])[0]
    if explicit_delays:
        return parse_delays(explicit_delays)
    try:
        timeout = float(params.get("timeout", [""])[0])
    except ValueError:
        timeout = 0.0
    try:
        interval = float(params.get("interval", ["2"])[0])
    except ValueError:
        interval = 2.0
    if timeout <= 0:
        return default_delays
    timeout = min(max(timeout, 1.0), 300.0)
    interval = min(max(interval, 0.5), 15.0)
    delays: list[float] = []
    current = 0.0
    while current <= timeout and len(delays) < 120:
        delays.append(round(current, 3))
        current += interval
    return tuple(delays) or default_delays


def find_payload(root: Path) -> Path | None:
    candidates: list[Path] = []
    env_path = os.environ.get("GOLDHEN_LINUX_PAYLOAD")
    if env_path:
        candidates.append(Path(env_path).expanduser())

    candidates.extend(
        [
            root / "payloads" / "linux-1024mb.elf",
            root.parent / "ps4linux" / "downloads" / "arabpixel-v24b1" / "extracted" / "PS4-Linux-Payloads-24b.1" / "elf" / "linux-1024mb.elf",
            root.parent / "ps4linux" / "downloads" / "arabpixel-v24b1" / "PS4-Linux-Payloads-24b.1" / "elf" / "linux-1024mb.elf",
        ]
    )

    for candidate in candidates:
        try:
            resolved = candidate.resolve()
        except OSError:
            continue
        if resolved.is_file():
            return resolved
    return None


def tcp_probe(target_ip: str, port: int, timeout: float = 1.0) -> tuple[bool, str]:
    try:
        with socket.create_connection((target_ip, port), timeout=timeout):
            return True, "open"
    except OSError as exc:
        return False, str(exc)


def safe_label(value: str | None, fallback: str) -> str:
    if not value:
        return fallback
    cleaned = "".join(ch for ch in value.lower() if ch.isalnum() or ch in "-_")
    return cleaned[:40] or fallback


def send_payload(target_ip: str, port: int, payload_path: Path, delays: tuple[float, ...], label: str) -> None:
    payload = payload_path.read_bytes()
    started = time.monotonic()
    prefix = f"[{label}]"
    print(
        f"{prefix} queued {payload_path} ({len(payload)} bytes) for {target_ip}:{port} "
        f"after delays {', '.join(str(d) for d in delays)}",
        flush=True,
    )

    for delay in delays:
        sleep_for = started + delay - time.monotonic()
        if sleep_for > 0:
            time.sleep(sleep_for)

        try:
            with socket.create_connection((target_ip, port), timeout=5) as sock:
                sock.sendall(payload)
            print(f"{prefix} sent {len(payload)} bytes to {target_ip}:{port}", flush=True)
            return
        except OSError as exc:
            if label.startswith("goldhen") or port == 9090:
                ftp_open, _ = tcp_probe(target_ip, 2121, timeout=0.4)
                if ftp_open:
                    print(
                        f"{prefix} GoldHEN FTP is reachable on {target_ip}:2121, "
                        f"but payload server is not listening on {target_ip}:{port} after {delay:g}s: {exc}",
                        flush=True,
                    )
                    continue
            print(f"{prefix} {target_ip}:{port} not ready after {delay:g}s: {exc}", flush=True)

    print(f"{prefix} failed to send payload to {target_ip}:{port}", flush=True)


class PS4HostHandler(SimpleHTTPRequestHandler):
    server: "PS4HostServer"

    def log_message(self, format: str, *args: object) -> None:
        client_ip = self.client_address[0] if self.client_address else "-"
        print(f"[http] {client_ip} {self.command} {self.path} - {format % args}", flush=True)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in ("/__ps4linux/send-linux-payload", "/__ps4linux/send-goldhen-linux"):
            self.handle_linux_payload(parsed.path, parsed.query)
            return
        if parsed.path.endswith("/cache.manifest") or parsed.path == "/cache.manifest":
            self.handle_cache_manifest(parsed.path)
            return
        super().do_GET()

    def do_HEAD(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in ("/__ps4linux/send-linux-payload", "/__ps4linux/send-goldhen-linux"):
            self.handle_linux_payload(parsed.path, parsed.query, head_only=True)
            return
        if parsed.path.endswith("/cache.manifest") or parsed.path == "/cache.manifest":
            self.handle_cache_manifest(parsed.path, head_only=True)
            return
        super().do_HEAD()

    def handle_cache_manifest(self, request_path: str, head_only: bool = False) -> None:
        relative = request_path.lstrip("/")
        manifest_path = (Path.cwd() / relative).resolve()
        try:
            manifest_path.relative_to(Path.cwd().resolve())
        except ValueError:
            self.send_error(404)
            return
        if not manifest_path.is_file():
            self.send_error(404)
            return

        body = manifest_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/cache-manifest; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        if not head_only:
            self.wfile.write(body)

    def handle_linux_payload(self, request_path: str, query: str, head_only: bool = False) -> None:
        params = parse_qs(query, keep_blank_values=False)
        target_ip = params.get("target", [self.client_address[0]])[0]
        default_port = "9021" if request_path == "/__ps4linux/send-linux-payload" else "9090"
        default_label = "binloader-linux" if default_port == "9021" else "goldhen-linux"
        try:
            port = int(params.get("port", [default_port])[0])
        except ValueError:
            port = int(default_port)
        default_delays = BINLOADER_DELAYS if default_port == "9021" else DEFAULT_DELAYS
        delays = parse_retry_delays(params, default_delays)
        label = safe_label(params.get("label", [default_label])[0], default_label)

        payload_path = self.server.goldhen_linux_payload
        if not payload_path:
            body = (
                "Linux payload was not found. Set GOLDHEN_LINUX_PAYLOAD or place "
                "linux-1024mb.elf at payloads/linux-1024mb.elf.\n"
            ).encode("utf-8")
            self.send_response(500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if not head_only:
                self.wfile.write(body)
            print(f"[{label}] request rejected: payload not found", flush=True)
            return

        worker = threading.Thread(
            target=send_payload,
            args=(target_ip, port, payload_path, delays, label),
            daemon=True,
        )
        worker.start()

        body = (
            f"Queued Linux payload for {target_ip}:{port} with delays "
            f"{', '.join(str(d) for d in delays)}.\n"
        ).encode("utf-8")
        self.send_response(202)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if not head_only:
            self.wfile.write(body)


class PS4HostServer(ThreadingHTTPServer):
    def __init__(self, server_address: tuple[str, int], handler_class: type[PS4HostHandler], payload_path: Path | None):
        super().__init__(server_address, handler_class)
        self.goldhen_linux_payload = payload_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve the PS4 6.72 host with local helper endpoints.")
    parser.add_argument("--bind", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()

    root = Path(args.root).resolve()
    os.chdir(root)
    payload_path = find_payload(root)

    print(f"Serving {root}")
    print(f"Bind address: {args.bind}:{args.port}")
    if payload_path:
        print(f"Linux payload: {payload_path}")
    else:
        print("Linux payload: not found; set GOLDHEN_LINUX_PAYLOAD to enable auto-send")

    server = PS4HostServer((args.bind, args.port), PS4HostHandler, payload_path)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping host.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

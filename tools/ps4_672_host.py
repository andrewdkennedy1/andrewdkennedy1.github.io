#!/usr/bin/env python3
"""Static PS4 6.72 host with a local GoldHEN Linux helper endpoint."""

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
    return tuple(delays[:8]) or DEFAULT_DELAYS


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


def send_payload(target_ip: str, port: int, payload_path: Path, delays: tuple[float, ...]) -> None:
    payload = payload_path.read_bytes()
    started = time.monotonic()
    print(
        f"[goldhen-linux] queued {payload_path} ({len(payload)} bytes) for {target_ip}:{port} "
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
            print(f"[goldhen-linux] sent {len(payload)} bytes to {target_ip}:{port}", flush=True)
            return
        except OSError as exc:
            print(f"[goldhen-linux] {target_ip}:{port} not ready after {delay:g}s: {exc}", flush=True)

    print(f"[goldhen-linux] failed to send payload to {target_ip}:{port}", flush=True)


class PS4HostHandler(SimpleHTTPRequestHandler):
    server: "PS4HostServer"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/__ps4linux/send-goldhen-linux":
            self.handle_goldhen_linux(parsed.query)
            return
        super().do_GET()

    def do_HEAD(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/__ps4linux/send-goldhen-linux":
            self.handle_goldhen_linux(parsed.query, head_only=True)
            return
        super().do_HEAD()

    def handle_goldhen_linux(self, query: str, head_only: bool = False) -> None:
        params = parse_qs(query, keep_blank_values=False)
        target_ip = params.get("target", [self.client_address[0]])[0]
        try:
            port = int(params.get("port", ["9090"])[0])
        except ValueError:
            port = 9090
        delays = parse_delays(params.get("delays", [""])[0])

        payload_path = self.server.goldhen_linux_payload
        if not payload_path:
            body = (
                "GoldHEN Linux payload was not found. Set GOLDHEN_LINUX_PAYLOAD or place "
                "linux-1024mb.elf at payloads/linux-1024mb.elf.\n"
            ).encode("utf-8")
            self.send_response(500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if not head_only:
                self.wfile.write(body)
            print("[goldhen-linux] request rejected: payload not found", flush=True)
            return

        worker = threading.Thread(
            target=send_payload,
            args=(target_ip, port, payload_path, delays),
            daemon=True,
        )
        worker.start()

        body = (
            f"Queued GoldHEN Linux payload for {target_ip}:{port} with delays "
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
        print(f"GoldHEN Linux payload: {payload_path}")
    else:
        print("GoldHEN Linux payload: not found; set GOLDHEN_LINUX_PAYLOAD to enable auto-send")

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

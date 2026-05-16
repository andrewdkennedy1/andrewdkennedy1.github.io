# andrewdkennedy1.github.io

Static GitHub Pages content, including the PS4 6.72 Linux host.

## PS4 6.72 Host

Preferred hosted URL:

- Cached/offline: `https://andrewdkennedy1.github.io/ps4-672-linux/`

The host uses AppCache so the PS4 can keep using it offline after the first
successful load. The visible PS4 page is intentionally one button: `Boot Linux`.

## Self-Host On Your LAN

Use this when you do not want to wait for GitHub Pages to build. The scripts bind
to `0.0.0.0`, so the PS4 can reach the host from another device on the same LAN.

Windows:

```bat
start-ps4-672-host.bat
```

Linux/macOS/Git Bash:

```sh
./start-ps4-672-host.sh
```

Optional custom port:

```sh
./start-ps4-672-host.sh 8080
```

The scripts print URLs like:

```text
http://<your-pc-ip>:8765/ps4-672-linux/
```

On the PS4, open the printed `ps4-672-linux` URL and wait for the cache message
before using payload buttons.

For the current Linux test, use the one-button GoldHEN helper path. It gives
useful PC-side logs instead of leaving the PS4 browser as the only signal and
loads GamerHack's GoldHEN v2.4b18.9 payload instead of the older bundled
GoldHEN script.
Reboot the PS4, keep the Linux USB inserted, then open:

```text
http://<your-pc-ip>:8765/ps4-672-linux/?auto=goldhen-linux
```

That URL auto-presses the page's only visible button. It queues the local helper
to send `linux-1024mb.elf` to the PS4's GoldHEN BinLoader on port `9090`, then
runs the exploit and loads GoldHEN v2.4b18.9. Watch the PC command window for
`[goldhen-linux]` messages. If the PS4 says the page is not responding, do not
press Stop, Back, or another payload button; that can crash the exploit while
the browser thread is owned by the payload.

If the helper logs that GoldHEN FTP is reachable on `2121` but port `9090`
stays closed, open GoldHEN once and enable Payload Server. GoldHEN keeps that
setting, so later one-button attempts can open the payload server automatically
when GoldHEN loads.

The helper auto-finds the ELF from the sibling `ps4linux` checkout. If needed,
set `GOLDHEN_LINUX_PAYLOAD` to the full path of `linux-1024mb.elf` before
starting the server.

The direct PS4Boot payload fallbacks are hidden from the PS4 page so normal
testing stays one button. They remain callable by query string only when
debugging. The direct Pro 1 GB fallback is:

```text
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux-pro
```

Comparison and sanity-check auto URLs are also available:

```text
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux-pro-512
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux-browser
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux-arabpixel
http://<your-pc-ip>:8765/ps4-672-linux/?auto=goldhen
```

`?auto=linux` and `?auto=goldhen-linux` both use the one-button GoldHEN helper
path. `?auto=linux-legacy` remains as an alias for `?auto=linux-browser`.

The page also links comparison 6.72 hosts for stability testing:

- Chronoss Sleirsgoevy 6.72: `https://chronoss09.github.io/sleirsgoevy672/`
- Leeful 6.72 v6: `https://leeful.github.io/672v6/index.html`
- DarkModderVC PS4JB: `https://darkmoddervc.github.io/PS4JB/`
- PS4Boot 6.72 Linux / GoldHEN: `https://ps4boot.github.io/672/index.html`
- PS4Boot 6.72 GoldHEN-only: `https://ps4boot.github.io/672qh/index.html`
- PS4 Playground 6.72: `https://ps4.editzz.com/6.72/index.html`
- Chronoss GoldHEN 6.72: `https://chronoss09.github.io/GoldHen/6.72/index.html`
- Karo 6.72: `https://islataz.github.io/672/index.html`
- GamerHack 6.72: `https://gamerhack.github.io/672/index.html`

Those external hosts are for jailbreak/GoldHEN/Mira comparison and alternate
payload flows. They do not use this page's prepared USB files unless their
selected payload is a Linux loader.

If multiple IP addresses print, use the one on the same LAN as the PS4. Ignore
WSL, VPN, or virtual adapter addresses. On this network the likely LAN address
has been `10.101.69.2`; the exact value can change.

If the PS4 cannot connect but the server is running, allow Python through
Windows Defender Firewall or the host firewall for the current private network.

Keep the terminal or command prompt open. Press `Ctrl+C` to stop the server.

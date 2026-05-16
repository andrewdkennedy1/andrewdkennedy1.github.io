# andrewdkennedy1.github.io

Static GitHub Pages content, including the PS4 6.72 Linux host.

## PS4 6.72 Host

Preferred hosted URL:

- Cached/offline: `https://andrewdkennedy1.github.io/ps4-672-linux/`

The host uses AppCache so the PS4 can keep using it offline after the first
successful load. Use `Force Reload Latest Page` when iterating on local changes.

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

For the current Linux test, use the GoldHEN helper path first. It gives useful
PC-side logs instead of leaving the PS4 browser as the only signal. Reboot the
PS4, keep the Linux USB inserted, then open:

```text
http://<your-pc-ip>:8765/ps4-672-linux/?auto=goldhen-linux
```

This queues the local helper to send `linux-1024mb.elf` to the PS4's GoldHEN
BinLoader on port `9090`, then runs the exploit and loads GoldHEN. Watch the
PC command window for `[goldhen-linux]` messages. If the PS4 says the page is
not responding, do not press Stop, Back, or another payload button; that can
crash the exploit while the browser thread is owned by the payload.

The helper auto-finds the ELF from the sibling `ps4linux` checkout. If needed,
set `GOLDHEN_LINUX_PAYLOAD` to the full path of `linux-1024mb.elf` before
starting the server.

The direct Linux path is still available for comparison. Reboot clears the
jailbreak; the `Boot Linux from USB` / `Exploit + Linux Pro 1GB` button re-runs
the 6.72 exploit and then sends the cached PS4Boot PS4 Pro Linux payload. The
page can auto-start that direct path:

```text
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux
```

Comparison and sanity-check auto URLs are also available:

```text
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux-pro-512
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux-browser
http://<your-pc-ip>:8765/ps4-672-linux/?auto=linux-arabpixel
http://<your-pc-ip>:8765/ps4-672-linux/?auto=goldhen
```

`?auto=linux-legacy` remains as an alias for `?auto=linux-browser`.

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

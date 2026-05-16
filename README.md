# andrewdkennedy1.github.io

Static GitHub Pages content, including the PS4 6.72 Linux host.

## PS4 6.72 Host

Preferred hosted URLs:

- Cached/offline: `https://andrewdkennedy1.github.io/ps4-672-linux/`
- Live/debug: `https://andrewdkennedy1.github.io/ps4-672-linux-live/`

The cached URL uses AppCache so the PS4 can keep using it offline after the
first successful load. The live URL does not use AppCache, which makes it better
for quick testing while scripts are changing.

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
http://<your-pc-ip>:8765/ps4-672-linux-live/
```

On the PS4, open the printed `ps4-672-linux-live` URL while iterating because it
avoids AppCache. Once it works, open `ps4-672-linux` and wait for the cache
message if you want offline use.

For the Linux test, reboot the PS4 first. Reboot clears the jailbreak; the
`Boot Linux from USB` / `Exploit + Linux` button re-runs the 6.72 exploit and
then sends the Linux payload. The live page can auto-start that same path:

```text
http://<your-pc-ip>:8765/ps4-672-linux-live/?auto=linux
```

Fallback and sanity-check auto URLs are also available:

```text
http://<your-pc-ip>:8765/ps4-672-linux-live/?auto=linux-legacy
http://<your-pc-ip>:8765/ps4-672-linux-live/?auto=goldhen
```

The page also links comparison 6.72 hosts for stability testing:

- Chronoss Sleirsgoevy 6.72: `https://chronoss09.github.io/sleirsgoevy672/`
- DarkModderVC PS4JB: `https://darkmoddervc.github.io/PS4JB/`
- Chronoss GoldHEN 6.72: `https://chronoss09.github.io/GoldHen/6.72/index.html`

Those external hosts are for jailbreak/GoldHEN/Mira comparison only; they do not
use this page's ArabPixel Linux USB payload.

If multiple IP addresses print, use the one on the same LAN as the PS4. Ignore
WSL, VPN, or virtual adapter addresses. On this network the likely LAN address
has been `10.101.69.2`; the exact value can change.

If the PS4 cannot connect but the server is running, allow Python through
Windows Defender Firewall or the host firewall for the current private network.

Keep the terminal or command prompt open. Press `Ctrl+C` to stop the server.

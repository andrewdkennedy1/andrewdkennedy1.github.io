#!/usr/bin/env sh
set -eu

PORT="${1:-8765}"
ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "Python 3 was not found on PATH." >&2
  exit 1
fi

list_ips() {
  if [ -n "${HOST_IP:-}" ]; then
    printf '%s\n' "$HOST_IP"
  elif command -v powershell.exe >/dev/null 2>&1; then
    powershell.exe -NoProfile -ExecutionPolicy Bypass -Command 'Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike "127.*" -and $_.IPAddress -notlike "169.254.*" -and $_.AddressState -eq "Preferred" } | Select-Object -ExpandProperty IPAddress' | tr -d '\r'
  elif command -v pwsh >/dev/null 2>&1; then
    pwsh -NoProfile -Command 'Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike "127.*" -and $_.IPAddress -notlike "169.254.*" -and $_.AddressState -eq "Preferred" } | Select-Object -ExpandProperty IPAddress' | tr -d '\r'
  elif command -v hostname >/dev/null 2>&1 && hostname -I >/dev/null 2>&1; then
    hostname -I | tr ' ' '\n'
  elif command -v ip >/dev/null 2>&1; then
    ip route get 1.1.1.1 2>/dev/null | sed -n 's/.* src \([0-9.]*\).*/\1/p'
  else
    printf '%s\n' '<this-pc-ip>'
  fi
}

cd "$ROOT_DIR"

echo "Serving $ROOT_DIR"
echo "Bind address: 0.0.0.0:$PORT"
echo
for ip in $(list_ips); do
  case "$ip" in
    ""|127.*|169.254.*) continue ;;
  esac
  echo "PS4 cached/offline: http://$ip:$PORT/ps4-672-linux/"
  echo
done
echo "Use the IP on the same LAN as the PS4. Ignore WSL, VPN, or virtual adapter IPs."
echo "If the PS4 cannot connect, allow Python through the host firewall."
echo "GoldHEN auto-Linux helper: /__ps4linux/send-goldhen-linux sends linux-1024mb.elf to the PS4 on port 9090."
echo "Set GOLDHEN_LINUX_PAYLOAD to override the ELF path."
echo "Keep this terminal open while the PS4 uses the host."
echo "Press Ctrl+C to stop."
echo

exec "$PYTHON" tools/ps4_672_host.py --port "$PORT" --bind 0.0.0.0

@echo off
setlocal

set "PORT=%~1"
if "%PORT%"=="" set "PORT=8765"

cd /d "%~dp0"

set "PYTHON_CMD="
where python >nul 2>nul && set "PYTHON_CMD=python"
if not defined PYTHON_CMD where py >nul 2>nul && set "PYTHON_CMD=py -3"

if not defined PYTHON_CMD (
  echo Python was not found on PATH.
  echo Install Python 3, then run this file again.
  exit /b 1
)

echo Serving %CD%
echo Bind address: 0.0.0.0:%PORT%
echo.
powershell -NoProfile -ExecutionPolicy Bypass -Command "$port='%PORT%'; $ips=Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike '127.*' -and $_.IPAddress -notlike '169.254.*' -and $_.AddressState -eq 'Preferred' } | Select-Object -ExpandProperty IPAddress; if(-not $ips){$ips=@('<this-pc-ip>')}; foreach($ip in $ips){ 'PS4 cached/offline: http://' + $ip + ':' + $port + '/ps4-672-linux/'; '' }"
echo Use the IP on the same LAN as the PS4. Ignore WSL, VPN, or virtual adapter IPs.
echo If the PS4 cannot connect, allow Python through Windows Defender Firewall.
echo Keep this window open while the PS4 uses the host.
echo Press Ctrl+C to stop.
echo.

%PYTHON_CMD% -m http.server %PORT% --bind 0.0.0.0

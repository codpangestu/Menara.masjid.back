$ErrorActionPreference = 'SilentlyContinue'
# Kill SEMUA python yang menjalankan uvicorn backend (8001-8005)
Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -match 'uvicorn' } | ForEach-Object {
    Write-Host ("Killing PID {0}" -f $_.ProcessId)
    Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
}
Start-Sleep -Seconds 4
Write-Host "=== Verifikasi semua port bebas ==="
foreach ($port in 8001,8002,8003,8004,8005) {
    $c = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
    if ($c) { $c | ForEach-Object { Write-Host ("Port {0} MASIH ADA PID {1}" -f $port, $_.OwningProcess); taskkill /PID $_.OwningProcess /T /F 2>$null | Out-Null } }
    else { Write-Host ("Port {0} bebas" -f $port) }
}
Start-Sleep -Seconds 2
Write-Host "=== Final check ==="
foreach ($port in 8001,8002,8003,8004,8005) {
    $c = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
    if ($c) { Write-Host ("Port {0} MASIH DITEMPATI" -f $port) } else { Write-Host ("Port {0} OK" -f $port) }
}

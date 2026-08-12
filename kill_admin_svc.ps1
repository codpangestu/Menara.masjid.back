$ErrorActionPreference = 'SilentlyContinue'
# Bunuh semua proses python yang menjalankan admin_service
Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -match 'admin_service' } | ForEach-Object {
    Write-Host ("Killing PID {0}" -f $_.ProcessId)
    Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
    taskkill /PID $_.ProcessId /T /F 2>$null | Out-Null
}
Start-Sleep -Seconds 3
Write-Host "=== Sisa listener 8005 ==="
$conns = Get-NetTCPConnection -LocalPort 8005 -State Listen -ErrorAction SilentlyContinue
if ($conns) {
    $conns | ForEach-Object {
        Write-Host ("Listener PID {0}" -f $_.OwningProcess)
        taskkill /PID $_.OwningProcess /T /F 2>$null | Out-Null
    }
} else {
    Write-Host "8005 BERSIH"
}
Start-Sleep -Seconds 2
Write-Host "=== Verifikasi akhir ==="
$conns2 = Get-NetTCPConnection -LocalPort 8005 -State Listen -ErrorAction SilentlyContinue
if ($conns2) { $conns2 | ForEach-Object { Write-Host ("MASIH ADA: PID {0}" -f $_.OwningProcess) } } else { Write-Host "8005 BERSIH TOTAL" }

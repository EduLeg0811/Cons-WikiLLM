# Sobe a API (FastAPI :8000) e a SPA (Vite :5173) juntas para desenvolvimento.
#   pwsh dev.ps1
# Mata qualquer processo já escutando nas portas 8000/5173 antes de subir,
# abre o navegador na SPA quando ela responder, e Ctrl+C encerra tudo.
$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$apiUrl = "http://127.0.0.1:8000"
$spaUrl = "http://localhost:5173"

foreach ($port in 8000, 5173) {
  $conns = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
  foreach ($conn in $conns) {
    Write-Host "-> matando processo PID $($conn.OwningProcess) que ocupava a porta $port" -ForegroundColor Yellow
    Stop-Process -Id $conn.OwningProcess -Force -ErrorAction SilentlyContinue
  }
}

Write-Host "-> API  $apiUrl  (docs em /docs)" -ForegroundColor Green
$api = Start-Process -PassThru -NoNewWindow -WorkingDirectory "$root\tools" `
  -FilePath "python" -ArgumentList @("-m", "uvicorn", "api.main:app", "--port", "8000", "--reload")

Write-Host "-> SPA  $spaUrl" -ForegroundColor Green
try {
  Push-Location "$root\web"
  if (-not (Test-Path "node_modules")) { npm install }

  # Abre o navegador assim que a SPA responder, em background, sem travar o npm run dev.
  Start-Job -ScriptBlock {
    param($url)
    for ($i = 0; $i -lt 30; $i++) {
      try {
        Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 1 | Out-Null
        Start-Process $url
        return
      } catch { Start-Sleep -Seconds 1 }
    }
  } -ArgumentList $spaUrl | Out-Null

  npm run dev
} finally {
  Pop-Location
  if ($api -and -not $api.HasExited) {
    # /T derruba a árvore (uvicorn --reload spawna um processo-filho)
    taskkill /PID $api.Id /T /F 2>$null | Out-Null
  }
}

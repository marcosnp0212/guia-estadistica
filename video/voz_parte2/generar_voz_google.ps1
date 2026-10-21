# Voz en off de los videos con Google Cloud Text-to-Speech (voces Chirp 3 HD en espanol de Espana).
# 1) Pega tu clave de API en el archivo clave.txt (solo la clave, una linea).
# 2) Doble clic en generar_voz.bat (misma voz que la primera vez: Iapetus, velocidad 1)
$ErrorActionPreference = 'Stop'
$aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
$claveFile = Join-Path $aqui 'clave.txt'
if (-not (Test-Path $claveFile)) { Write-Host "Falta el archivo clave.txt con tu clave de API."; Read-Host "Pulsa Intro"; exit 1 }
$clave = (Get-Content $claveFile -Raw).Trim()
$h = @{ 'x-goog-api-key' = $clave }
try { $null = Invoke-RestMethod -Uri 'https://texttospeech.googleapis.com/v1/voices?languageCode=es-ES' -Headers $h }
catch { Write-Host "No se pudo conectar con Google. Revisa la clave, que la API Cloud Text-to-Speech este activada y que el proyecto tenga facturacion."; Write-Host $_.Exception.Message; Read-Host "Pulsa Intro"; exit 1 }
function Hablar($texto, $voz, $vel, $salida) {
  $body = @{ input = @{ text = $texto }; voice = @{ languageCode = 'es-ES'; name = $voz }; audioConfig = @{ audioEncoding = 'LINEAR16'; sampleRateHertz = 24000; speakingRate = $vel } } | ConvertTo-Json -Depth 5
  $bytes = [System.Text.Encoding]::UTF8.GetBytes($body)
  for ($t=1; $t -le 4; $t++) {
    try { $r = Invoke-RestMethod -Method Post -Uri 'https://texttospeech.googleapis.com/v1/text:synthesize' -Headers $h -ContentType 'application/json; charset=utf-8' -Body $bytes
          [IO.File]::WriteAllBytes($salida, [Convert]::FromBase64String($r.audioContent)); return }
    catch { Start-Sleep -Seconds (3*$t) }
  }
  throw "No se pudo generar $salida"
}
$voz = 'es-ES-Chirp3-HD-Iapetus'; $vel = 1.0
Write-Host "Voz: $voz  Velocidad: $vel. Generando..." 
Get-ChildItem -Path $aqui -Filter '*_guion.json' | Sort-Object Name | ForEach-Object {
  $tema = $_.BaseName -replace '_guion',''
  $dir = Join-Path $aqui "audio\$tema"; New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $segs = Get-Content -Raw -Encoding UTF8 $_.FullName | ConvertFrom-Json
  $n = 0
  foreach ($g in $segs) {
    $n++; $out = Join-Path $dir ($g.id + '.wav')
    if (-not (Test-Path $out)) { Hablar $g.texto $voz $vel $out }
    Write-Progress -Activity "Tema $tema" -Status "$n de $($segs.Count)" -PercentComplete (100*$n/$segs.Count)
  }
  Write-Host "Tema $tema : $n fragmentos."
}
Set-Content -Path (Join-Path $aqui 'audio\voz.txt') -Value "$voz $vel"
Write-Host "Listo. Comprime la carpeta 'audio' de esta carpeta en un .zip y subela al chat."
Read-Host "Pulsa Intro para cerrar"

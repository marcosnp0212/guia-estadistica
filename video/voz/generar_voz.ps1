# Genera la voz en off de los vídeos con las voces en español de Windows.
# Uso: clic derecho > Ejecutar con PowerShell (o doble clic en generar_voz.bat).
# Lee los archivos *_guion.json de esta carpeta y crea audio\<tema>\<id>.wav
Add-Type -AssemblyName System.Speech
$aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voces = $s.GetInstalledVoices() | Where-Object { $_.VoiceInfo.Culture.Name -like 'es-*' }
if (-not $voces) { Write-Host "No hay voces en español instaladas. Configuración > Hora e idioma > Voz > Agregar voces > Español (España)."; Read-Host "Pulsa Intro"; exit 1 }
Write-Host "Voces en español disponibles:"; $i=0; $voces | ForEach-Object { Write-Host "  [$i] $($_.VoiceInfo.Name)"; $i++ }
$sel = Read-Host "Número de la voz (Intro = 0)"; if ($sel -eq '') { $sel = 0 }
$s.SelectVoice($voces[[int]$sel].VoiceInfo.Name)
$s.Rate = 0
Get-ChildItem -Path $aqui -Filter '*_guion.json' | ForEach-Object {
  $tema = $_.BaseName -replace '_guion',''
  $dir = Join-Path $aqui "audio\$tema"; New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $segs = Get-Content -Raw -Encoding UTF8 $_.FullName | ConvertFrom-Json
  $n = 0
  foreach ($g in $segs) {
    $s.SetOutputToWaveFile((Join-Path $dir ($g.id + '.wav')))
    $s.Speak($g.texto); $n++
    Write-Progress -Activity "Tema $tema" -Status "$n de $($segs.Count)" -PercentComplete (100*$n/$segs.Count)
  }
  $s.SetOutputToNull()
  Write-Host "Tema $tema : $n fragmentos de audio."
}
Write-Host "Listo. Sube la carpeta 'audio' al chat."; Read-Host "Pulsa Intro para cerrar"

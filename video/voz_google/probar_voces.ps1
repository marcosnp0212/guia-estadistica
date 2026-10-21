# Genera una muestra de cada voz en espanol y abre una pagina para escucharlas y compararlas.
$ErrorActionPreference = 'Stop'
$aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
$clave = (Get-Content (Join-Path $aqui 'clave.txt') -Raw).Trim()
$h = @{ 'x-goog-api-key' = $clave }
try { $v = Invoke-RestMethod -Uri 'https://texttospeech.googleapis.com/v1/voices?languageCode=es-ES' -Headers $h }
catch { Write-Host "No se pudo conectar con Google. Revisa la clave y que la API este activada."; Write-Host $_.Exception.Message; Read-Host "Pulsa Intro"; exit 1 }
$voces = @($v.voices | Where-Object { $_.name -like 'es-ES-Chirp3-HD-*' } | Sort-Object name)
$dir = Join-Path $aqui 'muestras'; New-Item -ItemType Directory -Force -Path $dir | Out-Null
$frase = "Hola. Vamos a ver la varianza. Primero calculamos la media: cuarenta y tres entre cuarenta y cuatro, cero coma nueve siete. Despues, la suma de los cuadrados entre n, menos la media al cuadrado."
$filas = ''
for ($i=0; $i -lt $voces.Count; $i++) {
  $nom = $voces[$i].name; $g = if ($voces[$i].ssmlGender -eq 'FEMALE') {'Mujer'} else {'Hombre'}
  $f = Join-Path $dir ($nom + '.wav')
  if (-not (Test-Path $f)) {
    $body = @{ input = @{ text = $frase }; voice = @{ languageCode = 'es-ES'; name = $nom }; audioConfig = @{ audioEncoding = 'LINEAR16'; sampleRateHertz = 24000 } } | ConvertTo-Json -Depth 5
    $r = Invoke-RestMethod -Method Post -Uri 'https://texttospeech.googleapis.com/v1/text:synthesize' -Headers $h -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($body))
    [IO.File]::WriteAllBytes($f, [Convert]::FromBase64String($r.audioContent))
  }
  Write-Host ("Muestra {0} de {1}" -f ($i+1), $voces.Count)
  $corto = $nom -replace 'es-ES-Chirp3-HD-',''
  $filas += "<tr><td class='n'>$i</td><td><b>$corto</b><br><small>$g</small></td><td><audio controls preload='none' src='muestras/$nom.wav'></audio></td></tr>`n"
}
$html = @"
<!doctype html><html lang='es'><head><meta charset='utf-8'><title>Elige la voz</title>
<style>body{font-family:Segoe UI,sans-serif;max-width:760px;margin:30px auto;padding:0 16px;background:#f6f8f7;color:#1f2a30}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden}td{padding:10px 14px;border-bottom:1px solid #dde3e6;vertical-align:middle}
td.n{font-size:28px;font-weight:800;color:#2f5fd0;width:50px;text-align:center}audio{width:100%}p{line-height:1.5}</style></head><body>
<h1>Elige la voz</h1><p>Escucha las muestras. Apunta el <b>numero</b> de la que mas te guste y luego ejecuta <b>generar_voz_google.bat</b>: te pedira ese numero.</p>
<table>$filas</table></body></html>
"@
$pag = Join-Path $aqui 'elige_voz.html'
[IO.File]::WriteAllText($pag, $html, [System.Text.Encoding]::UTF8)
Start-Process $pag
Write-Host "Se ha abierto la pagina para escuchar las voces."; Read-Host "Pulsa Intro para cerrar"

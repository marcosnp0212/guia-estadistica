#!/bin/bash
# Los scripts usan rutas absolutas /home/claude/<carpeta>. Este script las enlaza con el repositorio.
set -e
R="$(cd "$(dirname "$0")" && pwd)"
mkdir -p /home/claude
for d in build web video xl2 xl3 entrega; do
  if [ "$R/$d" != "/home/claude/$d" ]; then rm -rf "/home/claude/$d"; ln -s "$R/$d" "/home/claude/$d"; fi
done
# audios: opus (en el repo) -> wav (lo que usa el motor de vídeo)
for f in $(cd "$R/video/audio_opus" && ls */*.opus 2>/dev/null); do
  o="$R/video/audio/${f%.opus}.wav"; [ -f "$o" ] && continue
  mkdir -p "$(dirname "$o")"; ffmpeg -loglevel error -y -i "$R/video/audio_opus/$f" -ar 24000 -ac 1 "$o"
done
pip install --break-system-packages -q openpyxl playwright 2>/dev/null || true
which pandoc >/dev/null || echo "Falta pandoc: apt-get install -y pandoc"
echo "Listo."

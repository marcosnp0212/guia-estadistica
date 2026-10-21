#!/bin/bash
# Voz en off con las voces de macOS (Mónica o Jorge). Uso: bash generar_voz_mac.sh
cd "$(dirname "$0")"; VOZ="${1:-Mónica}"
for g in *_guion.json; do t="${g%_guion.json}"; mkdir -p "audio/$t"
  python3 -c "import json,sys;[print(s['id']+'\t'+s['texto']) for s in json.load(open(sys.argv[1]))]" "$g" | while IFS=$'\t' read -r id txt; do
    say -v "$VOZ" --file-format=WAVE --data-format=LEI16@22050 -o "audio/$t/$id.wav" "$txt"; done
  echo "Tema $t listo"; done

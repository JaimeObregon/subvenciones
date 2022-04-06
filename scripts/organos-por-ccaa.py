#!/usr/bin/env python3

import requests
import warnings
from pathlib import Path
import json

url_base = "https://www.infosubvenciones.es/bdnstrans/organos?code=A&value={:02d}"
n_ccaa = 19

def main():
    organos_por_ccaa = {}
    for i in range(1, n_ccaa+1):
        print(f"\r[{i:2d}/{n_ccaa:2d}]")
        request_listado = requests.get(url_base.format(i), verify=False)
        assert request_listado.status_code == 200
        listado_organos = request_listado.json()
        ccaa = { item['nivel1'] for item in listado_organos }
        organos = [ item["strdescripcion"] for item in listado_organos ]
        organos_por_ccaa[ccaa.pop()] = organos
    exportar_json(organos_por_ccaa, json_indent = 2)

def exportar_json(organos_por_ccaa, json_indent):
    out_path = Path(__file__).parents[1] / "files" / "organos_por_ccaa.json"
    organos_jsonified = json.dumps(
        organos_por_ccaa, 
        indent = json_indent,
        ensure_ascii = False
    )
    out_path.write_text(organos_jsonified)

if __name__ == "__main__":
    main()

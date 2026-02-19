"""Busca dados do seu sistema por API e gera QR Codes automaticamente.

Uso:
    export API_URL="https://seu-sistema.com/api/pagamentos/123"
    export API_TOKEN="seu-token"
    export QR_OUTPUT_DIR="/caminho/de-saida"  # opcional
    python gerador_qrcode_api.py

Configuração opcional:
    export QR_FIELD="payload_pix"  # campo no JSON que contém o texto do QRCode
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import requests

from gerador_qrcode import gerar_qrcode

API_URL = os.getenv("API_URL", "")
API_TOKEN = os.getenv("API_TOKEN", "")
QR_FIELD = os.getenv("QR_FIELD", "qrcode")
QR_OUTPUT_DIR = os.getenv("QR_OUTPUT_DIR", "")
TIMEOUT = int(os.getenv("API_TIMEOUT", "15"))


def buscar_dados_api(url: str, token: str | None = None) -> dict[str, Any]:
    headers: dict[str, str] = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def main() -> None:
    if not API_URL:
        raise RuntimeError(
            "Defina a variável de ambiente API_URL com o endpoint do seu sistema."
        )

    dados = buscar_dados_api(API_URL, API_TOKEN or None)
    texto_qrcode = dados.get(QR_FIELD)

    if not texto_qrcode:
        raise KeyError(
            f"Campo '{QR_FIELD}' não encontrado na resposta da API. "
            "Use QR_FIELD para definir o nome correto."
        )

    destino = Path(QR_OUTPUT_DIR).expanduser() if QR_OUTPUT_DIR else None
    caminho_arquivo = gerar_qrcode(str(texto_qrcode), destino=destino) if destino else gerar_qrcode(str(texto_qrcode))
    print(f"QR Code gerado com sucesso: {caminho_arquivo}")


if __name__ == "__main__":
    main()

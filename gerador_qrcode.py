from pathlib import Path

import pyqrcode

DESTINO_PADRAO = Path(__file__).resolve().parent / "qr_imagem"
BASE_FILENAME = "QRCode"


def gerar_qrcode(texto_qrcode: str, destino: Path = DESTINO_PADRAO) -> Path:
    """Gera um QR Code PNG e devolve o caminho completo da imagem."""
    if not texto_qrcode:
        raise ValueError("O texto para gerar o QR Code não pode ser vazio.")

    destino.mkdir(parents=True, exist_ok=True)

    contador = 0
    while True:
        sufixo = "" if contador == 0 else str(contador)
        filename = f"{BASE_FILENAME}{sufixo}.png"
        caminho_arquivo = destino / filename
        if not caminho_arquivo.exists():
            break
        contador += 1

    qr_code = pyqrcode.create(texto_qrcode)
    qr_code.png(str(caminho_arquivo), scale=8)

    return caminho_arquivo


def escolher_destino() -> Path:
    destino_digitado = input(
        "Pasta para salvar o QR Code (ENTER para usar ./qr_imagem): "
    ).strip()
    return Path(destino_digitado).expanduser() if destino_digitado else DESTINO_PADRAO


def main() -> None:
    link = input("Entre com o link/chave para criar o qrcode: ").strip()
    destino = escolher_destino()
    caminho = gerar_qrcode(link, destino=destino)
    print(f"QR Code salvo em: {caminho}")


if __name__ == "__main__":
    main()

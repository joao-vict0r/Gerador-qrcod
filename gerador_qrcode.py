import pyqrcode
from PIL import Image
import shutil
import os

# destino para guardar imagem
destino_imagem_qr = r"C:\Users\Joaov\Ambiente de Trabalho\Python projets\auto_boots\gerador qrcode\qr_imagem"

# Verifica se o diretório de destino existe caso contrário, cria o diretório
os.makedirs(destino_imagem_qr, exist_ok=True)

# Solicita o link de acesso ou chave pix para gerar o QR Code
link = input("Entre com o link para criar o qrcode: ")
qr_code = pyqrcode.create(link)

# Gera um nome de arquivo único para o QR Code
base_filename = "QRCode"
counter = 1
filename = f"{base_filename}.png"
while os.path.exists(os.path.join(destino_imagem_qr, filename)):
    filename = f"{base_filename}{counter}.png"
    counter += 1

# Salva o QR Code com o nome de arquivo único
qr_code.png(filename, scale=8)

# Move o arquivo para o diretório de destino
shutil.move(filename, os.path.join(destino_imagem_qr, filename))

# Exibe o QR Code gerado
Image.open(os.path.join(destino_imagem_qr, filename)).show()

print(f"QR Code salvo como {filename}")


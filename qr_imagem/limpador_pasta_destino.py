import os

# Define o caminho da pasta onde os arquivos serão deletados
caminho_pasta = r"C:\Users\Joao\Ambiente de Trabalho\Python projets\boots\qr_imagem"

# Define o tamanho limite em bytes: 300 MB
tamanho_limite = 300 * 1024 * 1024 

# Itera sobre os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    
    # Verifica se é um arquivo (não um diretório) e se o tamanho é maior que o limite
    if os.path.isfile(caminho_arquivo):
        tamanho_arquivo = os.path.getsize(caminho_arquivo)
        if tamanho_arquivo > tamanho_limite:
            os.remove(caminho_arquivo)
            print(f"Arquivo removido: {caminho_arquivo} ({tamanho_arquivo / (1024 * 1024):.2f} MB)")

print("Limpeza concluída.")

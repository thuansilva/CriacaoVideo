import requests

def download_file(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Verifica se houve erros na requisição

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):  # Faz o download em partes
                file.write(chunk)
        print(f"Arquivo salvo como {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")

# Exemplo de uso
url = "https://exemplo.com/arquivo.pdf"  # Substitua pela URL desejada
filename = "arquivo_baixado.pdf"         # Nome do arquivo a ser salvo
download_file(url, filename)

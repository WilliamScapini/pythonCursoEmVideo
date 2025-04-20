import requests

url = "https://www.pudim.com.br"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    conteudoHTML = resposta.text
    print(conteudoHTML)# retorna o html do site que doi requisitado
    print("Conexão bem-sucedida!")
except requests.exceptions.RequestException as erro:
    # A linha abaixo será impressa se houver algum problema ao tentar acessar o site.
    # Isso pode acontecer se a internet estiver desconectada, se o site não existir,
    # ou se houver algum outro erro na comunicação.
    print(f"Ocorreu um erro ao conectar: {erro}")
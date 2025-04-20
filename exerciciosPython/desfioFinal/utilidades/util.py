import json
import os

# Códigos ANSI para colorir o texto no terminal
letraPadrao = '\033[0m'
letraVerde = '\033[1;32m'
letraAzul = '\033[34m'
letraVermelho = "\033[31m"
letraAmarela = "\033[33m"

def escreva(msg: str, carac: str = "-", cor: str = letraPadrao) -> None:
    """
    Exibe uma mensagem centralizada com uma borda de caracteres no terminal, podendo aplicar cor.

    Args:
        msg (str): A mensagem a ser exibida.
        carac (str, opcional): Caractere usado para as bordas superior e inferior. Padrão "-".
        cor (str, opcional): Código ANSI para aplicar cor à mensagem. Padrão: sem cor.
    """
    print(carac * 40)
    print(f"{cor}{msg.center(40)}{letraPadrao}")
    print(carac * 40)

def leiaInteiro(msg: str, *tupla: int) -> int:
    """
    Solicita ao usuário que digite um número inteiro, com validação opcional contra valores permitidos.

    Args:
        msg (str): Mensagem exibida ao solicitar a entrada.
        *tupla (int): Lista opcional de inteiros válidos. Se fornecida, valida a entrada com esses valores.

    Returns:
        int: O número inteiro digitado pelo usuário.
    """
    while True:
        try:
            entrada = input(f"{letraAmarela}{msg}{letraPadrao}")
            numero = int(entrada)
            if not tupla or numero in tupla:
                return numero
            else:
                print(f"{letraVermelho}ERRO! Digite uma opção válida entre {tupla}!{letraPadrao}")
        except ValueError:
            print(f"{letraVermelho}ERRO! Digite um número inteiro válido!{letraPadrao}")

def opcoes(carac: str = "-") -> None:
    """
    Exibe no terminal o menu principal de opções do sistema.

    Args:
        carac (str, opcional): Caractere usado para a linha inferior do menu. Padrão "-".
    """
    print(f"{letraVerde}1 -{letraAzul} Ver pessoas cadastradas.{letraPadrao}")
    print(f"{letraVerde}2 -{letraAzul} Cadastrar nova pessoa.{letraPadrao}")
    print(f"{letraVerde}3 -{letraAzul} Sair do sistema.{letraPadrao}")
    print(carac * 40)

def leiaNomeEidade() -> dict:
    """
    Solicita ao usuário que informe seu nome e idade.

    Returns:
        dict: Dicionário contendo 'nome' (str) e 'idade' (int).
    """
    valor = input("Digite o nome: ")
    idade = leiaInteiro("Digite a idade: ")
    return {"nome": valor, "idade": idade}

def cadastrarPessoa(nome_arquivo: str) -> None:
    """
    Cadastra uma nova pessoa, salvando seus dados em um arquivo JSON.
    Caso o arquivo ou a pasta 'json' não existam, serão criados automaticamente.

    Args:
        nome_arquivo (str): Nome do arquivo JSON onde os dados serão armazenados.
    """
    pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_json = os.path.join(pasta_principal, "json")
    os.makedirs(pasta_json, exist_ok=True)

    caminho_arquivo = os.path.join(pasta_json, nome_arquivo)

    # Lê os dados existentes, se o arquivo existir
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            cadastros = json.load(arquivo)
    except FileNotFoundError:
        cadastros = []

    novo_cadastro = leiaNomeEidade()
    cadastros.append(novo_cadastro)

    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(cadastros, arquivo, indent=4)

    escreva("CADASTRO REALIZADO COM SUCESSO!", carac="=", cor=letraVerde)

def mostraCadastros(nome_arquivo: str) -> None:
    """
    Lê e exibe os cadastros de pessoas armazenados em um arquivo JSON.

    Args:
        nome_arquivo (str): Nome do arquivo JSON com os dados das pessoas cadastradas.
    """
    pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_json = os.path.join(pasta_principal, "json")
    caminho_arquivo = os.path.join(pasta_json, nome_arquivo)

    try:
        with open(caminho_arquivo, 'r') as arquivo:
            cadastros = json.load(arquivo)

        if cadastros:
            escreva("PESSOAS CADASTRADAS", carac="=", cor=letraAzul)
            for pessoa in cadastros:
                print(f"Nome: {pessoa['nome']}")
                print(f"Idade: {pessoa['idade']}")
                print("-" * 20)
        else:
            escreva("NENHUM CADASTRO ENCONTRADO!", carac="=", cor=letraVermelho)

    except FileNotFoundError:
        escreva("NENHUM CADASTRO ENCONTRADO!", carac="=", cor=letraVermelho)

# Mostra o caminho da pasta principal (útil para debug)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

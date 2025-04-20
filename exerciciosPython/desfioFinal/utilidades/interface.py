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

def leiaInteiro(msg: str, *valores_validos: int) -> int:
    """
    Solicita ao usuário que digite um número inteiro, com validação opcional contra valores permitidos.

    Args:
        msg (str): Mensagem exibida ao solicitar a entrada.
        *valores_validos (int): Lista opcional de inteiros válidos. Se fornecida, valida a entrada com esses valores.

    Returns:
        int: O número inteiro digitado pelo usuário.
    """
    while True:
        try:
            entrada = input(f"{letraAmarela}{msg}{letraPadrao}")
            numero = int(entrada)
            if not valores_validos or numero in valores_validos:
                return numero
            else:
                print(f"{letraVermelho}ERRO! Digite uma opção válida entre {valores_validos}!{letraPadrao}")
        except ValueError:
            print(f"{letraVermelho}ERRO! Digite um número inteiro válido!{letraPadrao}")

def opcoes() -> None:
    """
    Exibe no terminal o menu principal de opções do sistema.

    Exibe as opções para visualizar as pessoas cadastradas, cadastrar uma nova pessoa ou sair do sistema.
    """
    print(f"{letraVerde}1 -{letraAzul} Ver pessoas cadastradas.{letraPadrao}")
    print(f"{letraVerde}2 -{letraAzul} Cadastrar nova pessoa.{letraPadrao}")
    print(f"{letraVerde}3 -{letraAzul} Sair do sistema.{letraPadrao}")
    print("-" * 40)

def leiaNomeEidade() -> dict:
    """
    Solicita ao usuário que informe seu nome e idade.

    Retorna um dicionário com as chaves 'nome' e 'idade'.

    Returns:
        dict: Dicionário contendo o nome e a idade fornecidos pelo usuário.
    """
    nome = input("Digite o nome: ")
    idade = leiaInteiro("Digite a idade: ")
    return {"nome": nome, "idade": idade}

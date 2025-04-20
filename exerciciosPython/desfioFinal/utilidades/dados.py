import json
import os
from .interface import escreva, letraVerde, letraAzul, letraVermelho, leiaNomeEidade

def caminhoBase() -> str:
    """
    Retorna o caminho base do projeto, que é o diretório acima do diretório atual (onde está o arquivo 'dados.py').

    Retorna:
        str: Caminho absoluto do diretório principal do projeto.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Volta duas pastas acima


def caminhoArquivo(nome_arquivo: str) -> str:
    """
    Retorna o caminho completo do arquivo onde os dados JSON serão armazenados.

    Se a pasta 'json' não existir, ela será criada automaticamente.

    Args:
        nome_arquivo (str): O nome do arquivo JSON a ser utilizado.

    Retorna:
        str: Caminho completo para o arquivo JSON.
    """
    pasta_json = os.path.join(caminhoBase(), "json")
    os.makedirs(pasta_json, exist_ok=True)  # Cria a pasta 'json' se não existir
    return os.path.join(pasta_json, nome_arquivo)  # Retorna o caminho completo para o arquivo JSON


def arquivoExiste(caminho: str) -> bool:
    """
    Verifica se um arquivo existe no caminho especificado.

    Args:
        caminho (str): O caminho do arquivo a ser verificado.

    Retorna:
        bool: True se o arquivo existir, False caso contrário.
    """
    return os.path.isfile(caminho)


def criarArquivo(caminho: str) -> None:
    """
    Cria um arquivo JSON vazio no caminho especificado, com uma lista vazia como conteúdo.

    Args:
        caminho (str): O caminho do arquivo a ser criado.
    """
    with open(caminho, 'w') as f:
        json.dump([], f)  # Cria um arquivo JSON com uma lista vazia


def lerArquivo(caminho: str) -> list:
    """
    Lê o conteúdo de um arquivo JSON e retorna os dados nele armazenados.

    Args:
        caminho (str): O caminho do arquivo JSON a ser lido.

    Retorna:
        list: Lista de dados lidos do arquivo JSON.
    """
    with open(caminho, 'r') as f:
        return json.load(f)  # Retorna os dados no formato de lista


def escreverArquivo(caminho: str, dados: list) -> None:
    """
    Sobrescreve o conteúdo de um arquivo JSON com os dados fornecidos.

    Args:
        caminho (str): O caminho do arquivo JSON a ser sobrescrito.
        dados (list): A lista de dados a ser escrita no arquivo JSON.
    """
    with open(caminho, 'w') as f:
        json.dump(dados, f, indent=4)  # Escreve a lista de dados com indentação


def cadastrarPessoa(nome_arquivo: str) -> None:
    """
    Cadastra uma nova pessoa. O novo cadastro é adicionado ao arquivo JSON correspondente.

    Se o arquivo JSON não existir, ele será criado automaticamente.

    Args:
        nome_arquivo (str): O nome do arquivo JSON onde os cadastros serão armazenados.
    """
    caminho = caminhoArquivo(nome_arquivo)
    
    # Se o arquivo não existir, cria um arquivo vazio
    if not arquivoExiste(caminho):
        criarArquivo(caminho)

    # Lê os cadastros existentes no arquivo
    cadastros = lerArquivo(caminho)

    # Adiciona o novo cadastro à lista
    cadastros.append(leiaNomeEidade())

    # Sobrescreve o arquivo com os dados atualizados
    escreverArquivo(caminho, cadastros)

    # Exibe uma mensagem de sucesso
    escreva("CADASTRO REALIZADO COM SUCESSO!", "=", letraVerde)


def mostraCadastros(nome_arquivo: str) -> None:
    """
    Exibe os cadastros de pessoas armazenados em um arquivo JSON.

    Caso o arquivo não exista ou não haja cadastros, exibe uma mensagem de erro.

    Args:
        nome_arquivo (str): O nome do arquivo JSON contendo os cadastros.
    """
    caminho = caminhoArquivo(nome_arquivo)

    # Se o arquivo não existir, exibe uma mensagem de erro
    if not arquivoExiste(caminho):
        escreva("NENHUM CADASTRO ENCONTRADO!", "=", letraVermelho)
        return  # Sai da função

    # Lê os cadastros armazenados no arquivo
    cadastros = lerArquivo(caminho)

    # Se houver cadastros, exibe-os
    if cadastros:
        escreva("PESSOAS CADASTRADAS", "=", letraAzul)
        for pessoa in cadastros:
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print("-" * 20)
    else:
        # Se não houver cadastros, exibe uma mensagem de erro
        escreva("NENHUM CADASTRO ENCONTRADO!", "=", letraVermelho)

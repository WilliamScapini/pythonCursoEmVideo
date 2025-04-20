from utilidades.interface import escreva, opcoes, leiaInteiro
from utilidades.dados import cadastrarPessoa, mostraCadastros

while True:
    # Exibe o título do menu utilizando a função 'escreva' para centralizar e colorir a mensagem
    escreva("MENU PRINCIPAL", carac="=", cor='\033[1;32m')
    opcoes()   
    opcao = leiaInteiro("Sua opção: ", 1, 2, 3)# Solicita ao usuário que escolha uma opção válida (1, 2 ou 3)   
    if opcao == 1:
        mostraCadastros("cadastro.json")
    elif opcao == 2:
        cadastrarPessoa("cadastro.json")
    elif opcao == 3:
        escreva("Saindo do sistema...", carac="=", cor='\033[31m')
        break  

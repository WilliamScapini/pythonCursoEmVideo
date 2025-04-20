from utilidades import util
from time import sleep

while True:
    util.escreva("Menu Principal")
    util.opcoes()
    nu = util.leiaInteiro("Sua opção: ",1,2,3)
    if nu == 3:
        sleep(0.5)
        break
    elif nu == 2:
        sleep(0.5)
        util.cadastrarPessoa("cadastro.json")
        input()
    elif nu == 1:
        sleep(0.5)
        util.mostraCadastros("cadastro.json")
        input()

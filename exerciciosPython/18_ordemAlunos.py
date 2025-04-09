import random
import os

condicional = True
def sorteioOrdenado(l):
    ar = []
    if l <= 0:
        return []
    
    while len(ar) < l:
        valorR = random.randint(1,l)
        if valorR not in ar:
            ar.append(valorR)
    return ar         

arr = []
while condicional:
    valor = input("quantos alunos são?:\n")
    if valor.isnumeric():
        numAlunos = int(valor)
        condicional = False
        i = 1
        while i < numAlunos + 1:
            valor1 = input("Qual o nome do {}° aluno\n".format(i))
            if valor1.isalpha():
                i= i + 1
                arr.append(valor1)
            else:
                os.system("clear")
                print('Você digitou um valor inválido,\npor favor')
        os.system("clear")
        ordem = sorteioOrdenado(len(arr))
        print("Ordem dos alunos sorteados:\n")
        for n in range(len(ordem)):
            print("{}° Aluno {:_>25}".format(n+1,arr[ordem[n]-1]))
    else:
        os.system("clear")
        print('Você digitou um valor inválido,\npor favor')

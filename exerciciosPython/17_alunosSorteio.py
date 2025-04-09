import random 
import os

condicional = True

arr = []

while condicional:
    valor1 = input("Digite o nome do seu aluno\n")
    if valor1.isalpha():
        arr.append(valor1)
        valor2 = input("Tem mais alunos? responda com S ou N\n")
        if valor2 == 'S' or valor2 == "s":
            condicional = True
        elif valor2 == "N" or valor2 == 'n':
            indice = random.randint(1,len(arr))
            print("O aluno sorteado foi o \n{:-^30}".format(arr[indice]))
            condicional = False
        else:
                print("Caractere inválido tente novamente")   
                condicional = False
    else:
        os.system("clear")
        print("Vocẽ digitou um valor invalido,\npor favor")


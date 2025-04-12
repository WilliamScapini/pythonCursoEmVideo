import math as mat
import os

condicional = True 

def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False
 
while condicional:
    valor = input("Escreva um número real qualquer usando (.) \n")
    if isFloat(valor):
        num = float(valor)
        print("Você digitou {}\nSem suas casas decimais ficaria {}".format(num,mat.trunc(num)))
        condicional = False
    else:
        os.system("clear")
        print("Vocẽ digitou um valor invalido,\npor favor")
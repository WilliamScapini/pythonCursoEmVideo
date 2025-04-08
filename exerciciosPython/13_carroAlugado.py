import os

condicional = True
condicional1 = True
def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False

while condicional:
    valor1 = input("Quantos dias o carro foi alugado?\n")
    if isFloat(valor1):
        num = float(valor1)
        while condicional1:
            valor2 = input("Quantos km foram rodados?\n")
            if isFloat(valor2):
                num1 = float(valor2)
                val = num*60 + 0.15*num1
                valorFinal = "R$ {:.2f}".format(val)
                print("O valor a ser pago para {} dias e {}Km rodados é\n{:=^30}\n".format(num,num1,valorFinal))
                condicional = False
                condicional1 = False
            else: 
                os.system("clear")
                print('Você digitou um valor inválido para km rodados\nPor favor')
    else:
        os.system("clear")
        print('Você digitou um valor inválido\nPor favor')
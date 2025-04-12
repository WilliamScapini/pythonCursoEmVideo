condicional = True
condicional1 = True
def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False

while condicional:
    valor1 = input("Qual o valor do salário?\n")
    if isFloat(valor1):
        num = float(valor1)
        while condicional1:
            valor2 = input("Qual a % de de aumento que você quer aplicar?\n")
            if valor2.isnumeric():
                num1 = int(valor2)
                numAcrescimo = 1+(num1/100)
                val = num * numAcrescimo
                valorFinal = "R$ {:.2f}".format(val)
                print("Ao aplicar {}% de aumento em {} o valor final do salário do funcionario será\n{:=^25}".format(num1,num,valorFinal))
                condicional = False
                condicional1 = False
            else: 
                print('Você digitou um valor inválido\nPor favor')
    else:
        print('Você digitou um valor inválido\nPor favor')
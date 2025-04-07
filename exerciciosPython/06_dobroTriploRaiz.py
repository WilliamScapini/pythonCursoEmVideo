condicional = True
while condicional:
    valor1 = input("Digite um número:\n")
    if valor1.isnumeric() :
        numero1 = int(valor1)
        print("\n você digitou {} seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f1500}".format(numero1,numero1*2,numero1*3,numero1**(1/2)))
        condicional = False   
    else:
        print("Você digitou um número inválido\nPor favor ")
        condicional = True
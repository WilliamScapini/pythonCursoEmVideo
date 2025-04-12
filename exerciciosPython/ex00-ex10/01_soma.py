condicional = True
condicional1 = True
while condicional:
    valor1 = input("Digite um número:\n")
    if valor1.isnumeric() :
        numero1 = int(valor1)
        condicional = False
        while condicional1:  
            valor2 = input('Digite outro número\n')  
            if valor2.isnumeric():
                numero2 = int(valor2)
                condicional1 = False
                print("A soma de {} + {} = {}".format(numero1,numero2,numero2 + numero1))
            else:
                print("Você digitou um número inválido\nPor favor ")
                condicional1 = True    
    else:
        print("Você digitou um número inválido\nPor favor ")
        condicional = True
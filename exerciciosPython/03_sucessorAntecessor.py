condicional = True
while condicional:
    valor1 = input("Digite um número:\n")
    if valor1.isnumeric() :
        numero1 = int(valor1)
        print("\n você digitou {} seu succesor é {} e seu antecessor é {}".format(numero1,numero1+1,numero1-1))
        condicional = False   
    else:
        print("Você digitou um número inválido\nPor favor ")
        condicional = True
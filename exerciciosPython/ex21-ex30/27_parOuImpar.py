while True:
    valor = input("Digite um número inteiro para verificar se é impar ou par\n")
    if valor.isnumeric():
        num = int(valor)
        resto = num % 2
        if resto == 0:
            print(f"O número {num} é PAR!")
            break
        else:
            print(f"O número {num} é ÌMPAR!")
            break
    else:
        print("valor inválido, por favor")

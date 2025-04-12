while True:
    valor = input("Digite qualquer ano pra verificar se é bissexto:\n")
    if valor.isnumeric():
        num = int(valor)
        condicional = (num % 400 == 0 & num % 100 == 0) or (num % 4 == 0 & num % 100 != 0)
        if condicional:
            print(f"O ano de {num} é um ano bissexto!")
            break
        else:
            print(f"Não é um ano bissexto")
            break
    else:
        print("Valor inválido, por favor")
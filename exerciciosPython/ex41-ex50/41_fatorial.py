while True:
    valor = input("Digite o valor no qual quer obter o fatorial!:\n")
    if valor.isnumeric():
        num = int(valor)
        fatorial = 1
        for i in range(num,1,-1):
            fatorial = fatorial*i
        print(f"{num}! = {fatorial}")
        break
    else:
        print("Valor inválido por favor:")
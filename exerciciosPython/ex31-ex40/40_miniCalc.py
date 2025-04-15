arr = []
a= "=-"
while True:
    if len(arr) == 0:
        valor0 = int(input("Digite um valor:\n"))
        valor1 = int(input("Digite outro valor:\n"))
        arr.append(valor0)
        arr.append(valor1)
    else:
        valor = int(input("Digite o valor:\n"))
        arr.append(valor)
    operacao = int(input(f"{a*20}\nquais das opções você quer:\n1 - Somar\n2 - Multiplicar\n3 - Adicionar mais um número\n4 - Fechar o prograna\n{a*20}\n"))
    if operacao == 1:
        print(f"A soma dos números é {sum(arr)}")
        break
    elif operacao == 2:
        m = 1
        for num in arr:
            m = m*num
        print(f"A multiplicação desses número é {m}")
        break
    elif operacao == 4:
        print("fim")
        break
    elif operacao != 3:
        "Valor inválido por favor:\n"

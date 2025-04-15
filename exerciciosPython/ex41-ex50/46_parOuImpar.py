from random import randint
print("=-"*30)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*30)
while True:
    n = input("Digite um valor entre 0 e 10:\n")
    if not n.isnumeric():
        print("valor inválido, por favor\n")
    num = int(n)
    parOuImpar = input("Você quer par ou ímpar?[P/I]")
    aleatorio = randint(0,10)
    soma = num + aleatorio
    if parOuImpar.upper() == "P":
        if soma%2 == 0:
            print(f"Venceu!, pensei em {aleatorio} e a soma seria {soma} que é par")
            input("Pressione enter para continuar")
        else:
            print(f"Perdeu!, pensei em {aleatorio} e a soma seria {soma} que é ímpar")
            input("acabou")
            break
    else:
        if soma%2 == 0:
            print(f"Venceu!, pensei em {aleatorio} e a soma seria {soma} que é ímpar")
            input("Pressione enter para continuar")
        else:
            print(f"Perdeu!, pensei em {aleatorio} e a soma seria {soma} que é par")
            input("acabou")
            break

from os import system
while True:
    system("clear")
    n = int(input("Digite um valor pra ver sua tábuada:\n[digite um numero negativo para parar]\n"))
    print("="*25)
    if n < 0:
        break
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    input("")
print("Acabou")
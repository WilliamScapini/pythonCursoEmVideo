from random import randint
from time import sleep

print("=" * 30)
n = int(input("Quantos sorteios você quer gerar?\n"))
print("=" * 30)

numeros = []

for i in range(1, n + 1):
    sorteio = []
    while len(sorteio) < 6:
        numero = randint(1, 60)
        if numero not in sorteio:
            sorteio.append(numero)
    sorteio.sort()
    numeros.append(sorteio)
    print(f"Jogo {i}: {sorteio}")
    sleep(0.5)

print("=" * 10, "Boa Sorte!", "=" * 10)
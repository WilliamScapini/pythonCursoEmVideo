import random

estagios = ["pedra","papel","tesoura"]
valor = int(input("Insira:\n1 - pedra\n2 - papel\n3 - tesoura\n"))
indice = valor - 1

aleatorio = random.randint(0,2)
print(f"Minha escolha foi {estagios[aleatorio]}")
if indice == aleatorio:
    print(f"{estagios[indice]} com {estagios[aleatorio]} dá empate")
elif estagios[indice] == "pedra":
    if estagios[aleatorio] == "tesoura":
        print(f"Você venceu!\n{estagios[indice]} ganha de {estagios[aleatorio]}")
    else:
        print(f"Você perdeu!\n{estagios[indice]} perde de {estagios[aleatorio]}")
elif estagios[indice] == "papel":
    if estagios[aleatorio] == "pedra":
        print(f"Você venceu!\n{estagios[indice]} ganha de {estagios[aleatorio]}")
    else:
        print(f"Você perdeu!\n{estagios[indice]} perde de {estagios[aleatorio]}")
elif estagios[indice] == "tesoura":
    if estagios[aleatorio] == "papel":
        print(f"Você venceu!\n{estagios[indice]} ganha de {estagios[aleatorio]}")
    else:
        print(f"Você perdeu!\n{estagios[indice]} perde de {estagios[aleatorio]}")
else:
    print("Você digitou um valor inválido")
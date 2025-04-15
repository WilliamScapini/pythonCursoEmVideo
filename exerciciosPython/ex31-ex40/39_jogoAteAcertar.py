import random
import os
aleatorio = random.randint(0,10)
tentativas = 1
while True:
    if tentativas == 1:
        valor = int(input("Pensei em um número entre 0 e 10 tente acertar:\n"))
    else:
        valor = int(input("Tente outra vez:\n"))
    if (valor == aleatorio) and (tentativas == 1):
        print(f"Caramba!! Você acertou de primeira")
        break
    elif valor == aleatorio:
        print(f"Você acertou! foram {tentativas} tentativas")
        break
    else:
        os.system("clear")
        print("Errou!")
        tentativas += 1

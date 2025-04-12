import random

while True:
    numeroAleatorio = random.randint(1,6)
    valor = input("Tente adivinhar o número de 1 a 6 que pensei:\n")
    if valor.isnumeric():
        res = int(valor)
        if res == numeroAleatorio:
            print(f"Parábens, você acertou pensei examente em {numeroAleatorio}")
            continuacao = input("Quer continuar? (s para sim e n para não):")
            if continuacao == "N" or continuacao =='n':
                break  
        else:
            print(f"ERROU! pensei na verdade no {numeroAleatorio}")
            continuacao = input("Quer continuar? (s para sim e n para não)\n:")
            if continuacao == "N" or continuacao =='n':
                break            
    else:
        print("você digitou um valor inválido, por favor")
while True:
    a = input("Digite 5 números separados por espaço:\n")
    numeros = a.split()
    for i,num in enumerate(numeros):
        if not num.isnumeric():
            print("Algum valor é inválido, por favor!")
            continue
        else:
            numeros[i] = int(num)
    print(f"Dos números que você digitou,\no maior é {max(numeros)} na posição {numeros.index(max(numeros))+1}\nO menor {min(numeros)} na posição {numeros.index(min(numeros))+1}")
    input("")
    break
    

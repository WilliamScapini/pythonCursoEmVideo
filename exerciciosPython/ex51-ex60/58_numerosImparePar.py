arr = []
pares = []
impares = []
print("Digite números não duplicados para colocar em uma lista, obs para parar digite s")
while True:
    valor = input("Digite um número inteiro:")
    if valor.isnumeric():  
        num = int(valor)
        arr.append(num)
    else:
        break
for n in arr:
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Você digitou os valores {arr}\n onde {pares} são pares\n e {impares} são ímpares")
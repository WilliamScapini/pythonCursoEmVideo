arr = []
print("Digite números não duplicados para colocar em uma lista, obs para parar digite s")
while True:
    valor = input("Digite um número inteiro:")
    if valor.isnumeric():  
        num = int(valor)
        if num in arr:
            print("Valor duplicado:")
            continue
        arr.append(num)
    else:
        break
for i,n in enumerate(arr):
    if i != 0:
        while True:
            if n < arr[i-1]:
                arr[i] = arr[i-1]
                arr[i-1] = n
                continue
            else:
                break
print(f"Você digitou os valores\n{arr}")
arr = []
print("=-"*30)
print("Digite uma sequencia de números para obter sua média, maior e menor\n(obs) para parar o progra basta digitar uma letra")
print("=-=-="*12)

while True:
    valor = input("digite os número: ")
    if valor.isnumeric():
        num = int(valor)
        arr.append(num)
    else:
        break
arr.sort()
media = sum(arr)/len(arr)
print(f"O menor dos números digitados foi {arr[0]}\n o maior dos números foi {arr[len(arr)-1]}\ne a média dos números foi {media:.2f}")

valor = input("Dite o primeiro termo de uma PA e sua razão separados por virgula\nex: 5,6\n")
arr = valor.split(",")
arr[0] = int(arr[0])
arr[1] = int(arr[1])
limite = [10]
for i in range(0,limite[0]):
    print(f"{i+1}° Termo = {arr[0]+arr[1]*i}")

c= 0
while True:
    n = int(input("quer que eu mostre mais quantos termos?"))
    if n == 0:
        break
    limite.append(n+limite[c])
    for i in range(limite[c],limite[c+1]):
        print(f"{i+1}° Termo = {arr[0]+arr[1]*i}")
    c += 1

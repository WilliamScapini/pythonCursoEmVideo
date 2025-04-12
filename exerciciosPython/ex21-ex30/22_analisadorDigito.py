a= "-"*20

while True:
    valor = input("Escreva qualquer valor de 0 até 9999:\n")
    if valor.isnumeric() & 0 <= int(valor) <= 9999:
        n=0
        arr = []
        while n < len(valor):
            arr.append(valor[n])
            n = n+1
        i = 1
        while i < 4:
            try:
                arr[i]
                i = i + 1
            except:
                arr.insert(0,"0")
                i = i + 1 
        print(f"{a}\nO seu número tem:\n{arr[0]} milhares\n{arr[1]} centenas\n{arr[2]} dezenas\n{arr[3]} unidades\n{a}")
        break
    else:
        print("Você digitou um valor inválido, por favor")
               


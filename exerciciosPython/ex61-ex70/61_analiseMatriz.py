valor = input("Digite os números de uma matriz separando por espaço para linhas e ; pra colunas\n")
linhas = valor.strip().split(";")
matriz = []
somaNumerosPares = 0
somaTerceiraColuna = 0
for linha in linhas:
    matriz.append(linha.strip().split(" "))
for col in matriz:
    for i,c in enumerate(col):
        col[i] = int(c)
        if col[i]%2 ==0:
            somaNumerosPares += col[i]
    somaTerceiraColuna += col[2]
print("-"*18)
for row in matriz:
    for i in range(0,len(row)):
        if i<2:
            print(f"{row[i]:^4} |",end=" ")
        else:
            print(f"{row[i]:^4}")
print("-"*18)
print(f"A soma dos números pares é {somaNumerosPares}")
print(f"A soma da Terceira coluna é {somaTerceiraColuna}")
print(f"O maior valor da segunda linha é {max(matriz[2])}")
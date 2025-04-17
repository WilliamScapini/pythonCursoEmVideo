valor = input("Digite os números de uma matriz separando por espaço para linhas e ; pra colunas\n")
linhas = valor.strip().split(";")
matriz = []
for linha in linhas:
    matriz.append(linha.strip().split(" "))
for col in matriz:
    for i,c in enumerate(col):
        col[i] = int(c)
print("-"*18)
for row in matriz:
    for i in range(0,len(row)):
        if i<2:
            print(f"{row[i]:^4} |",end=" ")
        else:
            print(f"{row[i]:^4}")
print("-"*18)
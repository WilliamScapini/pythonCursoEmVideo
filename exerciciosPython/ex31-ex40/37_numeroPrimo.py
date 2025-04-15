valor = int(input("digite um número inteiro pra verificar se é primo\n"))
condicao = 'é primo'
for c in range(valor-1,2,-1):
    if valor%c == 0:
        condicao = "Não é primo"
        break
print(f"o número {valor} {condicao}")
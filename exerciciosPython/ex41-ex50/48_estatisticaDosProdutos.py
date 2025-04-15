arr = []
gasto = 0
produtosCaros = 0
while True:
    produto = input("Digite o nome do produto que quer cadastrar: ")
    price = input("Preço do produto que quer cadastrar ")
    if price.isnumeric():
        n = int(price)    
        arr.append([produto,n])
        condicional = input("Quer continuar? [S/N] ")
        if condicional.upper() == "N":
            break
    else:
        print("Valor inválido, por favor\n\n")
valorProdutoMaisBarato = arr[0][1]
produtoMaisBarato = arr[0][0]
for arra in arr:
    gasto += arra[1]
    if arra[1] >= 1000:
        produtosCaros += 1
    if arra[1] < valorProdutoMaisBarato:
        valorProdutoMaisBarato = arra[1]
        produtoMaisBarato = arra[0]
print("==="*15)
print(f"Com os dados digitados temos:\nR${gasto} foi o total gasto\n{produtosCaros} é o número de produtos acima de R$ 1.000,00\nE o produto mais barato foi {produtoMaisBarato} custando R${valorProdutoMaisBarato} ")
produtos_e_precos = (
    "Camiseta", 29.90,
    "Calça Jeans", 89.50,
    "Tênis", 120.00,
    "Meias", 15.00,
    "Boné", 35.50,
    "Mochila", 75.00,
    "Cinto", 45.00,
    "Óculos de Sol", 150.00,
    "Relógio", 220.00,
    "Carteira", 60.00
)
print("-"*30)
print('     LISTAGEM DE PREÇOS  ')
print("-"*30)
for c in range(0,len(produtos_e_precos),2):
    pontos = "."*(20-len(produtos_e_precos[c]))
    print(f"{produtos_e_precos[c]}{pontos}R${produtos_e_precos[c+1]:>7.2f}")
print("-"*30)
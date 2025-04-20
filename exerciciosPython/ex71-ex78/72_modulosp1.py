from modulos.moeda import moeda
p = float(input("Digite um preço R$ "))
print(f"A metade é {moeda.metade(p):.2f}")
print(f"O dobro é {moeda.dobro(p):.2f}")
print(f"Aumentando 10% é {moeda.aumentar(p,10):.2f}")
print(f"Com desconto de 13% é {moeda.diminuir(p,13):.2f}")
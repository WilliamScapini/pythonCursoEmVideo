from modulos.moeda import moeda
p = float(input("Digite um preço R$ "))
print(f"A metade é {moeda.metade(p,True)}")
print(f"O dobro é {moeda.dobro(p,True)}")
print(f"Aumentando 10% é {moeda.aumentar(p,10,True)}")
print(f"Com desconto de 13% é {moeda.diminuir(p,13,True)}")
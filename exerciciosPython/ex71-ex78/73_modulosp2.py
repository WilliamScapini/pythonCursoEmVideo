from modulos.moeda import moeda
from modulos.moeda import real
p = float(input("Digite um preço R$ "))
print(f"A metade é {real.real(moeda.metade(p))}")
print(f"O dobro é {real.real(moeda.dobro(p))}")
print(f"Aumentando 10% é {real.real(moeda.aumentar(p,10))}")
print(f"Com desconto de 13% é {real.real(moeda.diminuir(p,13))}")
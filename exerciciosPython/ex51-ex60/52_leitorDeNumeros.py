n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
tupla = (n1,n2,n3,n4)
print(f"Você digitou os valores {tupla}")
print(f"o  valor 9 apareceu {tupla.count(9)} vezes")
try:
    print(f"O número 3 apareceu primeiro na {tupla.index(3) + 1}ª posição")
except ValueError:
    print(f'O número 3 não apareceu na lista')
contador = []
for val in tupla:
    if val%2 == 0:
        contador.append(val)
print(f"Os valores pares digitados foram {contador[0:]}")
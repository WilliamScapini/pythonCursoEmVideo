valor = int(input("Digite o Valor que você quer sacar: R$"))

cedulas = [50, 20, 10, 5, 1]

contagem_cedulas = [0] * len(cedulas)

for i, cedula in enumerate(cedulas):# itera sobre a lista 'cedulas'. A função 'enumerate' retorna tanto o índice (i) quanto o valor (cedula) de cada elemento da lista.
    contagem_cedulas[i] = valor // cedula
    valor %= cedula

print("=" * 30)
for i, cedula in enumerate(cedulas):
    if contagem_cedulas[i] != 0:
        print(f"Total de {contagem_cedulas[i]} cédulas de R$ {cedula}")
print("=" * 30)
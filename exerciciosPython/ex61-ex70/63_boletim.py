alunos = []

while True:
    nome = input("Nome do Aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        break

print("=" * 30)
print(f"{'Nº':<3} {'Nome':<10} {'Média':>6}")
print("-" * 30)
for i, aluno in enumerate(alunos):
    print(f"{i:<3} {aluno[0]:<10} {aluno[2]:>6.2f}")
print("=" * 30)

while True:
    indice = int(input("Mostrar as notas de qual aluno? (número negativo para sair): "))
    if indice < 0:
        break
    if 0 <= indice < len(alunos):
        nome, notas = alunos[indice][0], alunos[indice][1]
        print(f"Notas de {nome}: {notas}")
    else:
        print("Número inválido.")
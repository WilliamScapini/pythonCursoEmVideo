pessoas = []
pessoa = {}

while True:
    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = input("Sexo:[M/F]\n").upper()
    pessoa["idade"] = int(input("idade: "))
    pessoas.append(pessoa.copy())
    condicional = input("Quer Continuar? [S/N]")
    if condicional.upper() == 'N':
        break
print("="*30)
print(f"O número de pessoas cadastradas foi {len(pessoas)}")
media = 0
mulheres = []
pessoasAcimaMedia = []
for pess in pessoas:
    media += pess["idade"]/len(pessoas) 
    if pess["sexo"] == 'F':
        mulheres.append(pess)
print(f"A média de idade é {media:.2f}")
print(f"Lista com todas as mulheres")
for mulher in mulheres:
    print(mulher["nome"],end=", ")
print(f"\nLista com pessoas acima da média {media:.2f}:")
for pess in pessoas:
    if pess["idade"] > media:
        print(f"{pess['nome']} com a idade de {pess['idade']}")

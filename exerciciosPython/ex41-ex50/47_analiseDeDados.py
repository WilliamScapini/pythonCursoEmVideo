arr = []
tem18 = 0
homens = 0
mulherMenorDeVinte = 0
while True:
    sexo = input("Digite o sexo da pessoa que quer cadastrar:[M/F]: ")
    if (sexo.upper() == "M") or (sexo.upper() == "F"):
        idade = int(input("Digite a idade da pessoa que quer cadastrar "))
        arr.append([sexo.upper(),idade])
        condicional = input("Quer continuar? [S/N] ")
        if condicional.upper() == "N":
            break
    else:
        print("Valor inválido, por favor")
for arra in arr:
    if arra[1] >= 18:
        tem18 += 1
    if arra[0] == "M":
        homens += 1
    if (arra[0] == "F")and (arra[1] < 20):
        mulherMenorDeVinte += 1

print(f"Com os dados digitados temos:\n{tem18} pessoas tem 18 anos ou mais\n{homens} pessoas são homens\n{mulherMenorDeVinte} mulheres tem menos de 20 anos")
import datetime
hoje = datetime.date.today()
valor = input("digite a data de nascimento do aluno no formato DD/MM/AAAA:\n")
def calculoIdade(val):
    dataAluno = val.split('/')
    if checkArr(dataAluno):
        if int(dataAluno[1]) < hoje.month:
            idade = hoje.year -int(dataAluno[2])
        elif int(dataAluno[1])> hoje.month:
            idade = hoje.year - int(dataAluno[2])-1
        else:
            if int(dataAluno[0]) <= hoje.day:
                idade = hoje.year - int(dataAluno[2])
            else:
                idade = hoje.year - 1-int(dataAluno[2])
        if idade < 0:
            return "Data inválida"
        return idade
    else:
      return "Você digitou um ano inválido"

def checkArr(arr):
    try:
        for val in arr:
            int(val)
        return True
    except ValueError:
        return False
    
idade = calculoIdade(valor)
if idade <= 9:
    categoria = "MIRIM"
elif idade <=14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"
print(f"A categoria do atleta é {categoria}")
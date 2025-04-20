from datetime import datetime
trabalhador = {}
nome = input("Qual seu nome? ")
while True:
    ano = input("Em que ano você nasceu? ")
    if ano.isnumeric():
        anonum = int(ano)
        if anonum < 2025:
            trabalhador["idade"]=datetime.now().year-anonum
            break
        else:
            print("ano inválido, por favor:")
    else:
        print("ano inválido, por favor: ")
while True:
    anosCarteira = input("Quantos anos de carteira assinada você tem? ")
    if anosCarteira.isnumeric():
        anoCartNum = int(anosCarteira)
        if anonum < 0:
            trabalhador["anosCarteira"]= 0
            break
        trabalhador["anosCarteira"] = anoCartNum
        trabalhador["anoDeContratacao"] = datetime.now().year - anoCartNum
        salario = float(input("Qual seu sálario? "))
        trabalhador["sálario"] = salario
        trabalhador["anoDeAposentadoria"] = trabalhador["idade"] + 35
        break
    else:
        print("ano inválido, por favor:")
print("=-="*15)
print()
for k,v in trabalhador.items():
    print(f"{k} tem o valor {v}")
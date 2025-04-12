valorDaCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos você pretende pagar? '))
# Calculo da prestação mensal
prestacao = valorDaCasa / (tempo * 12)
# Calculo de 30% do salário
trintaPorcento = salario * 0.3
# Verifica se a prestação mensal é maior que 30% do salário
if prestacao <= trintaPorcento:
    print(f'Empréstimo aprovado! Sua prestação mensal será de R$ {prestacao:.2f}')
else:
    print(f'Empréstimo negado! Sua prestação mensal de R$ {prestacao:.2f} é maior que 30% do seu salário de R$ {salario:.2f}')
# Fim do código
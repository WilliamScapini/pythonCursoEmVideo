valor = input("Qual a velocidade em km/h do seu carro?\n")
if valor.isnumeric():
    num = int(valor)
    if num > 80:
        velAcima = num - 80
        multa = velAcima * 7
        print(f"você está acima do limite da rodovia de 80Km/h em {velAcima}\nMulta de R$ {multa:.2f}")
else: 
    print('valor inválido')
condicional = True
def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False

while condicional:
    valor = input("1 U$ Dolar = R$ 5,97\nQuanto de reais você deseja converter?\n")
    if isFloat(valor):
        num = float(valor)
        print('você pode comprar U${:.2f} com essa cotação:'.format(num/5.97))
        condicional = False
    else:
        print('Você digitou um valor inválido\nPor favor')
        
condicional = True
def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False

while condicional:
    valor1 = input("Qual o valor da temperatura em Graus Celsius °C ?\n")
    if isFloat(valor1):
        num = float(valor1)
        fahrenheit = 5/9 * (num-32)
        print("A temperatura de {:.2f}°C em fahrenheit é {:.2f}°F".format(num,fahrenheit))
        condicional = False
    else:
        print('Você digitou um valor inválido\nPor favor')
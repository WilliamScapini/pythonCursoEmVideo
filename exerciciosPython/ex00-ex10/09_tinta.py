condicional = True
condicional1 = True
def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False

while condicional:
    valor1 = input("Digite o valor da altura da parede:\n")
    if isFloat(valor1):
        altura = float(valor1)
        while condicional1:
            valor2 = input("Digite o valor da base da parede:\n")
            if isFloat(valor2):
                base = float(valor2)
                area = base * altura
                print("Sua parede tem {:.2f}M² e você precisará de {:.2f}L de tinta para pintá-la".format(area,area/2))
                condicional = False
                condicional1 = False
            else: 
                print('Você digitou um valor inválido\nPor favor')
    else:
        print('Você digitou um valor inválido\nPor favor')
        
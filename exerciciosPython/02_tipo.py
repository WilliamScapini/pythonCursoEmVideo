def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

valor = input('digite algo:')
def tipo(val):
    if val.isnumeric():
        return 'Número'
    elif val.isalpha():
        return "Letra"
    elif val.isalnum():
        return 'Alfanúmerico'
    elif val.isspace():
        return "Espaço em branco"
    elif isFloat(val):
        return "Número decimal"
    elif val.isascii():
        return 'Caracter especial'

print('{} é do tipo {} em Python'.format(valor,tipo(valor)))
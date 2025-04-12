def binario(numero):
    num = int(numero)
    if num == 0:
        return "0"
    arr = []
    while num > 0:
        r = num % 2
        arr.insert(0, str(r))
        num = num // 2
    return int("".join(arr))
    
def octal(numero):
    num = int(numero)
    if num == 0:
        return "0"
    arr = []
    while num > 0:
        r = num % 8
        arr.insert(0, str(r))
        num = num // 8
    return int("".join(arr))

def hexaDecimal(numero):
    num = int(numero)
    if num == 0:
        return "0"
    arr = []
    hexa = ["0", "1", "2", "3", "4", "5", "6", "7", 
            "8", "9", "A", "B", "C", "D", "E", "F"]
    while num > 0:
        r = num % 16
        arr.insert(0, hexa[r])
        num = num // 16 
    return "".join(arr)

baseEscolhida = int(input('Escolha a base de conversão: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))
numero = int(input('Digite um número inteiro para conversão:\n'))

while True:
    if baseEscolhida == 1:
        print(f'O número {numero} em binário é {binario(numero)}')
        break
    elif baseEscolhida == 2:
        print(f'O número {numero} em octal é {octal(numero)}')
        break
    elif baseEscolhida == 3:
        print(f'O número {numero} em hexadecimal é {hexaDecimal(numero)}')
        break
    else:
        print('Opção inválida! Escolha 1, 2 ou 3.')
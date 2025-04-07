condicional = True

while condicional:
    valor = input("Digite um número inteiro para ver sua tábuada:")
    if valor.isnumeric():
        num = int(valor)
        print('A tábuada do {} é:\n'.format(num))
        for i in range(11):
            print("{} X {} = {}\n".format(num,i,num*i))
    else:
        print('Você digitou um valor inválido\nPor favor')
        
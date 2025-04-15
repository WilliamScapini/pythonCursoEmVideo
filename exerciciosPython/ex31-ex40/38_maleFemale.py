import os
while True:
    valor = input("Digite seu sexo com \n'm' - masculino\n'f' - feminino\n")
    if (valor.upper() == 'M') or (valor.upper() == "F"):
        print("Muito obrigado")
        break
    else:
        os.system("clear")
        print('você digitou um valor inválido, por favor:')
    
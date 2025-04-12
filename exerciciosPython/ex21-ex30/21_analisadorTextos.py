import os
valor = input("Digite seu nome completo!\n")
os.system("clear")
print("Seu nome todo em maiúsculas é:\n{}\n".format(valor.upper()))
print("Seu nome todo em minúsculas é:\n{}\n".format(valor.lower()))
nomeSemespaço = valor.replace(" ",'')
print("Seu nome tem ao todo {} Letras\n".format(len(nomeSemespaço)))
nomeSplit = valor.split()
print("\nSeu primeiro nome tem ao todo {} Letras\n".format(len(nomeSplit[0])))


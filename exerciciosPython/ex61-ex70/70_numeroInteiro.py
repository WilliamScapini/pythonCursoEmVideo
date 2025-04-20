def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
        else:
            print("\033[31mERRO! digite um número inteiro válido!\033[0m")
num = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número inteiro {num}")
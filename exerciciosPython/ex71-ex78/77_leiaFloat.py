def leiaInt(msg):
    while True:
        n = input(msg)
        n = n.strip()
        if n.isspace() or n == "":
            print("\033[31mO usuario preferiu não digitar esse número, será atribuido 0\033[0m")
            return 0
        if n.isnumeric():
            return n
        else:
            print("\033[31mERRO! digite um número inteiro válido!\033[0m")

def leiaFloat(msg):
    while True:
        n = input(msg)
        n = n.strip()
        if n.isspace() or n == "":
            print("\033[31mO usuario preferiu não digitar esse número, será atribuido 0\033[0m")
            return 0
        try:
            num = float(n)
            return n
        except Exception as erro:
            print("\033[31mERRO! digite um número real válido!\033[0m")


num = leiaInt("Digite um número inteiro: ")
num1 = leiaFloat("Digite um número real: ")
print(f"Você digitou o número inteiro {num}, e o número real {num1}")
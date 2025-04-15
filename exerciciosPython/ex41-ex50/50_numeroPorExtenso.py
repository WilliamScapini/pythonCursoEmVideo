numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)
while True:
    numero = int(input("Digite um numero entre 0 e 20\n"))
    if 0 <= numero <= 20:
        print(f"Você digitou o número {numeros_extenso[numero]}")
        break
    else:
        print("Tente Novamente ", end=" ")    
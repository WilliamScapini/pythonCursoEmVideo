preco = float(input("Insira o preço do produto\n"))
while True:
    formaDePagamento = input("insira os numeros das seguintes formas de pagmaento:\n1 - À Vista(dinheiro/pix)\n2 - À vista(cartão)\n3 - 2X(cartão)\n4 - 3x ou mais(cartão)\n")
    if formaDePagamento == '1':
        print(f"o valor a pagar é R${preco*0.9}")
        break
    elif formaDePagamento == '2':
        print(f"o valor a pagar é R${preco*0.95}")
        break
    elif formaDePagamento == '3':
        print(f"o valor a pagar é R${preco}")
        break
    elif formaDePagamento == '4':
        print(f"o valor a pagar é R${preco*1.2}")
        break
    else:
        print("você digitou uma forma de pagamento errada")
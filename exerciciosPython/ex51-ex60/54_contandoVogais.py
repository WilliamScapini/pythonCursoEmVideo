palavras = ("casa", "carro", "livro", "mesa", "cadeira", "computador", "telefone", "janela", "porta", "luz")
vogais = "AEIOU"

for palavra in palavras:
    print(f"Na palavra {palavra} temos ", end="")
    for letra in palavra:
        if letra.upper() in vogais:
            print(letra, end=" ")
    print("\n")
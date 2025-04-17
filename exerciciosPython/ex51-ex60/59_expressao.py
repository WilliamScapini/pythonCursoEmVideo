valor = input("Digite a expressão\n")
if valor.count("(") == valor.count(")"):
    print("Expressão válida!")
else:
    print("Expressão inválida")
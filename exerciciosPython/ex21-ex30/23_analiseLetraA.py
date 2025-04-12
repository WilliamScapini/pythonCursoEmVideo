while True:
    valor = input("Escreva uma frase Qualquer\n")
    if valor.isspace() or valor.isnumeric():
        print("\nVocê digitou uma frase inválida,por favor")
    else:
        numA = valor.lower().count("a")
        namSemEspaco = valor.lower().replace(" ","")
        posLetraA = namSemEspaco.find('a') + 1
        fraseReverse = namSemEspaco.rfind('a') + 1 
        print(f"A letra A aparece {numA} vezes\nA sua primeira aparecisão foi na letra N°{posLetraA}\ne sua última aparcição é na posição N°{fraseReverse}")
        break
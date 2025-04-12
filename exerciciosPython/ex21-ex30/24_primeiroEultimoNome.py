while True:
    valor = input("Escreva seu nome Qualquer\n")
    if valor.isspace() or valor.isalnum():
        print("\nVocê digitou um valor inválido,por favor")
    else:
        arr = valor.split()
        print(f"Olá {arr[0].capitalize()}, seu primeiro nome obviamente é {arr[0].capitalize()}\nE seu último nome é {arr[len(arr)-1].capitalize()}")
        break
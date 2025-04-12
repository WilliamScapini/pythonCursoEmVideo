valor = input("Digite 3 valores separados por espaços\n")
arr = valor.split()
arr.sort()
print(f"O maior número é o {arr[2]} e o menor é {arr[0]}")
valor = input("Digite o comprimento de 3 seguimentos de retas separdos por espaços:\n")
arr = valor.split()
i = 0 
while i < len(arr):
   arr[i] = float(arr[i])
   i = i + 1 
arr.sort()
if arr[0] + arr[1] > arr[2]:
   print(f"Os seguintos {arr[0]}, {arr[1]} e {arr[2]}\npodem formar um triângulo")
else:
   print(f"Os seguintos {arr[0]}, {arr[1]} e {arr[2]}\nnão podem formar um triângulo")
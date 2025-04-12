def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False
    
condicional = True

while condicional:
    valor = input("Digite o valor em metros que deseja converter:\n")
    if isFloat(valor):
        val = float(valor)
        print("\tVocê digitou {} m,\n\ttambém pode ser escrito como {} cm\n\te {} mm".format(val,val*100,val*1000))
        condicional = False
    else:
        print("Você digitou um valor inválido\npor favor:")    

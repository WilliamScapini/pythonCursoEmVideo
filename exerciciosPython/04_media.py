def isFloat(f):
    try: 
        float(f)
        return True
    except ValueError:
        return False
    
notas = []
condicional = True
while condicional:
    valor = input('Digite a nota do aluno:\n')
    if isFloat(valor):
        notas.append(float(valor))
        soun = input('Digite n se acabaram as notas ou s se tem mais notas\n')
        condicional = soun == 's'or soun == "S"
    else:
        print("Você digitou um valor inválido\n por favor")
def media(arr):
    tamanho = len(arr)
    med = sum(arr)/tamanho        
    return med

mediaF = media(notas)
print("a média final é {}".format(mediaF))

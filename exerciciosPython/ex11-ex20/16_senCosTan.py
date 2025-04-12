import math as mat
import os

condicional = True 
condicional1 = True

def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False
 
while condicional:
    valor1 = input("Digite um angulo em graus\n")
    if isFloat(valor1):
        numGraus = float(valor1)
        numRad = numGraus * mat.pi /180
        senCosTan = [mat.sin(numRad),mat.cos(numRad),mat.tan(numRad)]
        print("Para o angulo de {:.1f}° temos:\nseno = {:.3f}\ncosseno = {:.3f}\ntangente = {:.3f}".format(numGraus, senCosTan[0], senCosTan[1], senCosTan[2]))
        condicional = False   
    else:
        os.system("clear")
        print("Vocẽ digitou um valor invalido,\npor favor")
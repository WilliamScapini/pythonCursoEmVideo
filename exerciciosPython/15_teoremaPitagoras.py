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
    valor1 = input("Escreva o valor do cateto oposto do seu triângulo retângulo \n")
    if isFloat(valor1):
        catoposto = float(valor1)
        condicional = False
        while condicional1:    
            valor2 = input("Escreva o valor do cateto adjacente do seu triângulo retângulo \n")
            if isFloat(valor2):
                catadjacente = float(valor2)
                hipotenusa = mat.sqrt(mat.pow(catadjacente,2)+mat.pow(catoposto,2))
                print("Com os catetos sendo {:.2f} e {:.2f}\n a hipotesuna será {:.2f}".format(catoposto,catadjacente,hipotenusa))
                condicional1 = False
            else:
                os.system("clear")
                print("Vocẽ digitou um valor invalido,\npor favor")     
    else:
        os.system("clear")
        print("Vocẽ digitou um valor invalido,\npor favor")
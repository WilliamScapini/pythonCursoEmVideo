def fatorial(num,show=False):
    """
    O Fatorial calcula o fatorial de um número n(inteiro e não negativo)
    n! = n x (n-1) x (n-2) ... x 1 
    passando somente o número como paramento, retorna um número que é o resultado do fatorial
    passando outro parametro show=True, retorna uma string com a conta realizada ex:
    fatorial(5,show=True) -> retorna 5 x 4 x 3 x 2 x 1 = 120
    """
    if num == 0:
        return 1
    if num > 0:
        f = 1
        numeros = [num]
        while num > 1:
            f *= num
            num -= 1
            numeros.append(num)
        numeros.pop()
        if show:
            frase = ""
            for n in numeros:
                frase += "{} X ".format(n)
            frase += "1 = {}".format(f)
            return frase
        return f
    else:
        return "Não Existe Fatorial de número negativo"

help(fatorial)
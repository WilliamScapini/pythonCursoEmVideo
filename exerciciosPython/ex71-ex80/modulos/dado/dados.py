def isFLoat(p):
    """
    Verifica se um determinado valor pode ser convertido para o tipo float.

    Args:
        p (str): O valor a ser verificado.

    Returns:
        bool: True se o valor puder ser convertido para float, False caso contrário.
    """
    try:
        float(p)
        return True
    except ValueError:
        return False

def leiaDinheiro(msg):
    """
    Solicita ao usuário a entrada de um valor monetário e o valida,
    garantindo que seja um número de ponto flutuante válido.
    Aceita vírgula como separador decimal e a converte para ponto.

    Args:
        msg (str): A mensagem a ser exibida para o usuário solicitando a entrada.

    Returns:
        float: O valor monetário inserido pelo usuário como um número float.
               O loop continua até que uma entrada válida seja fornecida.
    """
    while True:
        a = input(msg)
        a = a.strip()
        if "," in a:
           a = a.replace(",",".")
        if isFLoat(a):
            a = float(a)
            return a
        else:
            print("ERRO! esse valor é inválido, por favor")

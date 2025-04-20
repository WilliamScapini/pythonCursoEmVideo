def metade(num, formated=False):
    """
    Calcula a metade de um número.

    Args:
        num (float): O número do qual se deseja calcular a metade.
        formated (bool, opcional): Indica se o resultado deve ser formatado como moeda.
                                    Padrão é False.

    Returns:
        float ou str: A metade do número. Se `formated` for True, retorna uma string
                      formatada como moeda (R$ com duas casas decimais).
                      Caso contrário, retorna um float.
    """
    if formated:
        return f"R$ {num/2:.2f}"
    return num/2

def dobro(num, formated=False):
    """
    Calcula o dobro de um número.

    Args:
        num (float): O número do qual se deseja calcular o dobro.
        formated (bool, opcional): Indica se o resultado deve ser formatado como moeda.
                                    Padrão é False.

    Returns:
        float ou str: O dobro do número. Se `formated` for True, retorna uma string
                      formatada como moeda (R$ com duas casas decimais).
                      Caso contrário, retorna um float.
    """
    if formated:
        return f"R$ {num*2:.2f}"
    return num*2

def aumentar(num, percent, formated=False):
    """
    Aumenta um número em uma determinada porcentagem.

    Args:
        num (float): O número a ser aumentado.
        percent (float): A porcentagem de aumento.
        formated (bool, opcional): Indica se o resultado deve ser formatado como moeda.
                                    Padrão é False.

    Returns:
        float ou str: O resultado do aumento. Se `formated` for True, retorna uma string
                      formatada como moeda (R$ com duas casas decimais).
                      Caso contrário, retorna um float.
    """
    mult = percent/100
    if formated:
        return f"R$ {num*(mult+1):.2f}"
    return num*(mult+1)

def diminuir(num, percent, formated=False):
    """
    Diminui um número em uma determinada porcentagem.

    Args:
        num (float): O número a ser diminuído.
        percent (float): A porcentagem de redução.
        formated (bool, opcional): Indica se o resultado deve ser formatado como moeda.
                                    Padrão é False.

    Returns:
        float ou str: O resultado da redução. Se `formated` for True, retorna uma string
                      formatada como moeda (R$ com duas casas decimais).
                      Caso contrário, retorna um float.
    """
    mult = percent/100
    if formated:
        return f"R$ {num*(1-mult):.2f}"
    return num *(1-mult)

def resumo(num, a, d):
    """
    Exibe um resumo formatado contendo o preço analisado, o dobro, a metade,
    o aumento e a redução percentual de um determinado valor.

    Args:
        num (float): O preço base a ser analisado.
        a (float): A porcentagem de aumento a ser aplicada.
        d (float): A porcentagem de redução a ser aplicada.

    Returns:
        None: Esta função apenas imprime informações formatadas e não retorna um valor.
    """
    print("-" * 29)
    print("       RESUMO DO VALOR")
    print("-" * 29)
    print(f"Preço analisado:      R$ {num:.2f}")
    print(f"Dobro do preço:       {dobro(num, True)}")
    print(f"Metade do preço:      {metade(num, True)}")
    print(f"Aumento de {a:2}%:       {aumentar(num, a, True)}")
    print(f"Redução de {d:2}%:       {diminuir(num, d, True)}")
    print("-" * 29)
    input()


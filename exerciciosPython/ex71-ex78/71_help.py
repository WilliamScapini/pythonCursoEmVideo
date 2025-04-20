def escreva(msg,color="\33[0m"):
    a = (len(msg)+4)*"-"
    print(f"{color}{a}\33[0m")
    print(f"{color}  {msg}  \33[0m")
    print(f"{color}{a}\33[0m")

def pyHelp():
    while True:
        escreva("Sistema de ajuda pyHelp","\33[42;30m")
        h = input('função ou biblioteca > ')
        if h.upper() == "FIM":
            escreva("ATÉ MAIS",'\33[41;37m')
            break
        else:
            try:
                # Tenta obter o objeto pelo nome
                obj = eval(h)
                if hasattr(obj, '__doc__'):
                    escreva(str(obj.__doc__), '\33[47;30m')
                else:
                    escreva(f"A ajuda para '{h}' não está disponível.", '\33[41;30m')
            except NameError:
                escreva(f"'{h}' não foi encontrado.", '\33[41;30m')
            except Exception as e:
                escreva(f"Erro ao acessar a ajuda para '{h}': {e}", '\33[41;30m')
            input("")
        
pyHelp()
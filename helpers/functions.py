
def derivada(funcao, x, delta = 10**(-10)):
    """
    Retorna a derivada de uma funcao no ponto x.    
    """
    return (funcao( x + delta ) - funcao(x)) / delta

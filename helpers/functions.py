
def derivada(funcao, x, delta = 10**(-10)):
    """
    Retorna a derivada de uma funcao no ponto x.    
    """
    return (funcao( x + delta ) - funcao(x)) / delta


def derivadaParcial(func, X, xIndex):
    dx = 1**-10
    y1 = func(X)
    X[xIndex] += dx
    y2 = func(X)
    X[xIndex] -= dx 
    return (y2 - y1)/dx


# creates matrix with m rows, n columns filled with value
def createMatrix(m,n,value):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(value)
    return matrix


# X : vetor of paramentes for X
# funcs : vetor of functions
def jacobianMatrix(funcs, X):
    J = createMatrix(len(funcs), len(X), None)
    for i in range(len(funcs)):
        for j in range(len(X)):
            J[i][j] = derivadaParcial(funcs[i], X, j)
    return J
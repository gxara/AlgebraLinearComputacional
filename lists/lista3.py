from helpers import operations



class Lista3:
    def __init__(self):
        pass

    @staticmethod
    def exercicio1():
        # Interpolação é encontrar uma função cuja curva passe exatamente sobre todos os pontos de um conjunto de pontos observados.
        # O objetivo aqui é, dados os pontos de x e y, encontrar os coeficientes que fazem o melhor ajuste da curva.
        x = [[1],[2],[3]]
        y = [[1],[2],[9]]

        p = operations.create_vandermonde_matrix(x)
        pT = operations.transpose(p)
        pTp = operations.multiply(pT,p)
        reverse_pTp = operations.getMatrixInverse(pTp)
        a = operations.multiply(reverse_pTp , pT)
        coeficientes = operations.multiply(a, y)
        print(coeficientes)

    @staticmethod
    def exercicio2():
        # Interpolação é encontrar uma função cuja curva passe exatamente sobre todos os pontos de um conjunto de pontos observados.
        # O objetivo aqui é, dados os pontos de x e y, encontrar os coeficientes que fazem o melhor ajuste da curva.
        x = [[1],[2],[3],[4]]
        y = [[1],[2],[9],[20]]

        p = operations.create_vandermonde_matrix(x)
        pT = operations.transpose(p)
        pTp = operations.multiply(pT,p)
        reverse_pTp = operations.getMatrixInverse(pTp)
        a = operations.multiply(reverse_pTp , pT)
        coeficientes = operations.multiply(a, y)
        print(coeficientes)


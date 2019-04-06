from helpers import operations
from helpers import Formatter


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
        
        print('\n')
        print('*** Exercício 1 ***\n')
        print('A resposta é:\t')
        for row in coeficientes:
            sign = '+' if row[0] > 0 else ''
            print(sign, row[0],'x^{}'.format(coeficientes.index(row) ), end='')
        print('\n')



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

        print('*** Exercício 2 ***\n')
        print('A resposta é:\t')
        Formatter.print_matrix(coeficientes)
        print('\n')

    @staticmethod
    def exercicio3():
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


        print('*** Exercício 3 ***\n')
        print('A resposta é:\t')
        Formatter.print_matrix(coeficientes)
        print('\n')

    @staticmethod
    def exercicio7():
        # Podemos resolver um sistema de equações utilizando matrizes
        # AX = Y
        A = [[1, -1, 1],[2, 3, 1],[-2, 2, 3]]
        Y = [[9], [5], [2]]
        inverse_A = operations.getMatrixInverse(A)
        X = operations.multiply(inverse_A, Y)
        print('*** Exercício 7 ***\n')
        print('A resposta é:\t')
        print(X)
        print('\n')

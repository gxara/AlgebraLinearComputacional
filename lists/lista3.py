from helpers import operations, linear_regression
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
        pTp = operations.multiply_matrices(pT,p)
        reverse_pTp = operations.getMatrixInverse(pTp)
        a = operations.multiply_matrices(reverse_pTp , pT)
        coeficientes = operations.multiply_matrices(a, y)
        
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
        pTp = operations.multiply_matrices(pT,p)
        reverse_pTp = operations.getMatrixInverse(pTp)
        a = operations.multiply_matrices(reverse_pTp , pT)
        coeficientes = operations.multiply_matrices(a, y)

        print('*** Exercício 2 ***\n')
        print('A resposta é:\t')
        for row in coeficientes:
            sign = '+' if row[0] > 0 else ''
            print(sign, row[0],'x^{}'.format(coeficientes.index(row) ), end='')
        print('\n')



    @staticmethod
    def exercicio3():
        # Interpolação é encontrar uma função cuja curva passe exatamente sobre todos os pontos de um conjunto de pontos observados.
        # O objetivo aqui é, dados os pontos de x e y, encontrar os coeficientes que fazem o melhor ajuste da curva.
        import matplotlib.pyplot as plt
        import numpy as np

        explicacao = 'Para melhor ajustarmos um conjunto de pontos a uma função f(x), precisamos achar os coeficientes que melhor aproximam a curva da função com os pontos dados.\n'

        print('*** Exercício 3 ***\n')

        print(explicacao)
        
        print('A resposta é:\t')

        x_points = np.linspace(0, 6, 1000)
        y_points = []


        x = [1,2,3,4]
        y = [1,2,9,20]

        plt.scatter(x,y)

        for x in x_points:
            y = (8) -(11.6653*x) + (5*x**2) - (0.33259*x**3)
            y_points.append(y)
        
        plt.plot(x_points,y_points)
        plt.show()
        return


    @staticmethod
    def exercicio4():
        # Para este exercício, utilizaremos o método lagrange definido na biblioteca scipy
        
        from scipy.interpolate import lagrange

        x = [1,2,3,4]
        y = [1,2,9,20]
        
        p = lagrange(x,y)

        print('\n')
        print('*** Exercício 4 ***\n')
        print('Para o exercício 4, precisamos encontrar uma função que aproxime um conjunto de pontos através da interpolação de lagrange\n')
        print('Os pontos são: x = {} , y = {}\n'.format(x,y))
        print('A resposta é:\t')

        print(p)

        return p



    @staticmethod
    def exercicio6():

        print('\n')
        print('*** Exercício 6 ***\n')
        print('Dado que x = 3.5 , temos que determinar o valor de y utilizando cada um dos polinômios encontrados nos exercícios anteriores.')
        
        x = 3.5
        y1 = (6) -(8*x) + (3*x**2)
        y2 = (8) -(11.6653*x) + (5*x**2) - (0.33259*x**3)
        #y3 não se aplica. No exercício 3 apenas ajustamos graficamente os pontos do exercício 2 à função encontrada pela interpolação polinomial
        y4 = (8) -(11.67*x) + (5*x**2) - (0.3333*x**3)        
        # y5 ainda falta fazer


        print('A resposta é:\t')
        print('Para a função do exercício 1: y = {}'.format(y1))
        print('Para a função do exercício 2: y = {}'.format(y2))
        print('Para a função do exercício 4: y = {}'.format(y4))

        return


    @staticmethod
    def exercicio7():
        # Podemos resolver um sistema de equações utilizando matrizes
        # AX = Y
        A = [[1, -1, 1],[2, 3, 1],[-2, 2, 3]]
        Y = [[9], [5], [2]]
        inverse_A = operations.getMatrixInverse(A)
        X = operations.multiply_matrices(inverse_A, Y)
        print('\n')
        print('*** Exercício 7 ***\n')
        print('A resposta é:\t')
        print(X)
        print('\n')

        return




    @staticmethod
    def exercicio9():
        # Dado o conjunto de pontos abaixo, precisamos encontrar os parâmetros a e b  da equação f(x) = a*ln(x) + b / (x**2 + 1)
        print('\n')
        print('*** Exercício 9 ***\n')
        print('O exercício pede para que seja preparada uma função que retorne os parâmetros a e b de uma reta, a partir de N pares de pontos fornecidos pelo usuário\n')
        print('\n')
 
        print('A função foi definida e se encontra no diretório helpers.\n')
        
        return
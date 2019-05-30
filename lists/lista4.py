from helpers import Formatter, functions
import math
import numpy as np
from numpy import linalg
from numpy.linalg import inv


class Lista4:
    def __init__(self):
        pass

    @staticmethod
    def original_function(x):
        y = x**2 - 4*math.cos(x)
        return y


    @staticmethod
    def bissecao(function, a, b, tolerance=0.0001):
        """
        Funçao para obter a raiz de uma equação f(x) 
        pelo método da bisseção.
        É necessário conhecer previamente um intervalo [a,b] tal que 
        f(a) < 0 e f(b) > 0  ou f(a) > 0 e f(b) < 0.
        Parâmetros necessários: a, b, e a função f(x)
        Parâmetro opcional: tolerância (default = 0.0001)
        """
        iter = 0
        while (abs(b - a) > tolerance):
            iter +=1
            xi = abs(a + b) / 2
            fi = function(xi)
            if fi > 0:
                b = xi
            else:
                a = xi
            
            # print(xi)
        
        print("A raiz obtida pelo método da bisseção é: {0}".format(xi), "e foram necessarias {} iterações".format(iter))
        
        return xi



    @staticmethod
    def derivada(funcao, x, delta = 10**(-10)):
        """
        Retorna a derivada de uma funcao no ponto x.    
        """
        return (funcao( x + delta ) - funcao(x)) / delta



    @staticmethod 
    def newton(f, x0, N_iter, delta=0.0001, tolerance=0.0001):
        """
        PROGRAMA 2
        Método para obter a raiz de uma função f
        pelo método de Newton.
        """


        for iter in range(N_iter):
            new_x = x0 - f(x0) / Lista4.derivada(f, x0)
            # print(new_x)
            tol_iter = abs(new_x - x0)
            # print(tol_iter)
            if tol_iter < tolerance:
                print("A raiz obtida pelo método de newton é: {0}".format(new_x), "e foram necessarias {} iterações".format(iter))
                return new_x
            x0 = new_x
        print("O método newton não convergiu")
        return
     



    @staticmethod 
    def newton_secante(f, x0, N_iter, delta=0.0001, tolerance=0.0001):
        """
        Método para obter a raiz de uma função f
        pelo método de Newton-Raphson.
        """
        x1 = x0 + delta

        for iter in range(N_iter):
            try:
                f0 = f(x0)
                f1 = f(x1)
                new_x = x1 - f1*(x1-x0) / f1 - f0
                tol_iter = abs(new_x - x1)
                if tol_iter < tolerance:
                    print("A raiz obtida pelo método de newton-secante é: {0}".format(x1), "e foram necessarias {} iterações".format(iter))
                    return x1
                x0 = x1
                x1 = new_x
            except OverflowError:
                print("O método newton-secante não convergiu")
                return
        print("O método newton-secante não convergiu")
        return
     

    @staticmethod 
    def interpolacao_inversa(f, pontos,  N_iter, tolerance=0.0001):
        """
        Método para obter a raiz de uma equação f(x) 
        pelo método da interpolacao inversa.
        Parâmetro opcional: tolerância (default = 0.0001)
        """
        sorted(pontos)

        x0 = 10**(36)

        for iter in range(N_iter):
            f1 = f(pontos[0])
            f2 = f(pontos[1])
            f3 = f(pontos[2])

            new_x = (f2*f3*pontos[0])/((f1-f2)*(f1-f3)) + (f1*f3*pontos[1])/((f2-f1)*(f2-f3)) + (f1*f2*pontos[2])/((f3-f1)*(f3-f2))
            tol_iter = abs(new_x - x0)
            
            if(tol_iter < tolerance):
                print("A raiz obtida pelo método da interpolação inversa é: {0}".format(new_x), "e foram necessarias {} iterações".format(iter))
                return new_x

            y = [f1, f2, f3]
            i = y.index(max(y))
            pontos[i] = new_x
            sorted(pontos)
            x0 = new_x
                
        print("O método da interpolação inversa não convergiu")
        return


    @staticmethod
    def newton_equation_solver(functionArray, X0, tol, symbols):
        """
        PROGRAMA 4
        Método para achar a solução de um sistema com N equações e N incógnitas
        pelo método de Newton.

        F = Vetor de funções   
        X0 = vetor solução de partida
        JF = Jacobiano aplicado a F
        (ainda precisa ser definido um método para calcular o jacobiano com derivadas parciais)
        """

        # define symbols that will be used
        global symbolsList
        symbolsList = symbols
        
        iterations = 1000
        jacob = functions.jacobian(functionArray)
        lastX = X0

        for i in range(iterations):
            j = functions.changeValuesMatrix(jacob, lastX)
            f = functions.changeValuesArray(functionArray, lastX)

            j_np = np.array(j).astype(np.float64)
            f_np = np.array(f).astype(np.float64)
            
            deltaX = -np.dot(inv(j_np),f_np)
            lastX = lastX + deltaX

            tolk = np.linalg.norm(deltaX, ord=2) / np.linalg.norm(lastX, ord=2)
            if (tolk < tol):
                return lastX

        return "Convergence not reached"


    # @staticmethod 
    # def broyden_equation_solver(F, X0, N_iter, tolerance=0.0001):
        """
        PROGRAMA 4
        Método para achar a solução de um sistema com N equações e N incógnitas
        pelo método de Broyden.

        O método de Broyden é similar ao de Newton. Porém, a matriz jacobiana 
        não é calculada numericamente em cada iteração. Ao invés disso, utiliza-se 
        uma matriz Jacobiana aproximada B.
        
        F = Vetor de funções   
        X0 = vetor solução de partida
        JF = Jacobiano aplicado a F
        (ainda precisa ser definido um método para calcular o jacobiano com derivadas parciais)
        """
        # return

    # # funcs : vetor of functions
    # # X     : vetor of initial values for the funcs params
    # def broydenSystem(X, tol, niter, funcs):
    #     J = functions.jacobianMatrix(funcs, X)
    #     #print 'J: ' + str(J)
    #     B = J
    #     F = [func(X) for func in funcs]
    #     interacoes = 0
    #     for k in range(niter):
    #         deltaX = resolveSystem(B, F)
    #         deltaX = multVectorScalar(deltaX, -1)
    #         X = sumVetors(X, deltaX)
    #         diff = norma(deltaX)/norma(X)
    #         iteracoes += 1
    #         if(diff < tol):
    #             return('Vetor solucao: ' + str(X) + '\nNumero de iteracoes: ' + str(iteracoes)) + '\n'
    #         else:
    #             F2 = [func(X) for func in funcs]
    #             Y = subtractVetors(F2, F)
    #             F = F2

    #             # calculates next B
    #             term1 = subtractVetors(Y, multiMV(B, deltaX))
    #             term2 = multiMM(vector2matrix(term1), transpose(vector2matrix(deltaX)))
    #             term3 = 1/multiMV(transpose(vector2matrix(X)), X)[0]
    #             term4 = multiMS(term2, term3)
    #             B = sumMatrix(B, term4)
    #     print("Convergencia nao atingida.")

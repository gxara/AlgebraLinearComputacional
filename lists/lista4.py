from helpers import Formatter, functions
import math


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
     
        while (abs(b - a) > tolerance):
            xi = abs(a + b) / 2
            fi = function(xi)
            if fi > 0:
                b = xi
            else:
                a = xi
        
        print("A raiz é: {0}".format(xi))
        
        return xi



    @staticmethod 
    def newton(f, x0, N_iter, delta=0.0001, tolerance=0.0001):
        """
        Método para obter a raiz de uma função f
        pelo método de Newton.
        """

        for iter in range(N_iter):
            new_x = x0 - f(x0) / functions.derivada(f, x0)
            tol_iter = abs(new_x - x0)
            if tol_iter < tolerance:
                return x1
            x0 = new_x
        print("Não convergiu")
        return
     



    @staticmethod 
    def newton_secante(f, x0, N_iter, delta=0.0001, tolerance=0.0001):
        """
        Método para obter a raiz de uma função f
        pelo método de Newton-Raphson.
        """
        x1 = x0 + delta

        for iter in range(N_iter):
            f0 = f(x0)
            f1 = f(x1)
            new_x = x1 - f1*(x1-x0) / f1 - f0
            tol_iter = abs(new_x - x1)
            if tol_iter < tolerance:
                return x1
            x0 = x1
            x1 = new_x
        print("Não convergiu")
        return
     

    @staticmethod 
    def interpolacao_inversa(f, pontos,  N_iter, tolerance=0.0001):
        """
        Método para obter a raiz de uma equação f(x) 
        pelo método da interpolacao inversa.
        É necessário conhecer previamente um intervalo [a,b] tal que 
        f(a) < 0 e f(b) > 0  ou f(a) > 0 e f(b) < 0.
        Parâmetros necessários: a, b, e a função f(x)
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
                return new_x

            y = [f1, f2, f3]
            i = y.index(max(y))
            pontos[i] = new_x
            sorted(pontos)
            x0 = new_x
                
        print("Não convergiu")
        return


    @staticmethod 
    def newton_broyden(f, x0, N_iter, delta=0.0001, tolerance=0.0001):
        """
        Método para obter a raiz de uma função f
        pelo método de Newton-Raphson.
        """
        return
     
from helpers import matrices
from lists import Lista3, Lista4
import math
import numpy as np
from sympy import symbols



"""
Utilizanado os programas desenvolvidos encontre as raízes da seguinte equação por todos
os métodos apresentados em sala de aula
"""

def function_test1(x):
    g = 9.806
    k = 0.00341
    s1 = x * (g*k)**(-1/2)
    s2 = math.cosh(s1)
    s3 = math.log(s2)
    s4 = s3 - 50
    return s4


def function_test2(x):
    s1 = 4 * math.cos(x)
    s2  = s1 - math.exp(2*x)
    return s2


#Aplicando todos os métodos conhecidos para calcular a raiz da primeira função:
print("\n****Buscando raízes para a primeira equação****\n")
Lista4.bissecao(function_test1, 0, 100)
Lista4.newton(function_test1, 50, 1000)
Lista4.newton_secante(function_test1, 0.001, 10)
Lista4.interpolacao_inversa(function_test1, [3,4,20], 4000)

print("\n****Buscando raízes para a segunda equação****\n")
#Aplicando todos os métodos conhecidos para calcular a raiz da segunda função:
Lista4.bissecao(function_test2, -10, 10)
Lista4.newton(function_test2, 50, 1000)
Lista4.newton_secante(function_test2, 0.001 , 100)
Lista4.interpolacao_inversa(function_test2, [3,4,5], 4000)






print("\n****Encontrar a solução para as equações abaixo utilizando os métodos de Newton e Broyden****\n")

x,y,z = symbols('x y z')

functionArray1 = np.array([16*(x**4)+16*(y**4)+(z**4)-16, (x**2)+(y**2)+(z**2)-3, (x**3)-y+z-1])
functionArray2 = np.array([x+2*y-2,(x**2)+4*(y**2)-4])

#Aplicando todos os métodos conhecidos para calcular a raiz da segunda função:
Lista4.newton_equation_solver(functionArray1, [1,1,1], 0.0001, [x,y,z])
# multiDimensionalNewtonMethod(functionArray1, [1,1,1], tolerance, [x,y,z])

# Lista4.newton(function_test2, 50, 1000)

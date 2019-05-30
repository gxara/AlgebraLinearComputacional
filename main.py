from helpers import matrices
from lists import Lista4, Lista7
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



print("\n****Encontrar a solução para o sistema de equações abaixo utilizando os métodos de Newton e Broyden****\n")

x,y,z = symbols('x y z')
functionArray = np.array([16*(x**4)+16*(y**4)+(z**4)-16, (x**2)+(y**2)+(z**2)-3, (x**3)-y+z-1])
print("\n{}\n".format(functionArray))

Lista4.newton_equation_solver(functionArray, [1,1,1], 0.0001, [x,y,z])
# Lista4.broyden_equation_solver(functionArray, [1,1,1], 0, 0.0001, [x,y,z])



print("\n****LISTA 7 - Calcular as derivadas por diferença central, passo a frente e passo atrás****\n")

def function_test3(x):
    s1 = x**3
    s2  = 1 / (math.exp(x))
    return s1 + s2

def function_test4(x):
    s1 = x**(1/3)
    s2  = math.log(x)
    return s1 + s2

def function_test5(x):
    s1 = 1
    s2  = math.exp(-((x/5)**2))
    return s1 - s2

d1 = Lista7.diferenca_central(function_test3, 3)
d2 = Lista7.step_forward(function_test3, 3)
d3 = Lista7.step_back(function_test3, 3)
print("a) Resultado da derivada por diferença central: {}".format(d1))
print("a) Resultado da derivada por passo à frente: {}".format(d2))
print("a) Resultado da derivada por passo atrás: {}".format(d3))

d4 = Lista7.diferenca_central(function_test4, 2)
d5 = Lista7.step_forward(function_test4, 2)
d6 = Lista7.step_back(function_test4, 2)

print("\n")
print("b) Resultado da derivada por diferença central: {}".format(d4))
print("b) Resultado da derivada por passo à frente: {}".format(d5))
print("b) Resultado da derivada por passo atrás: {}".format(d6))

d7 = Lista7.diferenca_central(function_test5, 6)
d8 = Lista7.step_forward(function_test5, 6)
d9 = Lista7.step_back(function_test5, 6)

print("\n")
print("c) Resultado da derivada por diferença central: {}".format(d7))
print("c) Resultado da derivada por passo à frente: {}".format(d8))
print("c) Resultado da derivada por passo atrás: {}".format(d9))
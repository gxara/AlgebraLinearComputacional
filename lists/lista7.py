from helpers import Formatter, functions
import math
import numpy as np  
from numpy import linalg  


class Lista7:
    def __init__(self):
        pass

    @staticmethod
    def original_function(x):
        y = x**2 - 4*math.cos(x)
        return y


    @staticmethod
    def diferenca_central(function, x0, delta=0.0001):
        """
        Método para cálculo numérico da derivada de uma função por meio da diferença central
        """

        derivada = (function(x0+delta) - function(x0-delta)) / 2*delta
        
        return derivada



    @staticmethod
    def step_forward(function, x0, delta=0.0001):
        """
        Método para cálculo numérico da derivada de uma função por meio do passo à frente
        """

        derivada = (function(x0+delta) - function(x0)) / delta
        
        return derivada



    @staticmethod
    def step_back(function, x0, delta=0.0001):
        """
        Método para cálculo numérico da derivada de uma função por meio do passo atrás
        """

        derivada = (function(x0) - function(x0 - delta)) / delta
        
        return derivada

    @staticmethod
    def richardson_extrapolation():
        return



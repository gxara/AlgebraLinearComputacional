import sys
from .operations import *
import numpy as np

def leastSquareMethod(X,Y):
    # Retorna os parâmetros a e b de uma reta, a partir de N pares de pontos fornecidos pelo usuário
    P = []
    for i in range(len(X)):
        P.append([1.0,X[i][0]])
    
    PTranspose = transpose(P)
    A = multiply_matrices(PTranspose,P)
    C = multiply_matrices(PTranspose,Y)
    B = multiply_matrices(np.linalg.inv(np.array(A)),C)

    return B

from helpers import operations

# Interpolação é encontrar uma função cuja curva passe exatamente sobre todos os pontos de um conjunto de pontos observados.
# O objetivo aqui é, dados os pontos de x e y, encontrar os coeficientes que fazem o melhor ajuste da curva.

# Exercício 1 - Interpolação polinomial:
x = [1,2,3]
y = [1,2,9]


p = operations.create_vandermonde_matrix(x)
pT = operations.transpose(p)
pTp = operations.multiply(pT,p)

print(pTp)


# vetor_x = [[1, 2, 3]]
# vetor_y = [[1], [2], [3]]
# vetor_coeficientes = [b1, b2, b3]

# matriz_vandermonde = [\
# [1, x1, pow(x1, 2)], 
# [1, x2, pow(x2, 2)], 
# [1, x3, pow(x3, 2)]]

# result = str(matriz_vandermonde).replace('],', ']\n').replace(']]', ']').replace('[[',' [')
# print(result)

# transposed_result = operations.transpose(matriz_vandermonde)
# result = str(transposed_result).replace('],', ']\n').replace(']]', ']').replace('[[',' [')
# print(result)

# multiplied_result = operations.multiply(operations.transpose(matriz_vandermonde), vetor_y)
# result = str(multiplied_result).replace('],', ']\n').replace(']]', ']').replace('[[',' [')
# print(result)


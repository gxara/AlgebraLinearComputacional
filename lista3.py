from helpers import operations

# Interpolação é encontrar uma função cuja curva passe exatamente sobre todos os pontos de um conjunto de pontos observados.
# O objetivo aqui é, dados os pontos de x e y, encontrar os coeficientes que fazem o melhor ajuste da curva.

# Exercício 1 - Interpolação polinomial:
x = [[1],[2],[3]]
y = [[1],[2],[9]]

p = operations.create_vandermonde_matrix(x)
pT = operations.transpose(p)
pTp = operations.multiply(pT,p)
reverse_pTp = operations.getMatrixInverse(pTp)
a = operations.multiply(reverse_pTp , pT)
coeficientes = operations.multiply(a, y)
print(coeficientes)

# Exercício 2 - Interpolação polinomial:

x = [[1],[2],[3],[4]]
y = [[1],[2],[9],[20]]

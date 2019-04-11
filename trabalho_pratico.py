from helpers import operations, Formatter


# QUESTÃO 1

print('\n*** Contiuação da questão 1 ***\n')
print('\n Cálculo do determinante...\n')


A = [[19 , 5 , 3 , 1 , 2 , 1],
     [ 5,  20,  5,  3, 1 , 2],\
     [ 3,   5, 19,  5,  1, 2],\
     [ 1,   3,  5, 16,  1, 2],\
     [ 2,   1,  1,  1, 15, 3],\
     [ 1,   2,  2,  2,  3, 14]]

beta = 0.15

A_times_beta = operations.multiply_matrix_by_constant(A, beta)
d = operations.get_determinant(A_times_beta)

print('determinante de A = {}'.format(d))



# QUESTÃO 2


print('\n*** Questão 2 ***\n')
# Dado o seguinte conjunto de pontos:
x = [-2.7 , -1 , 0 , 1 , 1.6 , 3.1]
y_divided_by_beta = [3.0 , 4.6 , 6.0 , 7.5 , 8.5 , 9.5]
beta = 0.53

# Ajuste uma reta y = a*x + b

# Para resolver, vamos utilizar a regressão linear
# AB = C
# B = A**(-1) * C

y = operations.multiply_array_by_constant(y_divided_by_beta, beta)

A = [[len(x), sum(x)], [sum(x),sum(element**2 for element in x)]]
C = operations.get_vector_C(x,y)

# Precisamos determinar o vetor B com os coeficientes que melhor se ajustam ao conjunto de pontos:
# B = A**(-1) * C

inverseA = operations.getMatrixInverse(A) 
B = operations.multiply_matrices(inverseA, C)

print('Vetor de coeficientes:\n')
Formatter.print_matrix(B)

print('\n Equação da reta:\n')
Formatter.print_equation(B)



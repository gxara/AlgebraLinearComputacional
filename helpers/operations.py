import sys

def transpose(original_matrix):
    n_rows = len(original_matrix)
    n_columns = len(original_matrix[0])
    
    transposed_matrix = []
    
    # Given a matrix of n x m dimensions, creates a null matrix with m x n dimensions
    for column in range(n_columns):
        transposed_matrix.append([])
        for row in range(n_rows):
            transposed_matrix[column].append(0)
    
    # Fills the new empty transposed matrix
    for i in range(n_rows):
        for j in range(n_columns):
            transposed_matrix[j][i] = original_matrix[i][j]
    
    return transposed_matrix


def multiply(matrix1, matrix2):
    matrix1_n_rows = len(matrix1)
    matrix1_n_columns = len(matrix1[0])
    
    matrix2_n_rows = len(matrix2)
    matrix2_n_columns = len(matrix2[0])
    
    if matrix1_n_columns != matrix2_n_rows:
        print("{} vs {}".format(matrix1_n_columns, matrix2_n_columns))
        print("As matrizes não são compatíveis para multiplicação!\n")
        sys.exit()

    result_matrix = []
    
    # Creates a null matrix with the resultant dimensions
    for column in range(matrix1_n_rows):
        result_matrix.append([])
        for row in range(matrix2_n_columns):
            result_matrix[column].append(0)

    # Multiply    
    for i in range(matrix1_n_rows):
        for k in range(matrix2_n_columns):
            for j in range(matrix2_n_rows):
            
                result_matrix[i][k] += matrix1[i][j] * matrix2[j][k]
    
    return result_matrix
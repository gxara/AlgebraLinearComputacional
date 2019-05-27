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


def multiply_matrices(matrix1, matrix2):
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

    # multiply_matrices    
    for i in range(matrix1_n_rows):
        for k in range(matrix2_n_columns):
            for j in range(matrix2_n_rows):
            
                result_matrix[i][k] += round(matrix1[i][j] * matrix2[j][k] , 4)
    
    return result_matrix


def create_vandermonde_matrix(vector_x):
    vector_x
    vandermonde_matrix = []
    pow = len(vector_x) -1
    for element in vector_x:
        vandermonde_matrix.append([])
        for index in range(pow+1):
            vandermonde_matrix[-1].append(element[0]**index)
    return vandermonde_matrix



def get_determinant(matrix):
    
    determinant=0
    
    # Calculate determinant with LaPlace method

    indices = list(range(len(matrix)))
     
    if len(matrix) == 2 and len(matrix[0]) == 2:
        determinant = round((matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1]), 4)
        return determinant
 
    for fc in indices:
        As = matrix.copy() 
        As.pop(0)
        
        height = len(As)
 
        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        signal = (-1) ** (fc % 2)
        sub_det = get_determinant(As)
        determinant += round(signal * matrix[0][fc] * sub_det, 4)
 
    return determinant


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixInverse(m):
    determinant = get_determinant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[round(m[1][1]/determinant,4), round(-1*m[0][1]/determinant,4)], [round(-1*m[1][0]/determinant,4), round(m[0][0]/determinant,4)]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(   round(((-1)**(r+c)) * get_determinant(minor), 4)   )
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors



# Vector C of a linear regression
def get_vector_C(X, Y):
    C = [[0],[0]]
    for index in range(len(Y)):
        C[0][0] += Y[index]
        C[1][0] += Y[index] * X[index]
    
    return C


def multiply_array_by_constant(array, constant):
    new_array = []
    for element in array:
        index = array.index(element)
        new_array.append(constant * array[index])

    return new_array


def multiply_matrix_by_constant(matrix, constant):
    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([])
        for column in range(len(matrix[0])):
            new_matrix[row].append([])
            new_matrix[row][column] = matrix[row][column] * constant

    return new_matrix




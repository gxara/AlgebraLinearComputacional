from copy import deepcopy
from sympy import symbols, diff

symbolsList = []


def derivada(funcao, x, delta = 10**(-10)):
    """
    Retorna a derivada de uma funcao no ponto x.    
    """
    return (funcao( x + delta ) - funcao(x)) / delta


def derivadaParcial(func, X, xIndex):
    dx = 1**-10
    y1 = func(X)
    X[xIndex] += dx
    y2 = func(X)
    X[xIndex] -= dx 
    return (y2 - y1)/dx


# creates matrix with m rows, n columns filled with value
def createMatrix(m,n,value):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(value)
    return matrix


def jacobian(funcArray):
	global symbolsList
	functionArray = deepcopy(funcArray)
	jacobian = []
	for i in range(functionArray.size):
		temp = []
		for j in range(len(symbolsList)):
			temp.append(diff(functionArray[i], symbolsList[j]))
		jacobian.append(temp)
	return jacobian


def jacobianBroyden(funcArray):
	global symbolsList
	functionArray = deepcopy(funcArray)
	jacobian = []
	functionList = functionArray.tolist()
    
	for i in range(len(functionArray)):
		temp = []
		for j in range(len(symbolsList)):
			temp.append(diff(functionList[i][0], symbolsList[j]))
		jacobian.append(temp)
	return jacobian


def changeValuesMatrix(matrix, valueArray):
	global symbolsList
	functionMatrix = deepcopy(matrix)
	for i in range(len(functionMatrix)):
		for j in range(len(functionMatrix[i])):
			for k in range(len(symbolsList)):
				functionMatrix[i][j] = functionMatrix[i][j].subs(symbolsList[k], valueArray[k])
	return functionMatrix


def changeValuesArray(array, valueArray):
	global symbolsList
	functionArray = deepcopy(array)
	for i in range(len(functionArray)):
		for k in range(len(symbolsList)):
				functionArray[i] = functionArray[i].subs(symbolsList[k], valueArray[k])
	return functionArray


def changeValuesArrayBroyden(array, valueArray):
	global symbolsList
	functionArray = deepcopy(array)
	for i in range(len(functionArray)):
		for j in range(len(functionArray[i])):
			for k in range(len(symbolsList)):
				functionArray[i][j] = functionArray[i][j].subs(symbolsList[k], valueArray[k])
	return functionArray
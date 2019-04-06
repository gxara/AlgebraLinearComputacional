import sys

class Formatter():



    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print('|', end='')
            for element in row:
                formatted_element = str(element)[:6]
                while len(formatted_element) != 6:
                    formatted_element = formatted_element + '0'
                print(formatted_element, end='')
            print('|')

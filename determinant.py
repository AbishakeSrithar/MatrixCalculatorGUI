import PyQt5.QtWidgets as qtw
import numpy as np
import copy


def get_square_dimensions(qwidget):
    items = ("1x1","2x2","3x3","4x4","5x5","6x6","7x7","8x8","9x9")
    item, okPressed = qtw.QInputDialog.getItem(qwidget, "Matrix Dimensions","Please select one of the following options", items, 0, False)
    if okPressed and item:
        # n x n dimensions
        n = int(item[0])

    return n


def get_matrix(qwidget, n):
    text, okPressed = qtw.QInputDialog.getText(qwidget, "Get CSV","Type values seperated by ','s", qtw.QLineEdit.Normal, "")
    if okPressed and text != '':
        temp = text.split(",")
        matrix1_values = []
        for value in temp:
            matrix1_values.append(int(value))
    if n ** 2 == len(matrix1_values):
        matrix = np.zeros((n, n))
        count = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix1_values[count]
                count += 1
        list_matrix = np.array(matrix).tolist()
        ans = calculate_determinant(qwidget, list_matrix, n)
        return ans

def calculate_determinant(qwidget, matrix, n):
    my_sum = 0
    # Corner case.
    if n == 1:
        return matrix[0][0]
    # Base case.
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Recursion
    for i in range(n):
        new_matrix = copy.deepcopy(matrix)
        new_matrix.pop(0)
        for j in range(n - 1):
            new_matrix[j].pop(i)
        my_sum += matrix[0][i] * ((-1) ** i) * qwidget.calculate_determinant(new_matrix, n - 1)
    return my_sum


import PyQt5.QtWidgets as qtw
import numpy as np
import copy
import get_input as gi


def multiplication(qwidget):
    n1, n2, matrix1_values = gi.get_matrix(qwidget)
    if matrix1_values:
        matrix = np.zeros((n1, n2))
        list_matrix = np.array(matrix).tolist()
        count = 0
        for i in range(n1):
            for j in range(n2):
                list_matrix[i][j] = matrix1_values[count]
                count += 1
        matrix1_values = []
    else:
        return False

    n1, n2, matrix1_values = gi.get_matrix(qwidget)
    if matrix1_values:
        matrix = np.zeros((n1, n2))
        list_matrix2 = np.array(matrix).tolist()
        count = 0
        for i in range(n1):
            for j in range(n2):
                list_matrix2[i][j] = matrix1_values[count]
                count += 1
        matrix1_values = []
    else:
        return False

    answer = np.matmul(list_matrix, list_matrix2).tolist()

    return answer
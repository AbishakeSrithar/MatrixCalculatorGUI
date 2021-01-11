import PyQt5.QtWidgets as qtw
import numpy as np
import copy
import get_input as gi


def transpose(qwidget):
    n1, n2, matrix1_values = gi.get_matrix(qwidget)
    if matrix1_values:
        matrix = np.zeros((n2, n1))
        count = 0
        for i in range(n1):
            for j in range(n2):
                matrix[j][i] = matrix1_values[count]
                count += 1
        list_matrix = np.array(matrix).tolist()
        return list_matrix
    else:
        return "Error"
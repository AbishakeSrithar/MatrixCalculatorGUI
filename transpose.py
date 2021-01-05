import PyQt5.QtWidgets as qtw
import numpy as np
import copy

def get_dimensions(qwidget):
    text, okPressed = qtw.QInputDialog.getText(qwidget, "Get dimensions","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
    if okPressed and text != '':
        temp = text.split(",")
        return int(temp[0]), int(temp[1])

def transpose(qwidget):
    n1, n2 = get_dimensions(qwidget)
    
    text, okPressed = qtw.QInputDialog.getText(qwidget, "Get CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
    if okPressed and text != '':
        temp = text.split(",")
        matrix1_values = []
        for value in temp:
            matrix1_values.append(int(value))
    if n1 * n2 == len(matrix1_values):
        matrix = np.zeros((n2, n1))
        count = 0
        for i in range(n1):
            for j in range(n2):
                matrix[j][i] = matrix1_values[count]
                count += 1
        print(matrix)
        list_matrix = np.array(matrix).tolist()
        return list_matrix
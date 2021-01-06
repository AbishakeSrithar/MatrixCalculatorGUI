import PyQt5.QtWidgets as qtw


def get_dimensions(qwidget):
    text, okPressed = qtw.QInputDialog.getText(qwidget, "Dimensions","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
    if okPressed and text != '':
        temp = text.split(",")
        return int(temp[0]), int(temp[1])


def get_matrix(qwidget):
    n1, n2 = get_dimensions(qwidget)

    text, okPressed = qtw.QInputDialog.getText(qwidget, "Elements CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
    if okPressed and text != '':
        temp = text.split(",")
        matrix1_values = list(map(int, temp))
    if n1 * n2 == len(matrix1_values):
        return n1, n2, matrix1_values
    else:
        return False
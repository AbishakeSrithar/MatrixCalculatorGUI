import PyQt5.QtWidgets as qtw


def get_dimensions(qwidget):
    text, okPressed = qtw.QInputDialog.getText(qwidget, "Dimensions","Input m, n", qtw.QLineEdit.Normal, "")
    if okPressed and text != '':
        temp = text.split(",")
        try:
            return int(temp[0]), int(temp[1])
        except:
            return 0, 0


def get_matrix(qwidget):
    n1, n2 = get_dimensions(qwidget)

    text, okPressed = qtw.QInputDialog.getText(qwidget, "Elements","Input a, b, c,...", qtw.QLineEdit.Normal, "")
    if okPressed and text != '':
        temp = text.split(",")
        try:
            matrix1_values = list(map(int, temp))
        except:
            return 0, 0, False
    if n1 * n2 == len(matrix1_values):
        return n1, n2, matrix1_values
    else:
        return 0, 0, False
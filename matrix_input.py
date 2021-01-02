import PyQt5.QtWidgets as qtw


def get_square_dimensions(qwidget):
    items = ("1x1","2x2","3x3","4x4","5x5","6x6","7x7","8x8","9x9")
    item, okPressed = qtw.QInputDialog.getItem(qwidget, "Matrix Dimensions","Matrix Dimensions", items, 0, False)
    if okPressed and item:
        # n x n dimensions
        n = int(item[0])

    return n


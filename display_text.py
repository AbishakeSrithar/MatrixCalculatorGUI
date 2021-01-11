import PyQt5.QtWidgets as qtw

def display_text(qwidget, ans, function):
    answer_box = qtw.QMessageBox()
    answer_box.setIcon(qtw.QMessageBox.Information)
    answer_box.setText(str(ans))
    answer_box.setGeometry(300, 100, 300, 100)
    answer_box.setWindowTitle(function)
    answer_box.setStandardButtons(qtw.QMessageBox.Ok)

    answer_box.exec()
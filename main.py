# Matric Calculator
# Step 1: Make a working application ✔
# Step 2: Modularise, maybe seperate files too
# Step 3: Check for clean inputs
# Step 4: Testing Framework/ Error catching

import PyQt5.QtWidgets as qtw
import numpy as np
import copy
import determinant as det
import addition as add
import multiplication as mult
import transpose as tran

class MainWindow(qtw.QWidget):
    """ Calculator """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix Calculator")
        self.setGeometry(300, 100, 300, 100)
        # Window with Box Layout
        self.setLayout(qtw.QVBoxLayout())
        self.interface()
        self.dimensions = []
        self.matrix1_values = []
        self.show()


    def interface(self):
        # Container with Grid Layout
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Buttons
        btn_determinant = qtw.QPushButton("Determinant", clicked=self.determinant)
        btn_addition = qtw.QPushButton("Addition", clicked=self.addition)
        btn_multiplication = qtw.QPushButton("Multiplication", clicked=self.multiplication)
        btn_transpose = qtw.QPushButton("Transpose", clicked=self.transpose)

        # Adding Buttons to Grid
        container.layout().addWidget(btn_determinant,5,0,4,4)
        container.layout().addWidget(btn_addition,10,0,4,4)
        container.layout().addWidget(btn_multiplication,5,5,4,4)
        container.layout().addWidget(btn_transpose,10,5,4,4)
        self.layout().addWidget(container)

    
    def determinant(self):
        ans = det.get_det(self)
        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(ans))
        answer_box.setGeometry(300, 100, 300, 100)
        answer_box.setWindowTitle("Determinant")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()

    
    def addition(self):
        ans = add.addition(self)
        
        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(ans))
        answer_box.setWindowTitle("Determinant")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()


    def multiplication(self):

        ans = mult.multiplication(self)
        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(ans))
        answer_box.setWindowTitle("Multiplication")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()


    def transpose(self):
        ans = tran.transpose(self)
        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(ans))
        answer_box.setWindowTitle("Transpose")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
while True:
    app.exec_()
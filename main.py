# Matric Calculator
# Step 1: Make a working application ✔
# Step 2: Modularise, maybe seperate files too
# Step 3: Check for clean inputs
# Step 4: Testing Framework?

import PyQt5.QtWidgets as qtw
import numpy as np
import copy
import determinant as det
import addition as add

class MainWindow(qtw.QWidget):
    """ Calculator """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix Calculator")

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
        container.layout().addWidget(btn_determinant,0,0,2,2)
        container.layout().addWidget(btn_addition,3,0,2,2)
        container.layout().addWidget(btn_multiplication,0,5,2,2)
        container.layout().addWidget(btn_transpose,3,5,2,2)
        self.layout().addWidget(container)

    
    def determinant(self):
        n = det.get_square_dimensions(self)
        # items = ("1x1","2x2","3x3","4x4","5x5","6x6","7x7","8x8","9x9")
        # item, okPressed = qtw.QInputDialog.getItem(self, "Matrix Dimensions","Matrix Dimensions", items, 0, False)
        # if okPressed and item:
        #     # n x n dimensions
        #     n = int(item[0])
        ans = det.get_matrix(self, n)
        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(ans))
        answer_box.setWindowTitle("Determinant")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()

    
    # def input(self, n):
    #     text, okPressed = qtw.QInputDialog.getText(self, "Get CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
    #     if okPressed and text != '':
    #         temp = text.split(",")
    #         for value in temp:
    #             self.matrix1_values.append(int(value))
    #     if n ** 2 == len(self.matrix1_values):
    #         matrix = np.zeros((n, n))
    #         count = 0
    #         for i in range(n):
    #             for j in range(n):
    #                 matrix[i][j] = self.matrix1_values[count]
    #                 count += 1
    #         print(matrix)
    #         list_matrix = np.array(matrix).tolist()
    #         ans = self.det(list_matrix, n)
    #         print(ans)
    #         return ans


    # def det(self, matrix, n):
    #     my_sum = 0
    #     # Corner case.
    #     if n == 1:
    #         return matrix[0][0]
    #     # Base case.
    #     if n == 2:
    #         return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    #     # Recursion
    #     for i in range(n):
    #         new_matrix = copy.deepcopy(matrix)
    #         new_matrix.pop(0)
    #         for j in range(n - 1):
    #             new_matrix[j].pop(i)
    #         my_sum += matrix[0][i] * ((-1) ** i) * self.det(new_matrix, n - 1)
    #     return my_sum

    
    def addition(self):
        list_matrix2 = add.addition(self)
        # items = ("1","2","3","4","5","6","7","8","9")
        # item, okPressed = qtw.QInputDialog.getItem(self, "Matrix Dimension 1","Matrix Dimension 1", items, 0, False)
        # if okPressed and item:
        #     # n x n dimensions
        #     n = int(item[0])

        # items2 = ("1","2","3","4","5","6","7","8","9")
        # item2, okPressed2 = qtw.QInputDialog.getItem(self, "Matrix Dimension 2","Matrix Dimension 2", items, 0, False)
        # if okPressed2 and item2:
        #     # n x n dimensions
        #     n2 = int(item2[0])

        # text, okPressed = qtw.QInputDialog.getText(self, "Get CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
        # if okPressed and text != '':
        #     temp = text.split(",")
        #     for value in temp:
        #         self.matrix1_values.append(int(value))
        # if n * n2 == len(self.matrix1_values):
        #     matrix = np.zeros((n, n2))
        #     list_matrix = np.array(matrix).tolist()
        #     count = 0
        #     for i in range(n):
        #         for j in range(n):
        #             list_matrix[i][j] = self.matrix1_values[count]
        #             count += 1
        #     self.matrix1_values = []
        # else:
        #     return

        # items = ("1","2","3","4","5","6","7","8","9")
        # item, okPressed = qtw.QInputDialog.getItem(self, "Matrix Dimension 1","Matrix Dimension 1", items, 0, False)
        # if okPressed and item:
        #     # n x n dimensions
        #     n = int(item[0])

        # items2 = ("1","2","3","4","5","6","7","8","9")
        # item2, okPressed2 = qtw.QInputDialog.getItem(self, "Matrix Dimension 2","Matrix Dimension 2", items, 0, False)
        # if okPressed2 and item2:
        #     # n x n dimensions
        #     n2 = int(item2[0])

        # text, okPressed = qtw.QInputDialog.getText(self, "Get CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
        # if okPressed and text != '':
        #     temp = text.split(",")
        #     for value in temp:
        #         self.matrix1_values.append(int(value))
        # if n * n2 == len(self.matrix1_values):
        #     matrix = np.zeros((n, n2))
        #     list_matrix2 = np.array(matrix).tolist()
        #     count = 0
        #     for i in range(n):
        #         for j in range(n):
        #             list_matrix2[i][j] = self.matrix1_values[count] + list_matrix[i][j]
        #             count += 1
        #     self.matrix1_values = []
        
        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(list_matrix2))
        answer_box.setWindowTitle("Determinant")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()

    def multiplication(self):
        items = ("1","2","3","4","5","6","7","8","9")
        item, okPressed = qtw.QInputDialog.getItem(self, "Matrix Dimension 1","Matrix Dimension 1", items, 0, False)
        if okPressed and item:
            # n x n dimensions
            n = int(item[0])

        item2, okPressed2 = qtw.QInputDialog.getItem(self, "Matrix Dimension 2","Matrix Dimension 2", items, 0, False)
        if okPressed2 and item2:
            # n x n dimensions
            n2 = int(item2[0])

        text, okPressed = qtw.QInputDialog.getText(self, "Get CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
        if okPressed and text != '':
            temp = text.split(",")
            for value in temp:
                self.matrix1_values.append(int(value))
        if n * n2 == len(self.matrix1_values):
            matrix = np.zeros((n, n2))
            list_matrix = np.array(matrix).tolist()
            count = 0
            for i in range(n):
                for j in range(n):
                    list_matrix[i][j] = self.matrix1_values[count]
                    count += 1
            self.matrix1_values = []
        else:
            return 

        items = ("1","2","3","4","5","6","7","8","9")
        item, okPressed = qtw.QInputDialog.getItem(self, "Matrix Dimension 1","Matrix Dimension 1", items, 0, False)
        if okPressed and item:
            # n x n dimensions
            n = int(item[0])

        items2 = ("1","2","3","4","5","6","7","8","9")
        item2, okPressed2 = qtw.QInputDialog.getItem(self, "Matrix Dimension 2","Matrix Dimension 2", items, 0, False)
        if okPressed2 and item2:
            # n x n dimensions
            n2 = int(item2[0])

        text, okPressed = qtw.QInputDialog.getText(self, "Get CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
        if okPressed and text != '':
            temp = text.split(",")
            for value in temp:
                self.matrix1_values.append(int(value))
        if n * n2 == len(self.matrix1_values):
            matrix = np.zeros((n, n2))
            list_matrix2 = np.array(matrix).tolist()
            count = 0
            for i in range(n):
                for j in range(n):
                    list_matrix2[i][j] = self.matrix1_values[count]
                    count += 1
            self.matrix1_values = []
        else:
            return 

        answer = np.matmul(list_matrix, list_matrix2).tolist()

        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(answer))
        answer_box.setWindowTitle("Multiplication")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()


    def transpose(self):
        items = ("1","2","3","4","5","6","7","8","9")
        item, okPressed = qtw.QInputDialog.getItem(self, "Matrix Dimension 1","Matrix Dimension 1", items, 0, False)
        if okPressed and item:
            n = int(item[0])

        items2 = ("1","2","3","4","5","6","7","8","9")
        item2, okPressed2 = qtw.QInputDialog.getItem(self, "Matrix Dimension 2","Matrix Dimension 2", items, 0, False)
        if okPressed2 and item2:
            n2 = int(item2[0])

        text, okPressed = qtw.QInputDialog.getText(self, "Get CSV","Input (seperate values by ',')", qtw.QLineEdit.Normal, "")
        if okPressed and text != '':
            temp = text.split(",")
            for value in temp:
                self.matrix1_values.append(int(value))
        if n * n2 == len(self.matrix1_values):
            matrix = np.zeros((n, n))
            count = 0
            for i in range(n):
                for j in range(n):
                    matrix[j][i] = self.matrix1_values[count]
                    count += 1
            print(matrix)
            list_matrix = np.array(matrix).tolist()
            ans = self.det(list_matrix, n)
            print(ans)

        answer_box = qtw.QMessageBox()
        answer_box.setIcon(qtw.QMessageBox.Information)
        answer_box.setText(str(list_matrix))
        answer_box.setWindowTitle("Transpose")
        answer_box.setStandardButtons(qtw.QMessageBox.Ok)

        return answer_box.exec()


                    
        


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
app.exec_()
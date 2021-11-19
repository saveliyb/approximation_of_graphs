import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QListWidget
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from func import *
import numpy as np
import matplotlib.pyplot as plt
from sqlFunc import *


class history(QListWidget):
    """widget class for displaying the history list"""

    def __init__(self):
        super(history, self).__init__()
        self.setGeometry(1000, 100, 500, 300)
        self.setWindowTitle("Stored")
        self.update_Widget()

    def format_history(self):
        """this function converts the history into a format for output"""
        for _ in list(read_Sql()):
            data = [i for i in json.loads(_[2]) if i]
            data_x = [i for i in json.loads(_[3]) if i]
            try:
                lenght_name = len(_[1] + "   :   ")

                string_ans = _[1] + "   :   " + "x" + "\u00B2 "
                string_ans += plus_or_minus(str(data[0][1])) + str(
                    abs(float(data[0][1]))
                )
                string_ans += " x "
                string_ans += plus_or_minus(str(data[0][2])) + str(
                    abs(float(data[0][2]))
                )
                string_ans += " = y"
                string_ans += "\t"
                string_ans += "x \u2208 " + f"{data_x[0][0]}; {data_x[0][1]}"
                self.addItem(string_ans)
                k = 1  # counter for the cycle
                for j in data[1:]:
                    string_ans = (
                        "".join([" " for k in range(lenght_name)])
                        + "      x"
                        + "\u00B2 "
                    )
                    string_ans += plus_or_minus(str(j[1])) + str(abs(float(j[1])))
                    string_ans += " x "
                    string_ans += plus_or_minus(str(j[2])) + str(abs(float(j[2])))
                    string_ans += " = y"
                    string_ans += "\t"
                    string_ans += "x \u2208 " + f"{data_x[k][0]}; {data_x[k][1]}"
                    self.addItem(string_ans)
                    k += 1
            except:
                pass

            finally:
                self.addItem("")
        self.verticalScrollBar()

    def update_Widget(self):
        self.clear()
        self.format_history()
        self.update()


class coefficients_list(QListWidget):
    """widget class for displaying a list of the equations obtained from the drawing"""

    def __init__(self, coefficients, x_belong):
        super(coefficients_list, self).__init__()
        self.x_belong = x_belong
        self.multiplier = [i for i in coefficients if i != None]
        self.setWindowTitle("coefficients")
        self.setGeometry(1510, 100, 400, 100)
        self.format_coefficients()

    def format_coefficients(self):
        """this function converts the coefficients into a format for output"""
        for i in range(len(self.multiplier)):
            string_ans = roman(i + 1) + "   :   " + "x" + "\u00B2 "
            string_ans += plus_or_minus(str(self.multiplier[i][1])) + str(
                abs(float(self.multiplier[i][1]))
            )
            string_ans += " x "
            string_ans += plus_or_minus(str(self.multiplier[i][2])) + str(
                abs(float(self.multiplier[i][2]))
            )
            string_ans += " = y"
            string_ans += "\t"
            string_ans += "x \u2208 " + f"{self.x_belong[i][0]}; {self.x_belong[i][1]}"
            self.addItem(string_ans)


class Window(QMainWindow):
    """the class of the main widget of the program"""

    def __init__(self):
        super().__init__()
        create_table_sql()
        self.x_belongs = []
        self.coefficients = []
        self.setWindowTitle("Paint")

        self.setGeometry(100, 100, 800, 600)

        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 5
        self.BruchColor = Qt.black

        self.lastPoint = QPoint()
        self.clear()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("menu")
        undo = mainMenu.addAction("undo")
        undo.triggered.connect(self.undo)
        clear = QAction("clear", self)
        fileMenu.addAction(clear)
        clear.triggered.connect(self.clear)
        save = QAction("save", self)
        fileMenu.addAction(save)
        save.triggered.connect(self.save)
        stored_show = QAction("stored", self)
        fileMenu.addAction(stored_show)
        stored_show.triggered.connect(self.stored_show)
        Action = QAction("approksimacia", self)
        fileMenu.addAction(Action)
        Action.triggered.connect(self.appr)
        Action.triggered.connect(self.def_coefficientslisting_show)

    def mousePressEvent(self, event):
        """a function that tracks mouse clicks"""
        if event.button() == Qt.LeftButton:
            self.drawing = True

            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        """function that tracks mouse movement"""
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)

            painter.setPen(QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            painter.drawLine(self.lastPoint, event.pos())

            self.lastPoint = event.pos()

            self.update()
            self.lst.append((event.pos().x(), event.pos().y()))

    def mouseReleaseEvent(self, event):
        """function that tracks the raising of the left mouse button"""
        if event.button() == Qt.LeftButton:

            self.drawing = False
            self.answer_lst.append([_ for _ in self.lst])
            self.lst.clear()

    def paintEvent(self, event):
        """the function displays a pen drawing on the canvas"""
        canvasPainter = QPainter(self)

        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def clear(self):
        """function that cleans the canvas"""
        self.image.fill(Qt.white)
        self.lst = []
        self.answer_lst = []
        self.update()

    def undo(self):
        """function cancels the last drawn element"""
        try:
            points = self.answer_lst[-1]
            self.answer_lst = self.answer_lst[:-1]
            for i in points:
                painter = QPainter(self.image)
                painter.setPen(
                    QPen(Qt.white, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                )
                for point in range(-1, 2):
                    painter.drawPoint(i[0] + point, i[1])
                    painter.drawPoint(i[0] + point, i[1])
                    painter.drawPoint(i[0] + point, i[1])
                self.update()
        except IndexError:
            pass

    def def_coefficientslisting_show(self):
        """the function displays the parabola equations of the drawing"""
        self.coefficientslisting = coefficients_list(self.coefficients, self.x_belongs)
        self.coefficientslisting.show()

    def stored_show(self):
        """the function displays the history of saved equations"""
        self.widget_history = history()
        self.widget_history.show()

    def save(self):
        """saves the image and parabola equations to the database"""
        if self.coefficients:
            filePath, _ = QFileDialog.getSaveFileName(
                self,
                "Save Image",
                "",
                "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ",
            )
            name = filePath.split("/")[-1].split(".")[0]
            write_sql(name, self.coefficients, self.x_belongs)
            if filePath == "":
                return
            self.image.save(filePath)
            try:
                self.widget_history.update_Widget()
            except:
                pass
        else:
            self.appr()
            self.def_coefficientslisting_show()
            self.save()

    def appr(self):
        """a function for calling the approximation function and passing the necessary arguments to it"""
        lst = []

        for i in range(len(self.answer_lst)):
            a = set_list_x_y([set_many_list(self.answer_lst[i])])
            [self.x_belongs.append(_) for _ in a[-1]]
            a = a[:2]
            for _ in range(len(a[0])):
                lst.append(self.mnkGP(np.asarray(a[0][_]), np.asarray(a[1][_])))
        self.coefficients = [_ for _ in lst]

    def make_poly(self, x, coefs):
        """generate a polynomial from an array of coefficients"""
        f = np.zeros(len(x))
        for i in range(len(coefs)):
            f = f + coefs[-1 - i] * x ** i
        return f

    def func(self, xx, yy):

        fit_result = np.polyfit(x=xx, y=yy, deg=2, full=True)
        newX = np.linspace(1420, 1460, 100)
        plt.scatter(xx, yy)
        plt.plot(newX, self.make_poly(newX, fit_result[0]), "g", linewidth=0.5)
        plt.show()

    def mnkGP(self, x, y):
        """approximation function"""
        if x != []:
            d = 2  # '''displays the points taken for approximation'''
            fp, residuals, rank, sv, rcond = np.polyfit(x, y, d, full=True)
            f = np.poly1d(fp)
            coefficients = [round(fp[0], 4), round(fp[1], 4), round(fp[2], 4)]

            """displays the points taken for approximation"""
            # print(f'x принадежит от {min(x)}, до {max(x)}')

            fx = np.linspace(x[0], x[-1] + 1, len(x))
            plt.plot(x, y, "o", label="Original data", markersize=10)
            plt.plot(fx, f(fx), linewidth=2)
            plt.grid(True)
            plt.show()

            return coefficients


App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing the window
window.show()

# start the app
sys.exit(App.exec())

# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from maint import set_many_list, set_list_x_y
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint")

        self.setGeometry(100, 100, 800, 600)

        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 5
        self.BruchColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("approksimacia")
        saveAction = QAction("approksimacia", self)
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.appr)

        self.lst = []
        self.answer_lst = []

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True

            self.lastPoint = event.pos()


    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)

            painter.setPen(QPen(Qt.black, 2,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            painter.drawLine(self.lastPoint, event.pos())

            self.lastPoint = event.pos()

            self.update()
            # print((event.pos().x(), event.pos().y()))
            # print(tuple(event.pos()))
            # print(type((event.pos().x(), event.pos().y())))
            self.lst.append((event.pos().x(), event.pos().y()))
            # print(self.lst)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.drawing = False
            self.answer_lst.append([_ for _ in self.lst])
            # print([len(self.answer_lst[i]) for i in range(len(self.answer_lst))])
            self.lst.clear()

    def paintEvent(self, event):
        canvasPainter = QPainter(self)

        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def clear(self):
        # make the whole canvas white
        self.image.fill(Qt.white)
        # update
        self.update()

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def appr(self):
        # print([set_many_list(self.answer_lst[i]) for i in range(len(self.answer_lst))])
        # print('answer', len(self.answer_lst))
        # print(len(self.answer_lst), self.answer_lst)
        for i in range(len(self.answer_lst)):
            # print(self.answer_lst[i])
            # print(len(self.answer_lst[i]))
            # print(len(set_many_list(self.answer_lst[i])))
            # print([set_many_list(self.answer_lst[i])])
            a = set_list_x_y([set_many_list(self.answer_lst[i])])
            # print('a', len(a[0]), len(a[1]))
            # print('fhdxjbnkml;')
            for _ in range(len(a[0])):
                # print(_)
                self.mnkGP(np.asarray(a[0][_]), np.asarray(a[1][_]))
            # self.mnkGP(*set_list_x_y([set_many_list(self.answer_lst[i])]))
            # print(i*1000)
        # print(self.answer_lst)

    def make_poly(self, x, coefs):
        # generate a polynomial from an array of coefficients
        f = np.zeros(len(x))
        for i in range(len(coefs)):
            f = f + coefs[-1 - i] * x ** i
        return (f)

    def func(self, xx, yy):
        fit_result = np.polyfit(x=xx, y=yy, deg=2, full=True)
        # print(1111)
        # print(fit_result)
        newX = np.linspace(1420, 1460, 100)
        plt.scatter(xx, yy)
        plt.plot(newX, self.make_poly(newX, fit_result[0]), 'g', linewidth=.5)
        plt.show()

    def mnkGP(self, x, y):
        # print(f'x\n{x}', f'y\n{y}', sep='\n-------\n')
        if x != []:
            d = 2  # степень полинома
            fp, residuals, rank, sv, rcond = np.polyfit(x, y, d, full=True)  # Модель
            f = np.poly1d(fp)  # аппроксимирующая функция
            print('Коэффициент -- a %s  ' % round(fp[0], 4))
            print('Коэффициент-- b %s  ' % round(fp[1], 4))
            print('Коэффициент -- c %s  ' % round(fp[2], 4))
            y1 = [fp[0] * x[i] ** 2 + fp[1] * x[i] + fp[2] for i in range(0, len(x))]  # значения функции a*x**2+b*x+c
            so = round(sum([abs(y[i] - y1[i]) for i in range(0, len(x))]) / (len(x) * sum(y)) * 100, 4)  # средняя ошибка
            print('Average quadratic deviation ' + str(so))
            fx = np.linspace(x[0], x[-1] + 1, len(x))  # можно установить вместо len(x) большее число для интерполяции
            plt.plot(x, y, 'o', label='Original data', markersize=10)
            plt.plot(fx, f(fx), linewidth=2)
            plt.grid(True)
            plt.show()



App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing the window
window.show()

# start the app
sys.exit(App.exec())


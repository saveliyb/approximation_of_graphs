# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QListWidget
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from maint import *
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sqlFunc import *
from functools import partial

class history(QListWidget):  # https://doc.qt.io/qt-5/qlistwidget.html
    def __init__(self):
        super(history, self).__init__()
        self.setGeometry(1000, 100, 500, 300)
        self.setWindowTitle('Stored')
        for _ in list(read_Sql()):
            a = [i for i in json.loads(_[2]) if i != None][1:]
            try:
                self.addItem(':  '.join([_[1], '   '.join([str(i) for i in json.loads(_[2])[0]])]))
                for j in a:
                    self.addItem(''.join([''.join([' ' for i in range(len(_[1]) + 3)]), '   '.join([str(k) for k in j])]))
            except:
                pass
        self.verticalScrollBar()


class coefficients_list(QListWidget):
    def __init__(self, coefficients):
        super(coefficients_list, self).__init__()
        coefficients = [i for i in coefficients if i != None]
        self.setWindowTitle('coefficients')
        self.setGeometry(1000, 100, 500, 150)
        for i in range(len(coefficients)):
            print(roman(i+1))
            self.addItem('   '.join([roman(i+1), ':   '.join(['  '.join([str(x) for x in coefficients[i]])])]))
            # self.addItem(':  '.join([_[1], '   '.join([str(i) for i in json.loads(_[2])[0]])]))



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        create_table_sql()
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
        clear = QAction("clear", self)
        fileMenu.addAction(clear)
        clear.triggered.connect(self.clear)
        save = QAction("save", self)
        fileMenu.addAction(save)
        save.triggered.connect(self.save)
        stored = QAction("stored", self)
        fileMenu.addAction(stored)
        stored.triggered.connect(self.stored)
        Action = QAction("approksimacia", self)
        fileMenu.addAction(Action)
        Action.triggered.connect(self.appr)
        Action.triggered.connect(partial(self.coefficientslisting, coefficients=self.coefficients))



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
            self.lst.append((event.pos().x(), event.pos().y()))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.drawing = False
            self.answer_lst.append([_ for _ in self.lst])
            self.lst.clear()

    def paintEvent(self, event):
        canvasPainter = QPainter(self)

        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def clear(self):
        self.image.fill(Qt.white)
        self.lst = []
        self.answer_lst = []
        self.update()


    def coefficientslisting(self, coefficients):
        print(self.coefficients)
        self.coefficientslisting = coefficients_list(self.coefficients)
        # self.coefficientslisting.coefficients = self.coefficients
        self.coefficientslisting.show()

    def stored(self):
        # a = history()
        self.widget = history()
        self.widget.show()

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        # print(filePath, _)
        name = filePath.split('/')[-1].split('.')[0]
        write_sql(name, self.coefficients)
        if filePath == "":
            return
        self.image.save(filePath)

    def appr(self):
        lst = []
        for i in range(len(self.answer_lst)):
            a = set_list_x_y([set_many_list(self.answer_lst[i])])
            for _ in range(len(a[0])):
                lst.append(self.mnkGP(np.asarray(a[0][_]), np.asarray(a[1][_])))
        self.coefficients = [_ for _ in lst]
        # self.coefficients_listing(self.coefficients)


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
            coefficients = [round(fp[0], 4), round(fp[1], 4), round(fp[2], 4)]

            print('Коэффициент -- a %s  ' % round(fp[0], 4))
            print('Коэффициент-- b %s  ' % round(fp[1], 4))
            print('Коэффициент -- c %s  ' % round(fp[2], 4))
            y1 = [fp[0] * x[i] ** 2 + fp[1] * x[i] + fp[2] for i in range(0, len(x))]  # значения функции a*x**2+b*x+c
            # so = round(sum([abs(y[i] - y1[i]) for i in range(0, len(x))]) / (len(x) * sum(y)) * 100, 4)  # средняя ошибка
            # print('Average quadratic deviation ' + str(so))
            # print(f'x принадежит от {min(x)}, до {max(x)}')
            fx = np.linspace(x[0], x[-1] + 1, len(x))  # можно установить вместо len(x) большее число для интерполяции
            plt.plot(x, y, 'o', label='Original data', markersize=10)
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
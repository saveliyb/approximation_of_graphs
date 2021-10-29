# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from main import set_many_list

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint")

        self.setGeometry(100, 100, 800, 600)

        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
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
            print([len(self.answer_lst[i]) for i in range(len(self.answer_lst))])
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
        print([set_many_list(self.answer_lst[i]) for i in range(len(self.answer_lst))])
        # print(self.answer_lst)



App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing the window
window.show()

# start the app
sys.exit(App.exec())


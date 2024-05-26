from view import mouse
from view import wallpaper
from view import aidraw
from view import extrafunction
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
import sys
import keyboard




class ImageLabel(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.resize(600, 400)
            self.setWindowTitle("label image")

            pix = QPixmap(r'E:\logo.jpg')
            label = QLabel(self)
            label.setPixmap(pix)
            label.setScaledContents(True)  # 自适应QLabel大小

            layout = QVBoxLayout()
            layout.addWidget(label)
            self.setLayout(layout)

def test1():
    app = QApplication(sys.argv)
    mainWidget = ImageLabel()
    mainWidget.show()

class AUi(QtWidgets.QMainWindow, mouse.Ui_mouse):
    def __init__(self):
        super(AUi, self).__init__()
        self.setupUi(self)

class BUi(QtWidgets.QMainWindow, wallpaper.Ui_Wallpaper):
    def __init__(self):
        super(BUi, self).__init__()
        self.setupUi(self)


class CUi(QtWidgets.QMainWindow, aidraw.Ui_aidraw ):
    def __init__(self):
        super(CUi, self).__init__()
        self.setupUi(self)

class DUi(QtWidgets.QMainWindow, extrafunction.Ui_extrafunction):
    def __init__(self):
        super(DUi, self).__init__()
        self.setupUi(self)

keyboard.add_hotkey('q', test1)

def view():
    app = QtWidgets.QApplication(sys.argv)
    a = AUi()
    a.show()
    b = BUi()
    c=CUi()
    d=DUi()
    # button是你定义的按钮
    a.pushButton_2.clicked.connect(
    	lambda:{a.close(), b.show()}
   	)
    a.pushButton_3.clicked.connect(
        lambda: {a.close(), c.show()}
    )
    a.pushButton_4.clicked.connect(
        lambda: {a.close(), d.show()}
    )
    a.pushButton_5.clicked.connect(
        lambda: {
            #在这里打开资源编辑器
            print("测试")
        }
    )
    b.pushButton.clicked.connect(
        lambda: {b.close(), a.show()}
    )
    b.pushButton_2.clicked.connect(
        lambda: {b.close(), c.show()}
    )
    b.pushButton_3.clicked.connect(
        lambda: {b.close(), d.show()}
    )
    c.pushButton.clicked.connect(
        lambda: {c.close(), a.show()}
    )
    c.pushButton_2.clicked.connect(
        lambda: {c.close(), b.show()}
    )
    c.pushButton_3.clicked.connect(
        lambda: {c.close(), d.show()}
    )
    d.pushButton.clicked.connect(
        lambda: {d.close(), a.show()}
    )
    d.pushButton_2.clicked.connect(
        lambda: {d.close(), b.show()}
    )
    d.pushButton_3.clicked.connect(
        lambda: {d.close(), c.show()}
    )
    app.setWindowIcon(QIcon('logo.jpg'))



    sys.exit(app.exec_())




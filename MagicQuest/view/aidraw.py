# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\practice\helloworld\.ui\aidraw.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aidraw(object):
    def setupUi(self, aidraw):
        aidraw.setObjectName("aidraw")
        aidraw.resize(500, 500)
        aidraw.setStyleSheet("QPushButton:hover { color: red }\n"
"QPushButton {   \n"
"    width:50px;\n"
"    height:20px;\n"
"    font: 75 9pt \"Bahnschrift Condensed\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(aidraw)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        aidraw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(aidraw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        aidraw.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(aidraw)
        self.statusbar.setObjectName("statusbar")
        aidraw.setStatusBar(self.statusbar)

        self.retranslateUi(aidraw)
        QtCore.QMetaObject.connectSlotsByName(aidraw)

    def retranslateUi(self, aidraw):
        _translate = QtCore.QCoreApplication.translate
        aidraw.setWindowTitle(_translate("aidraw", "Aidraw"))
        self.pushButton.setText(_translate("aidraw", "鼠标区"))
        self.pushButton_2.setText(_translate("aidraw", "壁纸区"))
        self.pushButton_3.setText(_translate("aidraw", "额外功能区"))
        self.pushButton_4.setText(_translate("aidraw", "设置区"))

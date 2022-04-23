# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from maincode2 import Ui_Form
from forgatten import Ui_Formn
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_Formmain(object):
    def setupUimain(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1002, 668)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Form.setFont(font)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setToolTip("")
        Form.setStatusTip("")
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1002, 668))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame{\n"
" background:;\n"
" image:url(ipad.jpg);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(240, 170, 531, 391))
        self.frame_2.setStyleSheet("#frame_2{\n"
" background:rgba(0,0,0,0.6);\n"
" border-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 431, 41))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
" border-radius:10px;\n"
" color:#000000;\n"
"  font-size:20px;\n"
"}\n"
"#lineEdit:focus{\n"
"  border: 4px solid  #9597ff\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 431, 41))
        self.lineEdit_2.setStyleSheet("#lineEdit_2{\n"
" border-radius:10px;\n"
" color:#000000;\n"
"  font-size:20px;\n"
"}\n"
"#lineEdit_2:focus{\n"
"  border: 4px solid  #9597ff\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(50, 257, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" #pushButton{\n"
"background: #0055ff;\n"
"\n"
"border-radius:15px;\n"
"  color:#fff;\n"
" font-size:27px;\n"
"}\n"
"#pushButton:focus{\n"
"  background:#ff0000;\n"
"transition: 0.7s;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(450, 120, 101, 101))
        self.frame_3.setStyleSheet("#frame_3{\n"
"background:#fff;\n"
"background:;\n"
"image:url(logooo.png);\n"
"border-radius:50px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 320, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(" #pushButton_2{\n"
                                      "background:rgba(0,0,0,0.4);\n"
                                      "\n"
                                      "border-radius:15px;\n"
                                      "  color:red;\n"
                                      " font-size:18px;\n"
                                      "}\n"
                                      "#pushButton_2:focus{\n"
                                      "  background:rgba(0,0,0,0.4);\n"
                                        "color: green;\n" 
                                      "transition: 0.7s;\n"
                                      "}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.data)
        self.pushButton_2.clicked.connect(self.openwindow)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Students Management System"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "login"))
        self.pushButton_2.setText(_translate("Form", "forgatten password"))
        #self.label.setText(_translate("Form", "forgatten password"))

    def data(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        root = sqlite3.connect('logindata.db')
        cursor = root.cursor()
        sql = "SELECT * FROM loginn WHERE Username='" + user + "' and Password='" + password + "'"
        cursor.execute(sql)
        root.commit()
        self.ab = cursor.fetchone()
        if self.ab!=None:
            self.window=QtWidgets.QFrame(Form)
            self.ui = Ui_Form()
            self.ui.setupUi2(self.window)
            self.window.show()

            self.ui.labelname.setText(self.ab[1])
            self.ui.labelid.setText(self.ab[0])
            self.ui.labelrole.setText(self.ab[3])
            self.ui.toolButton_7.clicked.connect(self.logmm)

        else:

            msg = QMessageBox()

            msg.setWindowTitle("Students System")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username or Password are not valid !")
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setWindowOpacity(1.0)
            msg.setStyleSheet("#msg{\n""background:black; \n""}")
            mt=msg.exec_()
            if mt==QMessageBox.Ok:
                self.lineEdit.clear()
                self.lineEdit_2.clear()

    def logmm(self):
        #app = QtWidgets.QApplication(sys.argv)
        self.xx = QtWidgets.QWidget()
        ui5 = Ui_Formmain()
        ui5.setupUimain(self.xx)
        self.xx.show()



    def openwindow(self):
        self.window3 = QtWidgets.QWidget()
        self.ui = Ui_Formn()
        self.ui.setupUi6(self.window3)
        self.window3.show()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui5 = Ui_Formmain()
    ui5.setupUimain(Form)
    Form.setFixedWidth(1002)
    Form.setFixedHeight(668)
    Form.show()
    sys.exit(app.exec_())

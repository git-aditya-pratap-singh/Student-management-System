# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewstudent.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from view import Ui_Formview1


class Ui_Formview(object):
    def setupUiview(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 593)
        self.frametop = QtWidgets.QFrame(Form)
        self.frametop.setGeometry(QtCore.QRect(0, -1, 861, 153))
        self.frametop.setStyleSheet("#frametop{\n"
" background:#fff;\n"
"}")
        self.frametop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frametop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frametop.setObjectName("frametop")
        self.label = QtWidgets.QLabel(self.frametop)
        self.label.setGeometry(QtCore.QRect(130, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
" font-size:16px;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frametop)
        self.lineEdit.setGeometry(QtCore.QRect(240, 60, 311, 31))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frametop)
        self.pushButton.setGeometry(QtCore.QRect(580, 60, 151, 33))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"\n"
" border-radius:10px;\n"
"background:#5500ff;\n"
"\n"
" color:#fff;\n"
" font-size:20px;\n"
" }\n"
"#pushButton:hover{\n"
" background:#5555ff;\n"
" border:2px solid #00ff7f;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.framebottom = QtWidgets.QFrame(Form)
        self.framebottom.setGeometry(QtCore.QRect(0, 150, 861, 441))
        self.framebottom.setStyleSheet("#framebottom{\n"
" background:#fff;\n"
" background:;\n"
" image:url(istockphoto-913084642-612x612.jpg);\n"
"}")
        self.framebottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framebottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framebottom.setObjectName("framebottom")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.show_value)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ERP-ID :"))
        self.pushButton.setText(_translate("Form", "Submit"))


    def show_value(self):

        self.value=self.lineEdit.text()

        import sqlite3
        conn=sqlite3.connect('studentinfo.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM info WHERE ERP_ID='"+self.value+"'")
        conn.commit()
        self.data_value=cursor.fetchone()
        if self.data_value!=None:

            self.winc = QtWidgets.QFrame(self.framebottom)
            self.ui = Ui_Formview1()
            self.ui.setupUiview1(self.winc)
            self.winc.show()

            self.ui.labelid1.setText(self.data_value[0])
            self.ui.labelname1.setText(self.data_value[1])
            self.ui.labelroll1.setText(self.data_value[2])
            self.ui.labelgen1.setText(self.data_value[3])
            self.ui.labelno1.setText(self.data_value[4])
            self.ui.labelcourse1.setText(self.data_value[5])
            self.ui.labeldo1.setText(self.data_value[6])
            self.ui.labelmail1.setText(self.data_value[7])

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Students System")
            msg.move(860, 550)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("YOUR ID IS NOT CORRECT !")
            msg.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setWindowOpacity(1.0)
            msg.setStyleSheet("#msg{\n""background:black; \n""}")
            et = msg.exec_()

            if et == QMessageBox.Ok:
                self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui4 = Ui_Formview()
    ui4.setupUiview(Form)
    Form.show()
    sys.exit(app.exec_())

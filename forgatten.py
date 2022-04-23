# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgatten.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Ui_Formn(object):
    def setupUi6(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 438)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"color:#ff007f;\n"
"font-weight:20px;\n"
"}")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 74, 611, 4))
        font = QtGui.QFont()
        font.setPointSize(2)
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame{\n"
"background:#0000ff;\n"
"border-radius:30px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 130, 341, 31))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"\n"
"#lineEdit:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_error = QtWidgets.QLabel(Form)
        self.label_error.setGeometry(QtCore.QRect(250, 160, 271, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("#label_error{\n"
"color:red;\n"
"}")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 210, 341, 31))
        self.lineEdit_2.setStyleSheet("#lineEdit_2{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"\n"
"#lineEdit_2:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 290, 341, 31))
        self.lineEdit_3.setStyleSheet("#lineEdit_3{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"\n"
"#lineEdit_3:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 330, 291, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("#label_5{\n"
" color:red;\n"
"}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 370, 231, 37))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
" color:#fff;\n"
" background:#0055ff;\n"
" border-radius:10px;\n"
"}\n"
"#pushButton:hover{\n"
" background:#3094ff;\n"
" border:1px solid #00ff7f;\n"
"}")
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.Embu, QtCore.QLocale.Kenya))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.update)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Student System"))
        self.label.setText(_translate("Form", "Forgatten Password"))
        self.label_2.setText(_translate("Form", "User ID :"))
        self.label_3.setText(_translate("Form", " New Password :"))
        self.label_4.setText(_translate("Form", " Confirm Password :"))
        self.pushButton.setText(_translate("Form", "Submit"))

    def update(self):

        self.id = self.lineEdit.text()
        self.new=self.lineEdit_2.text()
        self.confirm=self.lineEdit_3.text()


        conn = sqlite3.connect("logindata.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM loginn WHERE Username='" + self.id + "'"
        cursor.execute(sql)
        conn.commit()
        self.id1 = cursor.fetchone()
        if self.id1 != None:

            self.label_error.setText("")

            if self.new==self.confirm:
                self.label_5.setText("")
                msg = QMessageBox()

                msg.setWindowTitle("Students System")
                msg.setIcon(QMessageBox.Question)
                msg.setText("Are you sure ?")
                msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setWindowOpacity(1.0)
                msg.setStyleSheet("#msg{\n""background:black; \n""}")
                mt = msg.exec_()
                if mt == QMessageBox.Ok:


                     game=sqlite3.connect("logindata.db")
                     cursor=game.cursor()
                     sql2="UPDATE loginn SET Password='"+self.confirm+"' WHERE Username='"+self.id+"'"
                     cursor.execute(sql2)
                     game.commit()

                     self.id = self.lineEdit.clear()
                     self.new = self.lineEdit_2.clear()
                     self.confirm = self.lineEdit_3.clear()

                     msg2 = QMessageBox()

                     msg2.setWindowTitle("Students System")
                     msg2.setIcon(QMessageBox.Question)
                     msg2.setText("your Password is reset !")
                     msg2.setStandardButtons(QMessageBox.Ok)
                     icon = QtGui.QIcon()
                     icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                     msg2.setWindowIcon(icon)
                     msg2.setWindowOpacity(1.0)
                     msg2.setStyleSheet("#msg2{\n""background:black; \n""}")
                     msg2.exec_()


            else:
                self.label_5.setText("does not match")

        else:
            self.label_error.setText("id is not required")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui= Ui_Formn()
    ui.setupUi6(Form)
    Form.setFixedWidth(649)
    Form.setFixedHeight(438)
    Form.show()
    sys.exit(app.exec_())

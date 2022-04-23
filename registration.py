# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formaadi(object):
    def setupUiaadi(self, Form):
        Form.setObjectName("Form")
        Form.resize(868, 591)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 868, 601))
        self.frame.setStyleSheet("#frame{\n"
" background:#fff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 30, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
" color:#ff0059;\n"
"font-size:55px;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(340, 180, 341, 31))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 258, 341, 31))
        self.lineEdit_2.setStyleSheet("#lineEdit_2{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_2:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 330, 341, 31))
        self.lineEdit_3.setStyleSheet("#lineEdit_3{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_3:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
" font-size:15px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 110, 831, 4))
        self.frame_2.setStyleSheet("#frame_2{\n"
" background:blue;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(180, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
"font-size:15px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(180, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
" font-size:15px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(180, 410, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("#label_5{\n"
"font-size:15px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(340, 410, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("#radioButton{\n"
" color:blue;\n"
 " font-size:12px;\n"                                      
"}")
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.sele)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(280, 500, 291, 36))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"color:#fff;\n"
"font-size:20px;\n"
"background:#5500ff;\n"
"border-radius:10px;\n"
" }\n"
"#pushButton:hover{\n"
"border:2px solid #61ffb0;\n"
"background:#5555ff;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.user_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " Registration"))
        self.label_2.setText(_translate("Form", "Username :"))
        self.label_3.setText(_translate("Form", "Name :"))
        self.label_4.setText(_translate("Form", "Password :"))
        self.label_5.setText(_translate("Form", "Role :"))
        self.radioButton.setText(_translate("Form", "Admin"))
        self.pushButton.setText(_translate("Form", "Submit"))

    def sele(self, selected):
        if selected:
            self.d=self.radioButton.text()


    def user_data(self):
        self.a=self.lineEdit.text()
        self.b= self.lineEdit_2.text()
        self.c = self.lineEdit_3.text()
        #self.d=self.radioButton.text()

        import sqlite3
        conn=sqlite3.connect('logindata.db')
        cursor=conn.cursor()
        cursor.execute("INSERT INTO loginn (Username,Name,Password,Role) values(?,?,?,?)",(self.a,self.b,self.c,self.d))
        conn.commit()

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        #self.radioButton.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formaadi()
    ui.setupUiaadi(Form)
    Form.show()
    sys.exit(app.exec_())

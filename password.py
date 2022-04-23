# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Formword(object):
    def setupUiword(self, Form):
        Form.setObjectName("Form")
        Form.resize(858, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 858, 591))
        self.frame.setStyleSheet("#frame{\n"
" background:#fff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 20, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
" color:#ff0059;\n"
" font-size:45px;\n"
"}")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 90, 811, 4))
        self.frame_2.setStyleSheet("#frame_2{\n"
" background:#5500ff;\n"
" border-radius:3px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
" font-size:15px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(370, 160, 341, 31))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 266, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
" font-size:15px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 270, 341, 31))
        self.lineEdit_2.setStyleSheet("#lineEdit_2{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_2:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(130, 376, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
" font-size:15px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 380, 341, 31))
        self.lineEdit_3.setStyleSheet("#lineEdit_3{\n"
"border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_3:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(330, 480, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"background:#37ff7a;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"font-size:18px;\n"
"}\n"
"#pushButton:hover{\n"
"border:2px solid #5500ff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.iderror = QtWidgets.QLabel(self.frame)
        self.iderror.setGeometry(QtCore.QRect(380, 200, 281, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.iderror.setFont(font)
        self.iderror.setStyleSheet("#iderror{\n"
" color:#ff002e;"
" font-size:13px;\n"
"}")
        self.iderror.setText("")
        self.iderror.setObjectName("iderror")
        self.olderror = QtWidgets.QLabel(self.frame)
        self.olderror.setGeometry(QtCore.QRect(380, 310, 291, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.olderror.setFont(font)
        self.olderror.setStyleSheet("#olderror{\n"
" color:#ff002e;"
"font-size:13px;\n"
"}")
        self.olderror.setText("")
        self.olderror.setObjectName("olderror")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.pass_change)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Student Management System"))
        self.label.setText(_translate("Form", "Change password"))
        self.label_2.setText(_translate("Form", "User ID :"))
        self.label_3.setText(_translate("Form", "Old password :"))
        self.label_4.setText(_translate("Form", "New password :"))
        self.pushButton.setText(_translate("Form", "change"))

    def pass_change(self):
        self.id=self.lineEdit.text()
        self.old=self.lineEdit_2.text()
        self.new_pass=self.lineEdit_3.text()
        import sqlite3
        root=sqlite3.connect('logindata.db')
        cursor=root.cursor()
        cursor.execute("SELECT * FROM loginn WHERE Username='"+self.id+"'")
        root.commit()
        self.data=cursor.fetchone()
        if self.data!=None:
            if self.data[0]==self.id:
                self.iderror.setText("")

            if self.data[2]==self.old:
                self.olderror.setText("")

                #--------------new password store-------------------

                cursor1=root.cursor()
                cursor1.execute("UPDATE loginn SET Password='"+self.new_pass+"' WHERE Username='"+self.id+"'")
                root.commit()

                #------Popup message show---------------

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Students System")
                msg.move(860, 550)
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Your Password is updated !")
                msg.setStandardButtons(QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setWindowOpacity(1.0)
                msg.setStyleSheet("#msg{\n""background:black; \n""}")
                et = msg.exec_()

                if et == QMessageBox.Ok:
                    self.lineEdit.clear()
                    self.lineEdit_2.clear()
                    self.lineEdit_3.clear()

            else:
                self.olderror.setText("password is not required")



        else:
            self.iderror.setText("Id is not required")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formword()
    ui.setupUiword(Form)
    Form.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from updatewindow import Ui_Formwindow
import sqlite3

db = sqlite3.connect('studentinfo.db')

class Ui_Formupdate(object):
    def setupUiupdate(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 491)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 861, 491))
        self.frame.setStyleSheet("#frame{\n"
" background:#fff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 30, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
" color:#ff007f;\n"
" font-size:43px;\n"
" \n"
"}")
        self.label.setObjectName("label")
        self.frame_2img = QtWidgets.QFrame(self.frame)
        self.frame_2img.setGeometry(QtCore.QRect(160, 110, 541, 361))
        self.frame_2img.setStyleSheet("#frame_2img{\n"
" background:;\n"
" image:url(taylor-vick-v2EpcozYjMw-unsplash.jpg);\n"
" \n"
"}")
        self.frame_2img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2img.setObjectName("frame_2img")
        self.frame_2 = QtWidgets.QFrame(self.frame_2img)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 541, 361))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("#frame_2{\n"
" background:rgba(0,0,0,0.4);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2id = QtWidgets.QLabel(self.frame_2)
        self.label_2id.setGeometry(QtCore.QRect(60, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2id.setFont(font)
        self.label_2id.setStyleSheet("#label_2id{\n"
" color:#fff;\n"
" font-size:20px;\n"
"}")
        self.label_2id.setObjectName("label_2id")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(180, 101, 291, 31))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"}\n"
"#lineEdit:hover{\n"
"background:#e5f4ff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(170, 200, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
" background:#5500ff;\n"
" border-radius:5px;\n"
" color:#fff;\n"
" font-size:20px;\n"
" }\n"
"#pushButton:hover{\n"
" background:#5555ff;\n"
" border:2px solid #00ff7f;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.frame_3line = QtWidgets.QFrame(self.frame)
        self.frame_3line.setGeometry(QtCore.QRect(29, 89, 811, 4))
        self.frame_3line.setStyleSheet("#frame_3line{\n"
" background:#0000ff;\n"
"}")
        self.frame_3line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3line.setObjectName("frame_3line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.show_data)





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Update Data"))
        self.label_2id.setText(_translate("Form", "ERP-ID :"))
        self.pushButton.setText(_translate("Form", "Submit"))

    def show_data(self):
        self.getid = self.lineEdit.text()


        cursor=db.cursor()
        cursor.execute("SELECT * FROM info WHERE ERP_ID='"+self.getid+"'")
        db.commit()
        self.data=cursor.fetchone()
        if self.data!=None:
            self.window=QtWidgets.QWidget()
            self.ui = Ui_Formwindow()

            self.ui.setupUiwindow(self.window)

            self.ui.pushButton.clicked.connect(self.update)
            self.ui.radioButton.toggled.connect(self.maleselected)
            self.ui.radioButton_2.toggled.connect(self.femaleselected)

            self.window.show()
            self.ui.lineEdit.setText(self.data[0])
            self.ui.lineEdit_2.setText(self.data[1])
            self.ui.lineEdit_3.setText(self.data[2])


            if self.data[3] == "Male":
                self.ui.radioButton.setChecked(True)
            else:
                self.ui.radioButton_2.setChecked(True)


            self.ui.lineEdit_5.setText(self.data[4])
            self.ui.lineEdit_4.setText(self.data[5])
            self.ui.lineEdit_6.setText(self.data[7])
            self.ui.lineEdit_9.setText(self.data[6])

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Students System")
            msg.move(860,550)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("YOUR ID IS NOT FOUND !")
            #msg= QMessageBox.question("YOUR ID IS NOT FOUND !",QMessageBox.Ok)
            msg.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setWindowOpacity(1.0)
            msg.setStyleSheet("#msg{\n""background:black; \n""}")
            et=msg.exec_()

            if et==QMessageBox.Ok:
                self.lineEdit.clear()

    def maleselected(self, selected):
            if selected:
                self.cd = self.ui.radioButton.text()
                self.m = self.cd

    def femaleselected(self, selected):
            if selected:
                self.bf = self.ui.radioButton_2.text()
                self.m = self.bf

    def update(self):

        self.a=self.ui.lineEdit.text()
        self.b=self.ui.lineEdit_2.text()
        self.c = self.ui.lineEdit_3.text()
        self.d=self.ui.lineEdit_4.text()
        self.e = self.ui.lineEdit_5.text()
        self.f = self.ui.lineEdit_6.text()
        self.g= self.ui.lineEdit_9.text()

         # impoet database

        import sqlite3
        conn = sqlite3.connect('studentinfo.db')
        cursor1 = conn.cursor()
        cursor1.execute("UPDATE info SET ERP_ID='"+self.a+"', Name='"+self.b+"', Roll_no='"+self.c+"',Gender='"+self.m+"', Phone_no='"+self.e+"', Course='"+self.d+"', e_mail='"+self.f+"', DOB='"+self.g+"' WHERE ERP_ID='"+ self.getid+"'")
        conn.commit()

        #popup msg ---your data is updated------

        msg2 = QtWidgets.QMessageBox()
        msg2.setWindowTitle("Students System")
        msg2.move(860, 550)
        msg2.setIcon(QMessageBox.Information)
        msg2.setText("YOUR DATA IS UPDATED !")
        msg2.setStandardButtons(QMessageBox.Ok)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg2.setWindowIcon(icon)
        msg2.setWindowOpacity(1.0)
        msg2.setStyleSheet("#msg{\n""background:black; \n""}")
        msg2.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui7 = Ui_Formupdate()
    ui7.setupUiupdate(Form)
    Form.show()
    sys.exit(app.exec_())

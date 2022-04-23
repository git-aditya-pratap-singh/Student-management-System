# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Formdelete(object):
    def setupUidelete(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 490)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, -1, 861, 491))
        self.frame.setStyleSheet("#frame{\n"
" background:#fff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
" color:#ff007f;\n"
" font-size:43px;\n"
"}")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 89, 821, 4))
        self.frame_2.setStyleSheet("#frame_2{\n"
" background:#0000ff;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(180, 130, 491, 331))
        self.frame_3.setStyleSheet("#frame_3{\n"
" background:;\n"
" image:url(ad.jpg);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 491, 330))
        self.frame_4.setStyleSheet("#frame_4{\n"
" background:rgba(0,0,0,0.6);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
" color:#fff;\n"
" font-size:19px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(180, 90, 231, 31))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"}\n"
"#lineEdit:hover{\n"
" background:#e5f4ff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(145, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
" background:#20aa65;\n"
" border-radius:5px;\n"
" font-size:20px;\n"
" color:#fff;\n"
"}\n"
"#pushButton:hover{\n"
" border:2px solid #00ff7f;\n"
" background:#65ff6a;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.delete_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Delete Data"))
        self.label_2.setText(_translate("Form", "ERP-ID :"))
        self.pushButton.setText(_translate("Form", "Submit"))

    def delete_data(self):
        self.data=self.lineEdit.text()
        import sqlite3
        root=sqlite3.connect('studentinfo.db')
        cursor=root.cursor()
        cursor.execute("DELETE FROM info WHERE ERP_ID='"+self.data+"'")
        root.commit()

        #popup message show delete data---------------

        msg2 = QtWidgets.QMessageBox()
        msg2.setWindowTitle("Students System")
        msg2.move(860, 550)
        msg2.setIcon(QMessageBox.Information)
        msg2.setText("YOUR DATA IS DELETED !")
        msg2.setStandardButtons(QMessageBox.Ok)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg2.setWindowIcon(icon)
        msg2.setWindowOpacity(1.0)
        msg2.setStyleSheet("#msg{\n""background:black; \n""}")
        em=msg2.exec_()
        if em==QMessageBox.Ok:
            self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formdelete()
    ui.setupUidelete(Form)
    Form.show()
    sys.exit(app.exec_())

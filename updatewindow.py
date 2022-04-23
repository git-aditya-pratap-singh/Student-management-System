# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatewindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Formwindow(object):
    def setupUiwindow(self, Form):
        Form.setObjectName("Form")
        Form.resize(717, 478)
        Form.move(665,339)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stulogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
" background:#fff;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
" font-size:15px;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 31, 381, 31))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit:hover{\n"
" background:#e5f4ff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
" font-size:15px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 100, 381, 31))
        self.lineEdit_2.setStyleSheet("#lineEdit_2{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_2:hover{\n"
" background:#e5f4ff;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
" font-size:15px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 170, 381, 31))
        self.lineEdit_3.setStyleSheet("#lineEdit_3{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_3:hover{\n"
" background:#e5f4ff;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 235, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
" font-size:15px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(230, 240, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("#radioButton{\n"
" font-size:13px;\n"
" color:blue;\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(300, 240, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("#radioButton_2{\n"
" font-size:13px;\n"
" color:blue;\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 240, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("#label_5{\n"
" font-size:15px;\n"
"}")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 300, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("#label_6{\n"
" font-size:15px;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 296, 121, 31))
        self.lineEdit_4.setStyleSheet("#lineEdit_4{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_4:hover{\n"
" background:#e5f4ff;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 296, 231, 31))
        self.lineEdit_5.setStyleSheet("#lineEdit_5{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_5:hover{\n"
" background:#e5f4ff;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 360, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("#label_7{\n"
" font-size:15px;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 357, 381, 31))
        self.lineEdit_6.setStyleSheet("#lineEdit_6{\n"
" border-radius:5px;\n"
" font-size:19px;\n"
"border:1px solid #00ff7f;\n"
"}\n"
"#lineEdit_6:hover{\n"
" background:#e5f4ff;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(288, 417, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
" background:#1e40ff;\n"
" \n"
" border-radius:10px;\n"
" color:#fff;\n"
" font-size:17px;\n"
"}\n"
"#pushButton:hover{\n"
" background:#3e8bff;\n"
" border:2px solid #3aff61;\n"
"}")

        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(474, 234, 137, 31))
        self.lineEdit_9.setStyleSheet("#lineEdit_9{\n"
                                      " border-radius:5px;\n"
                                      " font-size:19px;\n"
                                      "border:1px solid #00ff7f;\n"
                                      "}\n"
                                      "#lineEdit_9:hover{\n"
                                      " background:#e5f4ff;\n"
                                      "}")
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Student Management System"))
        self.label.setText(_translate("Form", "ERP-ID :"))
        self.label_2.setText(_translate("Form", "Name :"))
        self.label_3.setText(_translate("Form", "Roll No :"))
        self.label_4.setText(_translate("Form", "Gender :"))
        self.radioButton.setText(_translate("Form", "Male"))
        self.radioButton_2.setText(_translate("Form", "Female"))
        self.label_5.setText(_translate("Form", "DOB :"))
        self.label_6.setText(_translate("Form", "Course :"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", " Phone no"))
        self.label_7.setText(_translate("Form", "e-mail :"))
        self.pushButton.setText(_translate("Form", "Submit"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formwindow()
    ui.setupUiwindow(Form)
    Form.show()
    sys.exit(app.exec_())

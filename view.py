# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formview1(object):
    def setupUiview1(self, Form):
        Form.setObjectName("Form")
        Form.resize(861, 441)
        Form.setStyleSheet("#Form{\n"
" background:black;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(160, 30, 551, 381))
        self.frame.setStyleSheet("#frame{\n"
" background:#fff;\n"
" border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelid = QtWidgets.QLabel(self.frame)
        self.labelid.setGeometry(QtCore.QRect(100, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelid.setFont(font)
        self.labelid.setStyleSheet("#labelid{\n"
" font-size:15px;\n"
"}")
        self.labelid.setObjectName("labelid")
        self.labelid1 = QtWidgets.QLabel(self.frame)
        self.labelid1.setGeometry(QtCore.QRect(200, 30, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelid1.setFont(font)
        self.labelid1.setStyleSheet("#labelid1{\n"
" color:blue;\n"
"font-size:15px;\n"
"}")
        self.labelid1.setText("")
        self.labelid1.setObjectName("labelid1")
        self.labelname = QtWidgets.QLabel(self.frame)
        self.labelname.setGeometry(QtCore.QRect(100, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelname.setFont(font)
        self.labelname.setStyleSheet("#labelname{\n"
" font-size:15px;\n"
"}")
        self.labelname.setObjectName("labelname")
        self.labelname1 = QtWidgets.QLabel(self.frame)
        self.labelname1.setGeometry(QtCore.QRect(200, 85, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelname1.setFont(font)
        self.labelname1.setStyleSheet("#labelname1{\n"
" color:blue;\n"
"font-size:15px;\n"
"}")
        self.labelname1.setText("")
        self.labelname1.setObjectName("labelname1")
        self.labelroll = QtWidgets.QLabel(self.frame)
        self.labelroll.setGeometry(QtCore.QRect(100, 145, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelroll.setFont(font)
        self.labelroll.setStyleSheet("#labelroll{\n"
" font-size:15px;\n"
"}")
        self.labelroll.setObjectName("labelroll")
        self.labelroll1 = QtWidgets.QLabel(self.frame)
        self.labelroll1.setGeometry(QtCore.QRect(200, 143, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelroll1.setFont(font)
        self.labelroll1.setStyleSheet("#labelroll1{\n"
" color:blue;\n"
"font-size:15px;\n"
"}")
        self.labelroll1.setText("")
        self.labelroll1.setObjectName("labelroll1")
        self.labelgen = QtWidgets.QLabel(self.frame)
        self.labelgen.setGeometry(QtCore.QRect(100, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelgen.setFont(font)
        self.labelgen.setStyleSheet("#labelgen{\n"
" font-size:15px;\n"
"}")
        self.labelgen.setObjectName("labelgen")
        self.labelgen1 = QtWidgets.QLabel(self.frame)
        self.labelgen1.setGeometry(QtCore.QRect(200, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelgen1.setFont(font)
        self.labelgen1.setStyleSheet("#labelgen1{\n"
" color:blue;\n"
"font-size:15px;\n"
"}")
        self.labelgen1.setText("")
        self.labelgen1.setObjectName("labelgen1")
        self.labelno = QtWidgets.QLabel(self.frame)
        self.labelno.setGeometry(QtCore.QRect(100, 260, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelno.setFont(font)
        self.labelno.setStyleSheet("#labelno{\n"
" font-size:15px;\n"
"}")
        self.labelno.setObjectName("labelno")
        self.labelno1 = QtWidgets.QLabel(self.frame)
        self.labelno1.setGeometry(QtCore.QRect(200, 260, 161, 29))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelno1.setFont(font)
        self.labelno1.setStyleSheet("#labelno1{\n"
" color:blue;\n"
"font-size:15px;\n"
"}")
        self.labelno1.setText("")
        self.labelno1.setObjectName("labelno1")

        #--------------------------------------------------------------------
        self.labeldo = QtWidgets.QLabel(self.frame)
        self.labeldo.setGeometry(QtCore.QRect(320, 265, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labeldo.setFont(font)
        self.labeldo.setStyleSheet("#labeldo{\n"
                                   " font-size:15px;\n"
                                   "}")
        self.labeldo.setObjectName("labeldo")
        self.labeldo1 = QtWidgets.QLabel(self.frame)
        self.labeldo1.setGeometry(QtCore.QRect(375, 260, 161, 29))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labeldo1.setFont(font)
        self.labeldo1.setStyleSheet("#labeldo1{\n"
                                    " color:blue;\n"
                                    "font-size:15px;\n"
                                    "}")
        self.labeldo1.setText("")
        self.labeldo1.setObjectName("labeldo1")

        #--------------------------------------------------------------------


        self.labelcourse = QtWidgets.QLabel(self.frame)
        self.labelcourse.setGeometry(QtCore.QRect(270, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelcourse.setFont(font)
        self.labelcourse.setStyleSheet("#labelcourse{\n"
"font-size:15px;\n"
"}")
        self.labelcourse.setObjectName("labelcourse")
        self.labelcourse1 = QtWidgets.QLabel(self.frame)
        self.labelcourse1.setGeometry(QtCore.QRect(360, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelcourse1.setFont(font)
        self.labelcourse1.setStyleSheet("#labelcourse1{\n"
" color:blue;\n"
" font-size:15px;\n"
"}")
        self.labelcourse1.setText("")
        self.labelcourse1.setObjectName("labelcourse1")
        self.labelmail = QtWidgets.QLabel(self.frame)
        self.labelmail.setGeometry(QtCore.QRect(100, 310, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelmail.setFont(font)
        self.labelmail.setStyleSheet("#labelmail{\n"
" font-size:15px;\n"
"}")
        self.labelmail.setObjectName("labelmail")
        self.labelmail1 = QtWidgets.QLabel(self.frame)
        self.labelmail1.setGeometry(QtCore.QRect(200, 310, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelmail1.setFont(font)
        self.labelmail1.setStyleSheet("#labelmail1{\n"
" color:blue;\n"
"font-size:15px;\n"
"}")
        self.labelmail1.setText("")
        self.labelmail1.setObjectName("labelmail1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelid.setText(_translate("Form", "ERP-ID :"))
        self.labelname.setText(_translate("Form", "Name :"))
        self.labelroll.setText(_translate("Form", "Roll No :"))
        self.labelgen.setText(_translate("Form", "Gender :"))
        self.labelno.setText(_translate("Form", "Phone no :"))
        self.labeldo.setText(_translate("Form", "DOB :"))
        self.labelcourse.setText(_translate("Form", "Course :"))
        self.labelmail.setText(_translate("Form", "e-mail :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formview1()
    ui.setupUiview1(Form)
    Form.show()
    sys.exit(app.exec_())

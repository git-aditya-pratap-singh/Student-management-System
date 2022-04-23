# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formuser(object):
    def setupUiuser(self, Form):
        Form.setObjectName("Form")
        Form.resize(868, 592)

        self.framelgmain = QtWidgets.QFrame(Form)
        self.framelgmain.setGeometry(QtCore.QRect(0, 0, 868, 591))
        self.framelgmain.setStyleSheet("")
        self.framelgmain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framelgmain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framelgmain.setObjectName("framelgmain")
        self.framelgmain.setStyleSheet("#framelgmain{\n"
                                 "  background:#efebff;\n"
                                 "  border-radius:2px;\n"
                                 "}")


        self.framelogmain2 = QtWidgets.QFrame(self.framelgmain)
        self.framelogmain2.setGeometry(QtCore.QRect(0, 0, 868, 591))
        self.framelogmain2.setStyleSheet("")
        self.framelogmain2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framelogmain2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framelogmain2.setObjectName("framelogmain2")
        self.frame = QtWidgets.QFrame(self.framelogmain2)
        self.frame.setGeometry(QtCore.QRect(70, 80, 281, 41))
        self.frame.setStyleSheet("#frame{\n"
"  background:#3b19ff;\n"
"  border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 221, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("#label_8{\n"
"  color:#fff;\n"
"  font-size:25px;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(self.framelogmain2)
        self.frame_2.setGeometry(QtCore.QRect(70, 140, 281, 191))
        self.frame_2.setStyleSheet("#frame_2{\n"
" background:#fff;\n"
" border-radius:10px;\n"
"  box-shadow: 0 0 5px 5px #8d8e8d;\n"
"  border: 2px solid #11d09a;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(90, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("#label_9{\n"
" color:#10a0ff;\n"
" font-size:35px;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(30, 100, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("#label_10{\n"
" color:#10a0ff;\n"
" font-size:35px;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.frame_3 = QtWidgets.QFrame(self.framelogmain2)
        self.frame_3.setGeometry(QtCore.QRect(500, 80, 281, 41))
        self.frame_3.setStyleSheet("#frame_3{\n"
"  background:#00ff7f;\n"
"  border-radius:10px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("#label_11{\n"
"  color:#fff;\n"
"  font-size:25px;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.frame_4 = QtWidgets.QFrame(self.framelogmain2)
        self.frame_4.setGeometry(QtCore.QRect(500, 140, 281, 191))
        self.frame_4.setStyleSheet("#frame_4{\n"
" background:#fff;\n"
" border-radius:10px;\n"
"  box-shadow: 0 0 5px 5px #8d8e8d;\n"
"  border: 2px solid #11d09a;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("#label_12{\n"
" font-size:22px;\n"
"color:#3527ff;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("#label_13{\n"
" font-size:22px;\n"
"color:#3527ff;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(10, 130, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("#label_14{\n"
" font-size:22px;\n"
"color:#3527ff;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.labelname = QtWidgets.QLabel(self.frame_4)
        self.labelname.setGeometry(QtCore.QRect(90, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelname.setFont(font)
        self.labelname.setStyleSheet("#labelname{\n"
" font-size:22px;\n"
"color:#3527ff;\n"
"}")
        self.labelname.setText("")
        self.labelname.setObjectName("labelname")
        self.labelid = QtWidgets.QLabel(self.frame_4)
        self.labelid.setGeometry(QtCore.QRect(110, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelid.setFont(font)
        self.labelid.setStyleSheet("#labelid{\n"
" font-size:22px;\n"
"color:#3527ff;\n"
"}")
        self.labelid.setText("")
        self.labelid.setObjectName("labelid")
        self.labelrole = QtWidgets.QLabel(self.frame_4)
        self.labelrole.setGeometry(QtCore.QRect(90, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelrole.setFont(font)
        self.labelrole.setStyleSheet("#labelrole{\n"
" font-size:22px;\n"
"color:#3527ff;\n"
"}")
        self.labelrole.setText("")
        self.labelrole.setObjectName("labelrole")
        self.framedeveloper = QtWidgets.QFrame(self.framelogmain2)
        self.framedeveloper.setGeometry(QtCore.QRect(70, 360, 711, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        self.framedeveloper.setFont(font)
        self.framedeveloper.setStyleSheet("#framedeveloper{\n"
" background:#1cffda;\n"
" border-radius:10px;\n"
"}")
        self.framedeveloper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framedeveloper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framedeveloper.setObjectName("framedeveloper")
        self.label_15 = QtWidgets.QLabel(self.framedeveloper)
        self.label_15.setGeometry(QtCore.QRect(280, 0, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("#label_15{\n"
"  color:#fff;\n"
"  font-size:25px;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.textBrowser = QtWidgets.QTextBrowser(self.framelogmain2)
        self.textBrowser.setGeometry(QtCore.QRect(70, 430, 711, 121))
        self.textBrowser.setStyleSheet("#textBrowser{\n"
" background:#fff;\n"
" border-radius:10px;\n"
"  box-shadow: 0 0 5px 5px #8d8e8d;\n"
"  border: 2px solid #11d09a;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "  Total Students"))
        self.label_9.setText(_translate("Form", "Total"))
        self.label_10.setText(_translate("Form", "[0] Students"))
        self.label_11.setText(_translate("Form", "   Current User"))
        self.label_12.setText(_translate("Form", "Name :"))
        self.label_13.setText(_translate("Form", "User ID :"))
        self.label_14.setText(_translate("Form", "Role :"))
        self.label_15.setText(_translate("Form", "Developer"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#00007f;\">         Developed by - Aditya pratap singh</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">                                  email- singhadityapratap272@gmail.com</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">                                           follow on facebook &amp; Instagram</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui5 = Ui_Formuser()
    ui5.setupUiuser(Form)
    Form.show()
    sys.exit(app.exec_())

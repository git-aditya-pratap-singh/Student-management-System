# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maincode2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from addstudent3 import Ui_Form3
from manage import Ui_Formmanage
from viewstudent import Ui_Formview
from registration import Ui_Formaadi
from password import Ui_Formword
from details import Ui_Formd



import sqlite3
conn=sqlite3.connect('logindata.db')
import sys

class Ui_Form(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(1002, 668)
        self.mainframe = QtWidgets.QFrame(Form)
        self.mainframe.setGeometry(QtCore.QRect(0, 0, 1002, 668))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.mainframe.setFont(font)
        self.mainframe.setStyleSheet("#mainframe{\n"
" background:#edebff;\n"
"}")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.menuframe = QtWidgets.QFrame(self.mainframe)
        self.menuframe.setGeometry(QtCore.QRect(0, 0, 151, 668))
        self.menuframe.setStyleSheet("#menuframe{\n"
" background:#384b50;\n"
"}")
        self.menuframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuframe.setObjectName("menuframe")
        self.toolButton = QtWidgets.QToolButton(self.menuframe)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 151, 102))
        self.toolButton.setStyleSheet("#toolButton{\n"
"  background:#384b50;\n"
"}\n"                                     
"#toolButton:hover{\n"
" background:#fff;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("adminn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(70, 70))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.menuframe)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 100, 151, 100))
        self.toolButton_2.setStyleSheet("#toolButton_2{\n"
"  background:#384b50;\n"
"}\n"
"#toolButton_2:hover{\n"
" background:#fff;\n"
"}")
        self.toolButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graduate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.menuframe)
        self.toolButton_3.setGeometry(QtCore.QRect(0, 190, 151, 102))
        self.toolButton_3.setStyleSheet("#toolButton_3{\n"
"  background:#384b50;\n"
" \n"
"}\n"
"#toolButton_3:hover{\n"
" background:#fff;\n"
"\n"
"}")
        self.toolButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("networking.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.menuframe)
        self.toolButton_4.setGeometry(QtCore.QRect(0, 290, 151, 102))
        self.toolButton_4.setStyleSheet("#toolButton_4{\n"
"  background:#384b50;\n"
"}\n"
"#toolButton_4:hover{\n"
" background:#fff;\n"
"}")
        self.toolButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("cinema.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.menuframe)
        self.toolButton_5.setGeometry(QtCore.QRect(0, 390, 151, 100))
        self.toolButton_5.setStyleSheet("#toolButton_5{\n"
"  background:#384b50;\n"
"}\n"
"#toolButton_5:hover{\n"
" background:#fff;\n"
"}")
        self.toolButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("viewers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.menuframe)
        self.toolButton_6.setGeometry(QtCore.QRect(0, 480, 151, 100))
        self.toolButton_6.setStyleSheet("#toolButton_6{\n"
"  background:#384b50;\n"
"}\n"
"#toolButton_6:hover{\n"
" background:#fff;\n"
"}")
        self.toolButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.menuframe)
        self.toolButton_7.setGeometry(QtCore.QRect(0, 570, 151, 102))
        self.toolButton_7.setStyleSheet("#toolButton_7{\n"
"  background:#384b50;\n"
"}\n"
"#toolButton_7:hover{\n"
" background:#fff;\n"
"}")
        self.toolButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("power-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_7.setObjectName("toolButton_7")
        self.label = QtWidgets.QLabel(self.menuframe)
        self.label.setGeometry(QtCore.QRect(40, 80, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
" color:#fff;\n"
" font-family:Gill Sans Extrabold, sans-serif;\n"
" font-size:19px;\n"
"}\n"
"#label:hover{\n"
" color:black;\n"
"}\n"
"")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.menuframe)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
" color:#fff;\n"
" font-family:Gill Sans Extrabold, sans-serif;\n"
" font-size:19px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.menuframe)
        self.label_3.setGeometry(QtCore.QRect(40, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
" color:#fff;\n"
"  font-family:Gill Sans Extrabold, sans-serif;\n"
" font-size:19px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.menuframe)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
" color:#fff;\n"
" font-family:Gill Sans Extrabold, sans-serif;\n"
" font-size:19px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.menuframe)
        self.label_5.setGeometry(QtCore.QRect(40, 460, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("#label_5{\n"
" color:#fff;\n"
" font-family:Gill Sans Extrabold, sans-serif;\n"
" font-size:19px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.menuframe)
        self.label_6.setGeometry(QtCore.QRect(40, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("#label_6{\n"
" color:#fff;\n"
" font-family:Gill Sans Extrabold, sans-serif;\n"
" font-size:19px;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.menuframe)
        self.label_7.setGeometry(QtCore.QRect(30, 520, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("#label_7{\n"
" color:#fff;\n"
" font-family:Gill Sans Extrabold, sans-serif;\n"
" font-size:19px;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.dashboardframe = QtWidgets.QFrame(self.mainframe)
        self.dashboardframe.setGeometry(QtCore.QRect(150, 0, 861, 80))
        self.dashboardframe.setStyleSheet("#dashboardframe{\n"
" background:#ff007f;\n"
"}")
        self.dashboardframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboardframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboardframe.setObjectName("dashboardframe")
        self.labeldash = QtWidgets.QLabel(self.dashboardframe)
        self.labeldash.setGeometry(QtCore.QRect(230, 20, 371, 51))
        self.labeldash.setStyleSheet("#labeldash{\n"
" color:#fff;\n"
" font-family:sens-serif;\n"
" font: 85 25pt \"Script MT Bold\";\n"
"}")
        self.labeldash.setObjectName("labeldash")


        self.framelogmain = QtWidgets.QFrame(self.mainframe)
        self.framelogmain.setGeometry(QtCore.QRect(150, 80, 861, 591))
        self.framelogmain.setStyleSheet("")
        self.framelogmain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framelogmain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framelogmain.setObjectName("framelogmain")
        self.frame = QtWidgets.QFrame(self.framelogmain)
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
        self.frame_2 = QtWidgets.QFrame(self.framelogmain)
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
        self.frame_3 = QtWidgets.QFrame(self.framelogmain)
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
        self.frame_4 = QtWidgets.QFrame(self.framelogmain)
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
        self.framedeveloper = QtWidgets.QFrame(self.framelogmain)
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
        self.textBrowser = QtWidgets.QTextBrowser(self.framelogmain)
        self.textBrowser.setGeometry(QtCore.QRect(70, 430, 711, 121))
        self.textBrowser.setStyleSheet("#textBrowser{\n"
" background:#fff;\n"
" border-radius:10px;\n"
"  box-shadow: 0 0 5px 5px #8d8e8d;\n"
"  border: 2px solid #11d09a;\n"
"}")

        '''conn3 = sqlite3.connect("studentinfo.db")
        cursor = conn3.cursor()
        sql4 = "SELECT * FROM info"
        cursor.execute(sql4)
        conn3.commit()
        self.ax = cursor.fetchone()
        try:
             if self.ax != None:
                  self.label_10.setText("["+self.ax[8]+"] Students")
        except:
                print()

        self.textBrowser.setObjectName("textBrowser")'''
        self.frame_n = QtWidgets.QFrame(self.frame_2)
        self.frame_n.setGeometry(QtCore.QRect(65, 35, 150, 120))
        self.frame_n.setStyleSheet("#frame_n{\n"
                                   " background:(0,0,0,0.6);\n"
                                   " border: 0px;\n"
                                   " image:url(\"graduate.png\");\n"
                                   "}")
        self.frame_n.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_n.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_n.setObjectName("frame_n")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.toolButton_2.clicked.connect(self.add_data)
        self.toolButton_3.clicked.connect(self.manage_data)
        self.toolButton_4.clicked.connect(self.show_data)
        self.toolButton_6.clicked.connect(self.change)
        self.toolButton_5.clicked.connect(self.detail)
        self.toolButton.clicked.connect(self.admin_data)
        self.toolButton_7.clicked.connect(self.cut)
        #self.login.pressed.connect(self.check)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "Admin"))
        self.toolButton_7.setShortcut(_translate("Form", "Ctrl+C"))
        self.label.setText(_translate("Form", "Admin"))
        self.label_2.setText(_translate("Form", "Add Student"))
        self.label_3.setText(_translate("Form", "Manage"))
        self.label_4.setText(_translate("Form", "View Students"))
        self.label_5.setText(_translate("Form", "view all"))
        self.label_6.setText(_translate("Form", "Change password"))
        self.label_7.setText(_translate("Form", "Password"))
        self.labeldash.setText(_translate("Form", "    DASHBOARD"))
        self.label_8.setText(_translate("Form", "      Students"))
        #self.label_9.setText(_translate("Form", "Total"))
        #self.label_10.setText(_translate("Form", " Students"))
        self.label_11.setText(_translate("Form", "    Current User"))
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

    def add_data(self):
            self.win=QtWidgets.QFrame(self.framelogmain)
            self.ui= Ui_Form3()
            self.ui.setupUiadd(self.win)
            self.win.show()
            self.framedeveloper.setVisible(False)
            self.label_15.setVisible(False)
            self.labelrole.setVisible(False)

    def manage_data(self):
            self.var=QtWidgets.QFrame(self.framelogmain)
            self.ui = Ui_Formmanage()
            self.ui.setupUimanage(self.var)
            self.var.show()

    def show_data(self):
            self.win2=QtWidgets.QFrame(self.framelogmain)
            self.ui = Ui_Formview()
            self.ui.setupUiview(self.win2)
            self.win2.show()

    def change(self):
            self.wind=QtWidgets.QFrame(self.framelogmain)
            self.ui = Ui_Formword()
            self.ui.setupUiword(self.wind)
            self.wind.show()

    def admin_data(self):
            self.windows=QtWidgets.QFrame(self.framelogmain)
            self.ui=Ui_Formaadi()
            self.ui.setupUiaadi(self.windows)
            self.windows.show()

    def detail(self):
            self.windows2= QtWidgets.QFrame(self.framelogmain)
            self.ui = Ui_Formd()
            self.ui.setupUi(self.windows2)
            self.windows2.show()

    def cut(self):
            sys.exit()




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi2(Form)
    Form.show()
    sys.exit(app.exec_())

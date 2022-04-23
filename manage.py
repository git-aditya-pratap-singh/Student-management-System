# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from update import Ui_Formupdate
from delete import Ui_Formdelete

class Ui_Formmanage(object):
    def setupUimanage(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 595)
        self.frametop = QtWidgets.QFrame(Form)
        self.frametop.setGeometry(QtCore.QRect(0, 0, 861, 121))
        self.frametop.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frametop.setStyleSheet("#frametop{\n"
" background:#fff;\n"
"}")
        self.frametop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frametop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frametop.setObjectName("frametop")
        self.pushButtonupdate = QtWidgets.QPushButton(self.frametop)
        self.pushButtonupdate.setGeometry(QtCore.QRect(40, 26, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonupdate.setFont(font)
        self.pushButtonupdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonupdate.setStyleSheet("#pushButtonupdate{\n"
"  background:#5500ff;\n"
" border-radius:20px;\n"
" font-size:25px;\n"
" color:#fff;\n"
"}\n"
"#pushButtonupdate:hover{\n"
" background:#158eff;\n"
"    border: 2px solid #11d09a;\n"
"     transition: .4s;\n"
"\n"
"     \n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bt3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonupdate.setIcon(icon)
        self.pushButtonupdate.setIconSize(QtCore.QSize(70, 70))
        self.pushButtonupdate.setObjectName("pushButtonupdate")
        self.pushButtondelete = QtWidgets.QPushButton(self.frametop)
        self.pushButtondelete.setGeometry(QtCore.QRect(570, 30, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtondelete.setFont(font)
        self.pushButtondelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtondelete.setStyleSheet("#pushButtondelete{\n"
"   background:#07ff98;\n"
" border-radius:20px;\n"
" font-size:25px;\n"
" color:#fff;\n"
"}\n"
"#pushButtondelete:hover{\n"
" background:#07ff98;\n"
"    border: 2px solid #11d09a;\n"
"     transition: .4s;\n"
"\n"
"     \n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bt5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtondelete.setIcon(icon1)
        self.pushButtondelete.setIconSize(QtCore.QSize(70, 70))
        self.pushButtondelete.setObjectName("pushButtondelete")
        self.frame = QtWidgets.QFrame(self.frametop)
        self.frame.setGeometry(QtCore.QRect(370, 9, 121, 101))
        self.frame.setStyleSheet("#frame{\n"
" background:;\n"
" image:url(index.jfif);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.framebottom = QtWidgets.QFrame(Form)
        self.framebottom.setGeometry(QtCore.QRect(0, 110, 861, 491))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.framebottom.setFont(font)
        self.framebottom.setStyleSheet("#framebottom{\n"
" background:;\n"
" image:url(4k-wallpapers-for-pc-free-download-4k-high-resolution-wallpaper.jpg);\n"
" filter: blur(25px);\n"
"}")
        self.framebottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framebottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framebottom.setObjectName("framebottom")
        self.frame1 = QtWidgets.QFrame(self.framebottom)
        self.frame1.setGeometry(QtCore.QRect(120, 60, 611, 371))
        self.frame1.setStyleSheet("#frame1{\n"
"background:rgba(0,0,0,0.6);\n"
"border-radius:40px;\n"
"}")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.frame_2 = QtWidgets.QFrame(self.frame1)
        self.frame_2.setGeometry(QtCore.QRect(30, 10, 81, 61))
        self.frame_2.setStyleSheet("#frame_2{\n"
" background:(0,0,0,0.6);\n"
" background:;\n"
" image:url(\"graduate.png\");\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.labelabout = QtWidgets.QLabel(self.frame1)
        self.labelabout.setGeometry(QtCore.QRect(120, 20, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelabout.setFont(font)
        self.labelabout.setStyleSheet("#labelabout{\n"
" color:#ff0004;\n"
" font-size:35px;\n"
"}")
        self.labelabout.setObjectName("labelabout")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(30, 100, 551, 31))
        self.label.setStyleSheet("#label{\n"
" color:#fff;\n"
" font-size:20px;\n"
" }")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 331, 31))
        self.label_2.setStyleSheet("#label_2{\n"
" color:#fff;\n"
" font-size:20px;\n"
" }")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setGeometry(QtCore.QRect(30, 169, 541, 31))
        self.label_3.setStyleSheet("#label_3{\n"
" color:#fff;\n"
" font-size:20px;\n"
" }")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setGeometry(QtCore.QRect(30, 209, 541, 21))
        self.label_4.setStyleSheet("#label_4{\n"
" color:#fff;\n"
" font-size:20px;\n"
" }")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setGeometry(QtCore.QRect(30, 239, 531, 31))
        self.label_5.setStyleSheet("#label_5{\n"
" color:#fff;\n"
" font-size:20px;\n"
" }")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame1)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 531, 41))
        self.label_6.setStyleSheet("#label_6{\n"
" color:#fff;\n"
" font-size:20px;\n"
" }")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame1)
        self.label_7.setGeometry(QtCore.QRect(30, 305, 531, 31))
        self.label_7.setStyleSheet("#label_7{\n"
" color:#fff;\n"
" font-size:20px;\n"
" }")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButtonupdate.clicked.connect(self.update_data)
        self.pushButtondelete.clicked.connect(self.delete_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonupdate.setText(_translate("Form", " Update"))
        self.pushButtondelete.setText(_translate("Form", "Delete"))
        self.labelabout.setText(_translate("Form", "About us"))
        self.label.setText(_translate("Form", "A Student Management System helps a school manage data"))
        self.label_2.setText(_translate("Form", "communications, and scheduling."))
        self.label_3.setText(_translate("Form", "A School system generates and uses a large amount of data"))
        self.label_4.setText(_translate("Form", "this data must be communicated appropriately to students,"))
        self.label_5.setText(_translate("Form", "faculty,and parents. Some Students Management System"))
        self.label_6.setText(_translate("Form", "are designed to serve all of a school,s data manage needs."))
        self.label_7.setText(_translate("Form", "other Student Management System are specialized."))


    def update_data(self):
        self.root=QtWidgets.QFrame(self.framebottom)
        self.ui = Ui_Formupdate()
        self.ui.setupUiupdate(self.root)
        self.root.show()

    def delete_data(self):
        self.top=QtWidgets.QFrame(self.framebottom)
        self.ui = Ui_Formdelete()
        self.ui.setupUidelete(self.top)
        self.top.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formmanage()
    ui.setupUimanage(Form)
    Form.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addstudent3.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_Form3(object):

    def setupUiadd(self, Form):
        Form.setObjectName("Form")
        Form.resize(858, 593)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 860, 591))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame.setStyleSheet("#frame{\n"
" background:#ffffff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.labeladdstudent = QtWidgets.QLabel(self.frame)
        self.labeladdstudent.setGeometry(QtCore.QRect(40, 20, 381, 51))
        self.labeladdstudent.setMinimumSize(QtCore.QSize(55, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labeladdstudent.setFont(font)
        self.labeladdstudent.setStyleSheet("#labeladdstudent{\n"
" color:#0000ff;\n"
"font-size:50px;\n"                                           
"}")
        self.labeladdstudent.setObjectName("labeladdstudent")
        self.frame_line = QtWidgets.QFrame(self.frame)
        self.frame_line.setGeometry(QtCore.QRect(10, 80, 841, 5))
        self.frame_line.setStyleSheet("#frame_line{\n"
" background:#ff2f89;\n"
"}")
        self.frame_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_line.setObjectName("frame_line")
        self.labelid = QtWidgets.QLabel(self.frame)
        self.labelid.setGeometry(QtCore.QRect(180, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelid.setStyleSheet("#labelid{\n"
                                          " color:black;\n"
                                          "font-size:20px;\n"
                                          "}")
        self.labelid.setFont(font)
        self.labelid.setObjectName("labelid")
        self.lineEditid = QtWidgets.QLineEdit(self.frame)
        self.lineEditid.setGeometry(QtCore.QRect(310, 130, 381, 31))
        self.lineEditid.setStyleSheet("#lineEditid{\n"
" border-radius:5px;\n"
" color:black;\n"
" font-size:18px;\n"
" border: 2px solid  #534951;\n"
"}\n"
"#lineEditid:hover{\n"
"  background:#e5f4ff;\n"
"}")
        self.lineEditid.setObjectName("lineEditid")
        self.labelname = QtWidgets.QLabel(self.frame)
        self.labelname.setGeometry(QtCore.QRect(180, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelname.setStyleSheet("#labelname{\n"
                                   " color:black;\n"
                                   "font-size:20px;\n"
                                   "}")
        self.labelname.setFont(font)
        self.labelname.setObjectName("labelname")
        self.label_rollno = QtWidgets.QLabel(self.frame)
        self.label_rollno.setGeometry(QtCore.QRect(180, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_rollno.setStyleSheet("#label_rollno{\n"
                                   " color:black;\n"
                                   "font-size:20px;\n"
                                   "}")
        self.label_rollno.setFont(font)
        self.label_rollno.setObjectName("label_rollno")
        self.lineEditname = QtWidgets.QLineEdit(self.frame)
        self.lineEditname.setGeometry(QtCore.QRect(310, 200, 381, 31))
        self.lineEditname.setStyleSheet("#lineEditname{\n"
" border-radius:5px;\n"
" color:black;\n"
" font-size:18px;\n"
" border: 2px solid  #534951;\n"
"}\n"
"#lineEditname:hover{\n"
"  background:#e5f4ff;\n"
"}")
        self.lineEditname.setObjectName("lineEditname")
        self.lineEditrollno = QtWidgets.QLineEdit(self.frame)
        self.lineEditrollno.setGeometry(QtCore.QRect(310, 270, 381, 31))
        self.lineEditrollno.setStyleSheet("#lineEditrollno{\n"
" border-radius:5px;\n"
" color:black;\n"
" font-size:18px;\n"
" border: 2px solid  #534951;\n"
"}\n"
"#lineEditrollno:hover{\n"
"  background:#e5f4ff;\n"
"}")
        self.lineEditrollno.setObjectName("lineEditrollno")
        self.labelgender = QtWidgets.QLabel(self.frame)
        self.labelgender.setGeometry(QtCore.QRect(180, 340, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelgender.setStyleSheet("#labelgender{\n"
                                   " color:black;\n"
                                   "font-size:20px;\n"
                                   "}")
        self.labelgender.setFont(font)
        self.labelgender.setObjectName("labelgender")
        self.radioButtonmale = QtWidgets.QRadioButton(self.frame)
        self.radioButtonmale.setGeometry(QtCore.QRect(310, 340, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)


        self.radioButtonmale.setFont(font)
        self.radioButtonmale.setStyleSheet("#radioButtonmale{\n"
" color:blue;\n"
 "font-size:15px;\n"
"}")
        self.radioButtonmale.setObjectName("radioButtonmale")

        self.radioButtonmale.toggled.connect(self.maleselected)

        self.radioButtonfemale = QtWidgets.QRadioButton(self.frame)
        self.radioButtonfemale.setGeometry(QtCore.QRect(390, 340, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.radioButtonfemale.setFont(font)
        self.radioButtonfemale.setStyleSheet("#radioButtonfemale{\n"
"  color:blue;\n"
    "font-size:15px;\n"                                           
"}")
        self.radioButtonfemale.setObjectName("radioButtonfemale")

        self.radioButtonfemale.toggled.connect(self.femaleselected)

        self.labelDOB = QtWidgets.QLabel(self.frame)
        self.labelDOB.setGeometry(QtCore.QRect(500, 340, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelDOB.setStyleSheet("#labelDOB{\n"
                                   " color:black;\n"
                                   "font-size:20px;\n"
                                   "}")
        self.labelDOB.setFont(font)
        self.labelDOB.setObjectName("labelDOB")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(570, 340, 121, 22))
        self.dateEdit.setStyleSheet("#dateEdit{\n"
" border-radius:5px;\n"
" color:black;\n"
" font-size:18px;\n"
" border: 1px solid  #534951;\n"
"}")
        self.dateEdit.setObjectName("dateEdit")
        self.labelcourse = QtWidgets.QLabel(self.frame)
        self.labelcourse.setGeometry(QtCore.QRect(180, 400, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelcourse.setStyleSheet("#labelcourse{\n"
                                   " color:black;\n"
                                   "font-size:20px;\n"
                                   "}")
        self.labelcourse.setFont(font)
        self.labelcourse.setObjectName("labelcourse")
        self.lineEditcourse = QtWidgets.QLineEdit(self.frame)
        self.lineEditcourse.setGeometry(QtCore.QRect(310, 390, 113, 31))
        self.lineEditcourse.setStyleSheet("#lineEditcourse{\n"
" border-radius:5px;\n"
" color:black;\n"
" font-size:18px;\n"
" border: 2px solid  #534951;\n"
"}\n"
"#lineEditcourse:hover{\n"
"  background:#e5f4ff;\n"
"}")
        self.lineEditcourse.setObjectName("lineEditcourse")
        self.lineEditphone_no = QtWidgets.QLineEdit(self.frame)
        self.lineEditphone_no.setGeometry(QtCore.QRect(440, 390, 251, 31))
        self.lineEditphone_no.setStyleSheet("#lineEditphone_no{\n"
" border-radius:5px;\n"
" color:black;\n"
" font-size:18px;\n"
" border: 2px solid  #534951;\n"
"}\n"
"#lineEditphone_no:hover{\n"
"  background:#e5f4ff;\n"
"\n"
"}")
        self.lineEditphone_no.setObjectName("lineEditphone_no")
        self.labelmail = QtWidgets.QLabel(self.frame)
        self.labelmail.setGeometry(QtCore.QRect(180, 460, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelmail.setStyleSheet("#labelmail{\n"
                                   " color:black;\n"
                                   "font-size:20px;\n"
                                   "}")
        self.labelmail.setFont(font)
        self.labelmail.setObjectName("labelmail")
        self.lineEditmail = QtWidgets.QLineEdit(self.frame)
        self.lineEditmail.setGeometry(QtCore.QRect(310, 460, 381, 31))
        self.lineEditmail.setStyleSheet("#lineEditmail{\n"
" border-radius:5px;\n"
" color:black;\n"
" font-size:18px;\n"
" border: 2px solid  #534951;\n"
"}\n"
"#lineEditmail:hover{\n"
"  background:#e5f4ff;\n"
"\n"
"}")
        self.lineEditmail.setObjectName("lineEditmail")
        self.pushButtonsubmit = QtWidgets.QPushButton(self.frame)
        self.pushButtonsubmit.setGeometry(QtCore.QRect(180, 520, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonsubmit.setFont(font)
        self.pushButtonsubmit.setStyleSheet("#pushButtonsubmit{\n"
" border-radius:5px;\n"
" background:#5500ff;\n"
" border: 2px solid #fff;\n"
" color:#fff;\n"
"}\n"
"#pushButtonsubmit:hover{\n" 
" background:#617eff;\n"
"}")
        self.pushButtonsubmit.setObjectName("pushButtonsubmit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButtonsubmit.clicked.connect(self.add_data)

    def maleselected(self, selected):
        if selected:
            self.c=self.radioButtonmale.text()
            self.sc=self.c


    def femaleselected(self, selected):
        if selected:
            self.b = self.radioButtonfemale.text()
            self.sc=self.b




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labeladdstudent.setText(_translate("Form", "Add Students"))
        self.labelid.setText(_translate("Form", "ERP-ID :"))
        self.labelname.setText(_translate("Form", "Name :"))
        self.label_rollno.setText(_translate("Form", "Roll-no :"))
        self.labelgender.setText(_translate("Form", "Gender :"))
        self.radioButtonmale.setText(_translate("Form", "Male"))
        self.radioButtonfemale.setText(_translate("Form", "Female"))
        self.labelDOB.setText(_translate("Form", "DOB :"))
        self.labelcourse.setText(_translate("Form", "Course :"))
        self.lineEditphone_no.setPlaceholderText(_translate("Form", " Phone no"))
        self.labelmail.setText(_translate("Form", "e-mail :"))
        self.pushButtonsubmit.setText(_translate("Form", "Submit"))






    def add_data(self):


        #add data

        id=self.lineEditid.text()
        name=self.lineEditname.text()
        rollno=self.lineEditrollno.text()


        det=self.dateEdit.text()
        course=self.lineEditcourse.text()
        pho=self.lineEditphone_no.text()
        mail=self.lineEditmail.text()

        #fetch data in database

        data=sqlite3.connect('studentinfo.db')
        conn22=data.cursor()

        conn22.execute("INSERT INTO info (ERP_ID,Name,Roll_no,Gender,Phone_no,Course,DOB,e_mail) values(?,?,?,?,?,?,?,?)",(id,
                                                                                                                name,
                                                                                                                rollno,self.sc,pho,course,det,mail))
        data.commit()


        self.lineEditid.clear()
        self.lineEditname.clear()
        self.lineEditrollno.clear()

        self.lineEditcourse.clear()
        self.lineEditphone_no.clear()
        self.lineEditmail.clear()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUiadd(Form)
    Form.show()
    sys.exit(app.exec_())

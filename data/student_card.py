# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton


class Ui_add_student(object):
    def setupUi(self, add_student):
        add_student.setObjectName("add_student")
        add_student.resize(251, 296)
        add_student.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalLayout = QtWidgets.QHBoxLayout(add_student)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(add_student)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.label = QtWidgets.QLabel(add_student)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(add_student)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(add_student)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(add_student)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(add_student)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(add_student)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(add_student)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(add_student)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(add_student)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(add_student)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lineEdit_6)
        self.label_6 = QtWidgets.QLabel(add_student)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(add_student)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lineEdit_7)
        self.label_7 = QtWidgets.QLabel(add_student)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(add_student)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(add_student)

    @pyqtSlot()
    def on_cl(self):
        print("somthing")
    def retranslateUi(self, add_student):
        _translate = QtCore.QCoreApplication.translate
        add_student.setWindowTitle(_translate("add_student", "כרטיס חניך"))
        self.label.setText(_translate("add_student", "שם פרטי"))
        self.label_2.setText(_translate("add_student", "שם משפחה"))
        self.label_3.setText(_translate("add_student", "תעודת זהות"))
        self.label_4.setText(_translate("add_student", "מספר טלפון"))
        self.label_5.setText(_translate("add_student", "כיתה"))
        self.label_6.setText(_translate("add_student", "מין"))
        self.label_7.setText(_translate("add_student", "גיל"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_student = QtWidgets.QDialog()
    ui = Ui_add_student()
    ui.setupUi(add_student)
    add_student.show()
    sys.exit(app.exec_())
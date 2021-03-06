from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QInputDialog


class Ui_Employee_card(object):
    def setupUi(self, Employee_card):
        Employee_card.setObjectName("Employee_card")
        Employee_card.resize(308, 326)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Employee_card)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit.setObjectName("lineEdit")
        name = self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.label = QtWidgets.QLabel(Employee_card)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(Employee_card)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(Employee_card)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(Employee_card)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(Employee_card)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lineEdit_6)
        self.label_6 = QtWidgets.QLabel(Employee_card)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lineEdit_7)
        self.label_7 = QtWidgets.QLabel(Employee_card)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(Employee_card)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lineEdit_8)
        self.label_8 = QtWidgets.QLabel(Employee_card)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.buttonBox = QtWidgets.QDialogButtonBox(Employee_card)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(Employee_card)
        self.buttonBox.accepted.connect(Employee_card.accept) # type: ignore

        QtCore.QMetaObject.connectSlotsByName(Employee_card)
    @pyqtSlot()
    def accept(self,name):
        print(name)
    def retranslateUi(self, Employee_card):
        _translate = QtCore.QCoreApplication.translate
        Employee_card.setWindowTitle(_translate("Employee_card", "Employee_card"))
        self.label.setText(_translate("Employee_card", "???? ????????"))
        self.label_2.setText(_translate("Employee_card", "???? ??????????"))
        self.label_3.setText(_translate("Employee_card", "?????????? ????????"))
        self.label_4.setText(_translate("Employee_card", "???????? ??????????"))
        self.label_5.setText(_translate("Employee_card", "??????????"))
        self.label_6.setText(_translate("Employee_card", "??????"))
        self.label_7.setText(_translate("Employee_card", "?????? ??????????"))
        self.label_8.setText(_translate("Employee_card", "??????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Employee_card = QtWidgets.QDialog()
    ui = Ui_Employee_card()
    ui.setupUi(Employee_card)
    Employee_card.show()
    sys.exit(app.exec_())

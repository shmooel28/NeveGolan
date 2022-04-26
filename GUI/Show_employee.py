from PyQt5.QtWidgets import QDialog, QStyle, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton

from GUI import App


class Show_employee(QDialog):
    def __init__(self, mainSystem, parent=None):
        super().__init__(parent)
        self.setWindowTitle('אנשי צוות')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(mainSystem.count_employee+1)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("first name"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("last name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("phone number"))
        self.tableWidget.move(0, 0)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.pushButton = QPushButton()
        self.pushButton.setText('חזור')
        self.pushButton.clicked.connect(self.goMainWindow)
        self.layout.addWidget(self.pushButton)

        self.setLayout(self.layout)
        # Show widget
        self.show()


    def goMainWindow(self):
        self.cams = App(self.mainSystem)
        self.cams.show()
        self.close()
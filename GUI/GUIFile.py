from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidget, QWidget, QListWidgetItem, QHBoxLayout


class GUIFile(QWidget):
    def __init__(self,algo):
        self.algo = algo
        super().__init__()
        self.title = 'מערכת לניהול נווה גולן - תפריט'
        self.left = 0
        self.top = 0
        self.width = 1280
        self.height = 800
        self.my_list = QListWidget()
        self.my_list.setAcceptDrops(True)
        self.my_list.setDragEnabled(True)
        self.setGeometry(300,350,500,300)
        self.my_list.setViewMode(QListWidget.IconMode)
        self.box = QHBoxLayout()
        self.box.addWidget(self.my_list)
        self.setAcceptDrops(True)
        self.setLayout(self.box)
        for l in self.algo.main_system.link:
            if 'doc' in l[1]:
                QListWidgetItem(QIcon("docx.png"), l[1], self.my_list)
                # self.my_list.insertItem(1,widget)
            elif 'pdf' in l[1]:
                QListWidgetItem(QIcon("PDF.png"), l[1], self.my_list)
            elif 'txt' in l[1]:
                QListWidgetItem(QIcon("txt.png"), l[1], self.my_list)
            elif '.pptx' in l[1]:
                QListWidgetItem(QIcon("ppt.png"), l[1], self.my_list)
            elif 'xlsx' in l[1]:
                QListWidgetItem(QIcon("xlsx.png"), l[1], self.my_list)
            else:
                widget = QListWidgetItem(QIcon("pythonicon.png"), l[1])
                self.my_list.insertItem(1, widget)
        #self.initUI()

    #def initUI(self):

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self,event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    self.algo.main_system.link.append((str(url.toLocalFile()),str(url.fileName())))

                else:
                    self.algo.main_system.link.append((str(url.toString()),str(url.toDisplayString())))
            self.my_list.clear()
            for l in self.algo.main_system.link:
                if 'doc' in l[1]:
                    QListWidgetItem(QIcon("docx.png"), l[1],self.my_list)
                    #self.my_list.insertItem(1,widget)
                elif 'pdf' in l[1]:
                    QListWidgetItem(QIcon("PDF.png"), l[1],self.my_list)
                elif 'txt' in l[1]:
                    QListWidgetItem(QIcon("txt.png"), l[1],self.my_list)
                elif '.pptx' in l[1]:
                    QListWidgetItem(QIcon("ppt.png"), l[1],self.my_list)
                elif 'xlsx' in l[1]:
                    QListWidgetItem(QIcon("xlsx.png"), l[1],self.my_list)
                else:
                    widget = QListWidgetItem(QIcon("pythonicon.png"), l[1])
                    self.my_list.insertItem(1, widget)

        else:
            event.ignore()
    def getSelectedItem(self):
        item = QListWidgetItem(self.my_list.currentItem())
        return item.text()
    def keyPressEvent(self, e):  # doesnt work when app is in background
        if e.key() == Qt.Key_Delete:
            temp = self.getSelectedItem()
            for l in self.algo.main_system.link:
                if temp in l:
                    self.algo.main_system.link.remove(l)
                    self.close()
                    self.new_window = GUIFile(self.algo)
                    self.new_window.show()
                    break
            print(1)

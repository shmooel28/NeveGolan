import sys

from PyQt5.QtWidgets import QApplication

from src.Algo import Algo

if __name__ == '__main__':
    first_try = Algo()
    first_try.load_from_json("demo.json")
    app = QApplication(sys.argv)
    ex = App(first_try)
    sys.exit(app.exec_())
from  PyQt5.QtWidgets import QWidget, QApplication
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Curso RPi4"
        self.m = 200
        self.n = 200
        self.alto = 300
        self.ancho = 600
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.m,self.n,self.ancho,self.alto)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())


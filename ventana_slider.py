from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSlider
from PyQt5.QtCore import Qt
import sys

class App(QWidget):
    def __init__(self): #Establece los valores de la ventana
        super().__init__() #Inicializador de la super clase QWidget
        self.title = "Curso RPi4" #Titulo de la ventana
        self.m = 200 #Punto X de inicio de la ventana
        self.n = 200 #Punto Y de inicio de la ventana
        self.alto = 300 #Alto de la ventana
        self.ancho = 600 #Ancho de la ventana
        self.initUI()	#Invoca a la siguiente funcion
    def initUI(self): 	#Coloca los valores a QtWidget
        self.setWindowTitle(self.title)	
        self.setGeometry(self.m,self.n,self.ancho,self.alto)
        s = QSlider(Qt.Horizontal, self)
        s.setMaximum(1024)
        s.setMinimum(0)
        s.setGeometry(50,50,200,30)
        s.valueChanged.connect(self.cambio)
        self.show()
    def cambio(self, value):
        print(value)

if __name__ == "__main__":
    app = QApplication([]) 
    ex = App()
    sys.exit(app.exec_()) #Dicta la duracion de abierta la ventana


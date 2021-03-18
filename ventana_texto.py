from  PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
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
        #Label
        label1 = QLabel("Hola mundo",self) #Texto de label
        label1.move(50,50) #Posicion de label
        #boton
        button = QPushButton("Activar", self) #Texto del boton
        button.move(100, 100) #Posicion del boton
        button.clicked.connect(self.on) #conecta a la accion del boton a un metodo
        self.show() #Muestra la ventana
        
    def on(self): #Accion del boton
        print("Se presionó el boton")

if __name__ == "__main__":
    app = QApplication([]) 
    ex = App()
    sys.exit(app.exec_()) #Dicta la duracion de abierta la ventana


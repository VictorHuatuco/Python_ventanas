from  PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.out)

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
        
        #boton encendido
        button = QPushButton("Encender", self) #Texto del boton
        button.move(20, 80) #Posicion del boton
        button.clicked.connect(self.on) #conecta a la accion del boton a un metodo

        #boton apagado
        button2 = QPushButton("Apagar", self) #Texto del boton
        button2.move(100, 100) #Posicion del boton
        button2.clicked.connect(self.off) #conecta a la accion del boton a un metodo
        
        self.show() #Muestra la ventana

        
    def on(self): #Accion del boton
        GPIO.output(21,True)
        print("Led encendido")
    def off(self): #Accion del boton
        GPIO.output(21,Flase)
        print("Led apagado")

if __name__ == "__main__":
    app = QApplication([]) 
    ex = App()
    sys.exit(app.exec_()) #Dicta la duracion de abierta la ventana


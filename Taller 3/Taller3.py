from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import roboticstoolbox as rtb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from roboticstoolbox import RevoluteDH, DHRobot
from spatialmath.base import tr2rpy
import RPi.GPIO as GPIO
import tempfile
import math
import numpy
import numpy as np
import sys
from inversa_2R import *
from plot_1 import *
from Servos import *
from PyQt5.QtWidgets import QApplication, QTextEdit, QLabel, QDialog, QVBoxLayout, QPushButton
from PyQt5.QtGui import QImage, QPixmap  # Import both QImage and QPixmap

l1 = 7.5
l2 = 8.5

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(743, 911)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 660, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(90, 860, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 780, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Logo = QtWidgets.QLabel(Dialog)
        self.Logo.setGeometry(QtCore.QRect(280, 650, 431, 231))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 740, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 820, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 700, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 50, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Eje_X = QtWidgets.QTextEdit(self.groupBox_2)
        self.Eje_X.setGeometry(QtCore.QRect(50, 30, 71, 31))
        self.Eje_X.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Eje_X.setObjectName("Eje_X")
        self.Eje_Y = QtWidgets.QTextEdit(self.groupBox_2)
        self.Eje_Y.setGeometry(QtCore.QRect(50, 70, 71, 31))
        self.Eje_Y.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Eje_Y.setObjectName("Eje_Y")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.Bot_Posicion = QtWidgets.QPushButton(self.groupBox_2)
        self.Bot_Posicion.setGeometry(QtCore.QRect(150, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bot_Posicion.setFont(font)
        self.Bot_Posicion.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.Bot_Posicion.setObjectName("Bot_Posicion")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 50, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.Gota = QtWidgets.QPushButton(self.groupBox_3)
        self.Gota.setGeometry(QtCore.QRect(20, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Gota.setFont(font)
        self.Gota.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.Gota.setObjectName("Gota")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(480, 50, 241, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.Juan = QtWidgets.QPushButton(self.groupBox_4)
        self.Juan.setGeometry(QtCore.QRect(10, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Juan.setFont(font)
        self.Juan.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.Juan.setObjectName("Juan")
        self.Wendy = QtWidgets.QPushButton(self.groupBox_4)
        self.Wendy.setGeometry(QtCore.QRect(10, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Wendy.setFont(font)
        self.Wendy.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.Wendy.setObjectName("Wendy")
        self.Esteban = QtWidgets.QPushButton(self.groupBox_4)
        self.Esteban.setGeometry(QtCore.QRect(130, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Esteban.setFont(font)
        self.Esteban.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.Esteban.setObjectName("Esteban")
        self.Manuel = QtWidgets.QPushButton(self.groupBox_4)
        self.Manuel.setGeometry(QtCore.QRect(130, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Manuel.setFont(font)
        self.Manuel.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.Manuel.setObjectName("Manuel")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(240, 180, 481, 141))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.Img_Nom = QtWidgets.QLabel(self.groupBox_5)
        self.Img_Nom.setGeometry(QtCore.QRect(10, 10, 461, 121))
        self.Img_Nom.setText("")
        self.Img_Nom.setScaledContents(True)
        self.Img_Nom.setObjectName("Img_Nom")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(40, 170, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.Nombre = QtWidgets.QTextEdit(self.groupBox_6)
        self.Nombre.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.Nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nombre.setObjectName("Nombre")
        self.Bot_Nombre = QtWidgets.QPushButton(self.groupBox_6)
        self.Bot_Nombre.setGeometry(QtCore.QRect(120, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bot_Nombre.setFont(font)
        self.Bot_Nombre.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.Bot_Nombre.setObjectName("Bot_Nombre")
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(40, 250, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.Carro = QtWidgets.QComboBox(self.groupBox_7)
        self.Carro.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.Carro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Carro.setObjectName("Carro")
        self.Carro.addItem("")
        self.Carro.addItem("")
        self.Carro.addItem("")
        self.Carro.addItem("")
        self.Carro.addItem("")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 330, 331, 301))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Img_gota = QtWidgets.QLabel(self.groupBox)
        self.Img_gota.setGeometry(QtCore.QRect(10, 10, 311, 281))
        self.Img_gota.setText("")
        self.Img_gota.setObjectName("Img_gota")
        self.groupBox_8 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_8.setGeometry(QtCore.QRect(390, 330, 331, 301))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.Img_posicion = QtWidgets.QLabel(self.groupBox_8)
        self.Img_posicion.setGeometry(QtCore.QRect(10, 10, 311, 281))
        self.Img_posicion.setText("")
        self.Img_posicion.setObjectName("Img_posicion")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Gota.clicked.connect(self.R_gota)
        self.Bot_Nombre.clicked.connect(self.save_as_image)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Taller 3"))
        self.label_6.setText(_translate("Dialog", "Juan Esteban Sanchez Lamprea - 66912"))
        self.label_10.setText(_translate("Dialog", "2024-1"))
        self.label_8.setText(_translate("Dialog", "Juan Bernal Garcia - 87190"))
        self.label_7.setText(_translate("Dialog", "Juan Camio Luna Calderon - 90522"))
        self.label_9.setText(_translate("Dialog", "Ing Mecatronica. Electiva de robotica"))
        self.label_4.setText(_translate("Dialog", "Wendy Dayan Silva Venegas - 66934"))
        self.groupBox_2.setTitle(_translate("Dialog", "Posicion"))
        self.label_11.setText(_translate("Dialog", "x"))
        self.label_12.setText(_translate("Dialog", "y"))
        self.Bot_Posicion.setText(_translate("Dialog", "Iniciar"))
        self.groupBox_3.setTitle(_translate("Dialog", "Gota"))
        self.Gota.setText(_translate("Dialog", "Iniciar"))
        self.groupBox_4.setTitle(_translate("Dialog", "Nombres"))
        self.Juan.setText(_translate("Dialog", "Juan"))
        self.Wendy.setText(_translate("Dialog", "Wendy"))
        self.Esteban.setText(_translate("Dialog", "Esteban"))
        self.Manuel.setText(_translate("Dialog", "Manuel"))
        self.groupBox_6.setTitle(_translate("Dialog", "Ingresar nombre"))
        self.Bot_Nombre.setText(_translate("Dialog", "Iniciar"))
        self.groupBox_7.setTitle(_translate("Dialog", "Elegir una imagen"))
        self.Carro.setItemText(0, _translate("Dialog", "Elige una opción"))
        self.Carro.setItemText(1, _translate("Dialog", "Chevrolet"))
        self.Carro.setItemText(2, _translate("Dialog", "Renault"))
        self.Carro.setItemText(3, _translate("Dialog", "Kia"))
        self.Carro.setItemText(4, _translate("Dialog", "Mercedes"))

    def R_gota(self, Dialog):
        # Cinemática inversa
        # Punto 1
        Px = [16, 0,-16,-7.5,-4,7.5,16]
        Py = [0,16,0,-8.5,0,8.5,0]
        theta1=[]
        theta2=[]
        thetax=[]
        thetay=[]
        theta_P1toP2=[]
        n = 10
        x = numpy.arange(1,n+1,1)
        for i in range(0,7):
            [theta1_i, theta2_i] = inversa_2R(l1,l2,Px[i],Py[i])
            theta2.append(theta2_i)
            theta1.append(theta1_i)
        for i in range(0,6):
            if i==3:
                # Reverse the order of the points
                thetax_P1toP2 = numpy.arange(theta1[i], theta1[i+1], 0.2)[::-1]
                thetay_P1toP2 = numpy.arange(theta2[i], theta2[i+1], 0.2)
                print (thetay_P1toP2," ", thetax_P1toP2)

            else:
                thetax_P1toP2 = numpy.linspace(theta1[i], theta1[i+1], n)
                thetay_P1toP2 = numpy.linspace(theta2[i], theta2[i+1], n)
            thetax.append(thetax_P1toP2)
            thetay.append(thetay_P1toP2)
            print (thetax)
            print (thetay)

        # Concatenar los vectores en un solo vector
        thetax = numpy.concatenate(thetax)
        thetay = numpy.concatenate(thetay)

        v=thetax.size

        d = numpy.zeros((3,v))
        fig1 = plt.figure().add_subplot(projection='3d')
        fig1.set_xlabel('X')
        fig1.set_ylabel('Y')
        fig1.set_zlabel('Z')
        fig1.set_xlim(-19, 19)
        fig1.set_ylim(-19, 19)
        fig1.set_zlim(-19, 19)
        fig1.plot(d[0,i],d[1,i],d[2,i],'.b')
        for i in range (0,v):
            Servos(thetax[i],thetay[i])
            MTH = plot_1(l1,l2,thetax[i],thetay[i])
            print (MTH)
            d[:,i] =  MTH.t    
            fig1.plot(d[0,i],d[1,i],d[2,i],'.b')
        ang1 = np.rad2deg(theta1)
        ang2 = np.rad2deg(theta2)
        self.label_12.setText(f"{ang1} °")
        self.label_13.setText(f"{ang2} °")
        






        # plt.savefig("Ejemplo1.png")
        # self.Robot.setPixmap(QtGui.QPixmap("Ejemplo1.png"))

        
    def save_as_image(self, Dialog):
        print ("Creando imagen")
        nombre = self.Nombre.toPlainText()
        pixmap = QPixmap(200, 100)  # Tamaño de la imagen a crear
        pixmap.fill(QtGui.QColor("white"))  # Rellenar la imagen con color blanco
        painter = QtGui.QPainter(pixmap)
        font = painter.font()  # Obtener la fuente actual
        font.setPointSize(30)  # Establecer el tamaño de la fuente
        painter.setFont(font)  # Aplicar la fuente al pintor
        painter.drawText(10, 50, nombre)  # Dibujar texto en la imagen
        painter.end()
        pixmap.save("/home/pi/Documents/Electiva_Robotica/Taller 3/Esteban.png")  # Guardar la imagen como "imagen.png"
        print ("imagen creada")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

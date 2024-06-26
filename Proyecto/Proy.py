from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
import math
import numpy
import numpy as np
import pandas as pd
from sympy import *
from roboticstoolbox import *
from spatialmath.base import *
import matplotlib.pyplot as plt

direction_M1= 5 # Direction (DIR) GPIO Pin
step_M1 = 4 # Step GPIO Pin
EN_pin = 21 # enable pin (LOW to enable)
direction_M3= 6 # Direction (DIR) GPIO Pin
step_M3 = 17 # Step GPIO Pin
direction_M2= 26 # Direction (DIR) GPIO Pin
step_M2 = 27 # Step GPIO Pin
mymotortest_M1 = RpiMotorLib.A4988Nema(direction_M1, step_M1, (EN_pin,EN_pin,EN_pin), "A4988")
mymotortest_M2 = RpiMotorLib.A4988Nema(direction_M2, step_M2, (EN_pin,EN_pin,EN_pin), "A4988")
mymotortest_M3 = RpiMotorLib.A4988Nema(direction_M3, step_M3, (EN_pin,EN_pin,EN_pin), "A4988")
IR_SENSOR_PIN1 = 20
IR_SENSOR_PIN2 = 12
IR_SENSOR_PIN3 = 22
archivo = '/home/pi/Documents/Electiva_Robotica/Proyecto/Archivo.csv'
df = pd.read_csv(archivo)
previous_angle_M1 = int(df['M1'])
previous_angle_M2 = int(df['M2'])
previous_angle_M3 = int(df['M3'])

l1 = 18
l2 = 16
l3 = 38

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(719, 847)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(77, 710, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(50, 640, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(57, 614, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(57, 750, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(134, 790, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(47, 574, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.modo = QtWidgets.QLabel(Dialog)
        self.modo.setFont(font)
        self.modo.setObjectName("modo")
        self.Logo = QtWidgets.QLabel(Dialog)
        self.Logo.setGeometry(QtCore.QRect(380, 600, 291, 191))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.Motor1 = QtWidgets.QSlider(Dialog)
        self.Motor1.setGeometry(QtCore.QRect(120, 120, 160, 22))
        self.Motor1.setOrientation(QtCore.Qt.Horizontal)
        self.Motor1.setObjectName("Motor1")
        self.Motor1.setMaximum(360)#Modificar
        self.Motor2 = QtWidgets.QSlider(Dialog)
        self.Motor2.setGeometry(QtCore.QRect(120, 160, 160, 22))
        self.Motor2.setOrientation(QtCore.Qt.Horizontal)
        self.Motor2.setObjectName("Motor2")
        self.Motor2.setMaximum(180)#Modificar
        self.Motor2.setProperty("value", 90)
        self.Motor3 = QtWidgets.QSlider(Dialog)
        self.Motor3.setGeometry(QtCore.QRect(120, 200, 160, 22))
        self.Motor3.setOrientation(QtCore.Qt.Horizontal)
        self.Motor3.setObjectName("Motor3")
        self.Motor3.setMaximum(180)#Modificar
        self.Motor3.setProperty("value", 90)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Angulo_M1 = QtWidgets.QLabel(Dialog)
        self.Angulo_M1.setGeometry(QtCore.QRect(290, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Angulo_M1.setFont(font)
        self.Angulo_M1.setText("")
        self.Angulo_M1.setObjectName("Angulo_M1")
        self.Angulo_M2 = QtWidgets.QLabel(Dialog)
        self.Angulo_M2.setGeometry(QtCore.QRect(290, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Angulo_M2.setFont(font)
        self.Angulo_M2.setText("")
        self.Angulo_M2.setObjectName("Angulo_M2")
        self.Angulo_M3 = QtWidgets.QLabel(Dialog)
        self.Angulo_M3.setGeometry(QtCore.QRect(290, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Angulo_M3.setFont(font)
        self.Angulo_M3.setText("")
        self.Angulo_M3.setObjectName("Angulo_M3")
        self.Grip_abrir = QtWidgets.QPushButton(Dialog)
        self.Grip_abrir.setGeometry(QtCore.QRect(120, 250, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Grip_abrir.setFont(font)
        self.Grip_abrir.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.Grip_abrir.setObjectName("Grip_abrir")
        self.Grip_cerrar = QtWidgets.QPushButton(Dialog)
        self.Grip_cerrar.setGeometry(QtCore.QRect(200, 250, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Grip_cerrar.setFont(font)
        self.Grip_cerrar.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.Grip_cerrar.setObjectName("Grip_cerrar")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 341, 271))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(15, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 341, 271))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(15, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(108, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 60, 321, 271))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Semi_iniciar = QtWidgets.QPushButton(self.groupBox_2)
        self.Semi_iniciar.setGeometry(QtCore.QRect(110, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Semi_iniciar.setFont(font)
        self.Semi_iniciar.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.Semi_iniciar.setObjectName("Semi_iniciar")
        self.Pos_Z = QtWidgets.QTextEdit(self.groupBox_2)
        self.Pos_Z.setGeometry(QtCore.QRect(123, 139, 81, 31))
        self.Pos_Z.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pos_Z.setObjectName("Pos_Z")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(80, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(80, 140, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(79, 101, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.Pos_X = QtWidgets.QTextEdit(self.groupBox_2)
        self.Pos_X.setGeometry(QtCore.QRect(123, 57, 81, 31))
        self.Pos_X.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pos_X.setObjectName("Pos_X")
        self.Pos_Y = QtWidgets.QTextEdit(self.groupBox_2)
        self.Pos_Y.setGeometry(QtCore.QRect(123, 97, 81, 31))
        self.Pos_Y.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pos_Y.setObjectName("Pos_Y")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 340, 341, 151))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(20, 15, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.Auto_Iniciar = QtWidgets.QPushButton(self.groupBox_4)
        self.Auto_Iniciar.setGeometry(QtCore.QRect(110, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Auto_Iniciar.setFont(font)
        self.Auto_Iniciar.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.Auto_Iniciar.setObjectName("Auto_Iniciar")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 340, 321, 241))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.Img = QtWidgets.QLabel(self.groupBox_5)
        self.Img.setGeometry(QtCore.QRect(10, 10, 301, 221))
        self.Img.setText("")
        self.Img.setObjectName("Img")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(70, 680, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.Encender = QtWidgets.QPushButton(Dialog)
        self.Encender.setGeometry(QtCore.QRect(60, 510, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Encender.setFont(font)
        self.Encender.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.Encender.setObjectName("Encender")
        self.Apagar = QtWidgets.QPushButton(Dialog)
        self.Apagar.setGeometry(QtCore.QRect(210, 510, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Apagar.setFont(font)
        self.Apagar.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.Apagar.setObjectName("Apagar")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.label_15.raise_()
        self.label_11.raise_()
        self.label_5.raise_()
        self.label_14.raise_()
        self.label_13.raise_()
        self.label_12.raise_()
        self.Logo.raise_()
        self.Motor1.raise_()
        self.Motor2.raise_()
        self.Motor3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.Angulo_M1.raise_()
        self.Angulo_M2.raise_()
        self.Angulo_M3.raise_()
        self.Grip_abrir.raise_()
        self.Grip_cerrar.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.label_25.raise_()
        self.Encender.raise_()
        self.Apagar.raise_()
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(EN_pin,GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        self.servo1 = GPIO.PWM(19, 50)  # GPIO 19 para Servo 1 con frecuencia de 50Hz
        self.servo1.start(0)
        GPIO.setup(IR_SENSOR_PIN1, GPIO.IN)
        GPIO.setup(IR_SENSOR_PIN2, GPIO.IN)
        GPIO.setup(IR_SENSOR_PIN3, GPIO.IN)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Motor1.sliderMoved.connect(self.M1_slider)
        self.Motor2.sliderMoved.connect(self.M2_slider)
        self.Motor3.sliderMoved.connect(self.M3_slider)
        self.Semi_iniciar.clicked.connect(self.Semi_auto)
        self.Auto_Iniciar.clicked.connect(self.automatico)
        self.Apagar.clicked.connect(self.Bot_apagar)
        # self.Encender.clicked.connect(self.Bot_Encender)
        self.Grip_abrir.clicked.connect(self.Grip_ab)
        self.Grip_cerrar.clicked.connect(self.Grip_ce)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Proyecto Robot 3 GDL"))
        self.label_15.setText(_translate("Dialog", "Juan Bernal Garcia - 87190"))
        self.label_11.setText(_translate("Dialog", "Juan Camio Luna Calderon - 90522"))
        self.label_5.setText(_translate("Dialog", "Wendy Dayan Silva Venegas - 66934"))
        self.label_14.setText(_translate("Dialog", "Ing Mecatronica. Electiva de robotica"))
        self.label_13.setText(_translate("Dialog", "2024-1"))
        self.label_12.setText(_translate("Dialog", "Juan Esteban Sanchez Lamprea - 66912"))
        self.label_6.setText(_translate("Dialog", "Motor #1"))
        self.label_7.setText(_translate("Dialog", "Motor #2"))
        self.label_8.setText(_translate("Dialog", "Motor #3"))
        self.Grip_abrir.setText(_translate("Dialog", "Abrir"))
        self.Grip_cerrar.setText(_translate("Dialog", "Cerrar"))
        self.label_3.setText(_translate("Dialog", "Modo: Manual"))
        self.label_20.setText(_translate("Dialog", "Gripper"))
        self.label_22.setText(_translate("Dialog", "Gripper"))
        self.label_21.setText(_translate("Dialog", "Modo: Manual"))
        self.label_4.setText(_translate("Dialog", "Modo: Semiautomático"))
        self.Semi_iniciar.setText(_translate("Dialog", "Iniciar"))
        self.label_17.setText(_translate("Dialog", "Pos X"))
        self.label_18.setText(_translate("Dialog", "Pos Z"))
        self.label_19.setText(_translate("Dialog", "Pos Y"))
        self.label_23.setText(_translate("Dialog", "Modo: Automatico"))
        self.Auto_Iniciar.setText(_translate("Dialog", "Iniciar"))
        self.label_25.setText(_translate("Dialog", "Nicolás Martínez Guzmán - 70020"))
        self.Encender.setText(_translate("Dialog", "Encender"))
        self.Apagar.setText(_translate("Dialog", "Apagar"))
        self.modo.setText(_translate("Dialog", "Modo:"))
    def M1_slider(self, value):
        global previous_angle_M1, previous_angle_M2, previous_angle_M3
        #self.modo.setText("Dialog", "Modo:Manual")
        q1 = np.deg2rad(value)
        q2 = np.deg2rad(previous_angle_M2)
        q3 = np.deg2rad(previous_angle_M3)
        self.update_motor1_angle(value)
        previous_angle_M1 = value
        #MTH = ForwardKinematics3R(l1,l2,l3,q1,q2,q3)
    def M2_slider(self, value):
        global previous_angle_M1, previous_angle_M2, previous_angle_M3
        #self.modo.setText("Dialog", "Modo:Manual")
        q2 = np.deg2rad(value)
        q1 = np.deg2rad(previous_angle_M1)
        q3 = np.deg2rad(previous_angle_M3)
        self.update_motor2_angle(value)
        previous_angle_M2 = value
        #MTH = ForwardKinematics3R(l1,l2,l3,q1,q2,q3)
    def M3_slider(self, value):
        global previous_angle_M1, previous_angle_M2, previous_angle_M3
        #self.modo.setText("Dialog", "Modo:Manual")
        q3 = np.deg2rad(value)
        q2 = np.deg2rad(previous_angle_M2)
        q1 = np.deg2rad(previous_angle_M1)
        self.update_motor3_angle(value)
        previous_angle_M3 = value
        #MTH = ForwardKinematics3R(l1,l2,l3,q1,q2,q3)
    def update_motor1_angle(self, value):
        global previous_angle_M1
        self.Angulo_M1.setText(str(value))
        # Calcular el número de pasos necesarios para mover el motor al ángulo deseado
        angle = value
        steps_per_revolution = 1800
        steps_needed = int(abs(angle - previous_angle_M1) * steps_per_revolution / 360)
        GPIO.output(EN_pin, GPIO.LOW)  # Habilitar el motor

        # Mover el motor en la dirección apropiada según el cambio de ángulo
        if angle < previous_angle_M1:
            sentido=True
        else:
            sentido=False
        w=0
        print (steps_needed)
        while w!=steps_needed:
            while GPIO.input(IR_SENSOR_PIN1) == GPIO.LOW or GPIO.input(IR_SENSOR_PIN3) == GPIO.LOW:
                print("Objeto detenido")
            if GPIO.input(IR_SENSOR_PIN2) == GPIO.LOW:
                mymotortest_M1.motor_go(sentido, "Full", 1, 0.1, False, 0.05 )#bajar velocidad
                print("lento")
            else:
                mymotortest_M1.motor_go(sentido, "Full", 1, 0.005, False, 0.05)
            w=w+1   
            print (w)
             
        previous_angle_M1 = angle
        df['M1'] =previous_angle_M1
        df.to_csv(archivo, index=False)
    def update_motor2_angle(self, value):
        # Actualizar el ángulo en el QLabel correspondiente
        global previous_angle_M2
        
        self.Angulo_M2.setText(str(value))
        # Calcular el número de pasos necesarios para mover el motor al ángulo deseado
        angle = value
        steps_per_revolution = 700
        steps_needed = int(abs(angle - previous_angle_M2) * steps_per_revolution / 180)
        GPIO.output(EN_pin, GPIO.LOW)  # Habilitar el motor

        # Mover el motor en la dirección apropiada según el cambio de ángulo
        if angle < previous_angle_M2:
            
            sentido=False
        else:
            sentido=True
        w=0
        while w!=steps_needed:
            while GPIO.input(IR_SENSOR_PIN1) == GPIO.LOW or GPIO.input(IR_SENSOR_PIN3) == GPIO.LOW:
                print("Objeto detenido")

            if GPIO.input(IR_SENSOR_PIN2) == GPIO.LOW:
                mymotortest_M2.motor_go(
                sentido, "Full", 1, 0.1, False, 0.05
                    )
            else:
                # Si no nos estamos devolviendo, mantener la dirección actual
                mymotortest_M2.motor_go(
                sentido, "Full", 1, 0.005, False, 0.05
                    )
            w=w+1
        previous_angle_M2 = angle
        df['M2'] =previous_angle_M2
        df.to_csv(archivo, index=False)
        # Mover el motor a la posición deseada

        # Actualizar el ángulo anterior
        previous_angle_M2 = angle
    def update_motor3_angle(self, value):
        # Actualizar el ángulo en el QLabel correspondiente
        global previous_angle_M3
        self.Angulo_M3.setText(str(value))
        # Calcular el número de pasos necesarios para mover el motor al ángulo deseado
        angle = value
        steps_per_revolution = 700
        steps_needed = int(abs(angle - previous_angle_M3) * steps_per_revolution / 180)
        GPIO.output(EN_pin, GPIO.LOW)  # Habilitar el motor
        
        # Mover el motor en la dirección apropiada según el cambio de ángulo
        if angle < previous_angle_M3:
            sentido=False
        else:
            # Si no nos estamos devolviendo, mantener la dirección actual
            sentido=True
        w=0
        while w!=steps_needed:
            while GPIO.input(IR_SENSOR_PIN1) == GPIO.LOW or GPIO.input(IR_SENSOR_PIN3) == GPIO.LOW:
                print("Objeto detenido")

            if GPIO.input(IR_SENSOR_PIN2) == GPIO.LOW:
                mymotortest_M3.motor_go(
                sentido, "Full", 1, 0.1, False, 0.05
                    )
            else:
                mymotortest_M3.motor_go(
                sentido, "Full", 1, 0.005, False, 0.05
                    )
            w=w+1

        previous_angle_M3 = angle
        df['M3'] =previous_angle_M3
        df.to_csv(archivo, index=False)
        # Actualizar el ángulo anterior
        previous_angle_M3 = angle
    def Semi_auto(self, value):
        self.modo.setText("Modo:Semiautomatico")
        # Cinemática inversa
        Px = -int(self.Pos_X.toPlainText())
        Py = -int(self.Pos_Y.toPlainText())
        Pz = int(self.Pos_Z.toPlainText())
        print (Px, Py, Pz)
        e = -sqrt(Px**2+Py**2)
        c = Pz - l1
        b = sqrt(e**2+c**2)
        # Theta 1
        theta1 = float(atan2(Py,Px))
        # Theta 3
        cos_theta3 = (b**2-l2**2-l3**2)/(2*l2*l3)
        sen_theta3 = sqrt(1-(cos_theta3)**2)
        theta3 = float(atan2(sen_theta3, cos_theta3))
        # Theta 2
        alpha = math.atan2(c,e)
        phi = math.atan2(l3*sen_theta3, l2+l3*cos_theta3)
        theta2 = float(alpha - phi)
        if (theta2 == np.deg2rad(-180) or theta3 == np.deg2rad(-180)):
            theta2 = abs(theta2)
            theta3 = abs(theta3)
        if theta2 <= -numpy.pi:
            theta2 = (2*numpy.pi)+theta2
        if theta1 < 0:
            theta1 = theta1+np.deg2rad(360)
        elif (theta2 < 0 or theta3 < 0) :
            print("limites superados")
        else:
            self.Angulo_M1.setText(str(np.rad2deg(theta1)))
            self.Angulo_M2.setText(str(np.rad2deg(theta2)))
            self.Angulo_M3.setText(str(np.rad2deg(theta3)))
            self.update_motor1_angle((np.rad2deg(theta1)))
            self.update_motor2_angle((np.rad2deg(theta2)))
            self.update_motor3_angle((np.rad2deg(theta3)))
         
        #-------------

        q1 = theta1
        q2 = theta2
        q3 = theta3


        
        R = []
        R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=0))

        Robot = DHRobot(R, name='Bender')
        print(Robot)

        Robot.teach([q1, q2, q3], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

        #zlim([-15,30]);

        MTH = Robot.fkine([q1,q2,q3])
        print(MTH)
        print(f"Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}")
    def automatico(self, value):
	    print("Falta")

    def Bot_apagar(self, value):
        GPIO.cleanup() # clear GPIO allocations after run
        print("Falta")

    def Bot_Encender(self, value):

        print("Falta")

        
    def Grip_ab(self, value):
        self.servo1.ChangeDutyCycle(0)
        duty = 90 / 18.0 + 2.5
        self.servo1.ChangeDutyCycle(duty)
        
    def Grip_ce(self, value):
        self.servo1.ChangeDutyCycle(0)
        duty = 180 / 18.0 + 2.5
        self.servo1.ChangeDutyCycle(duty)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

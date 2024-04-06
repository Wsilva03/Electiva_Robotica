from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(606, 447)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 260, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Logo = QtWidgets.QLabel(Dialog)
        self.Logo.setGeometry(QtCore.QRect(310, 180, 271, 231))
        self.Logo.setText("")
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(-10, 180, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(80, 380, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(0, 340, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 220, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Antihorario = QtWidgets.QPushButton(Dialog)
        self.Antihorario.setGeometry(QtCore.QRect(170, 130, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Antihorario.setFont(font)
        self.Antihorario.setObjectName("Antihorario")
        self.Horario = QtWidgets.QPushButton(Dialog)
        self.Horario.setGeometry(QtCore.QRect(320, 130, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Horario.setFont(font)
        self.Horario.setObjectName("Horario")
        self.Vueltas = QtWidgets.QTextEdit(Dialog)
        self.Vueltas.setGeometry(QtCore.QRect(250, 70, 81, 41))
        self.Vueltas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Vueltas.setObjectName("Vueltas")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Antihorario.clicked.connect(self.girar_antihorario)
        self.Horario.clicked.connect(self.girar_horario)

        self.GPIO_PWM = 12
        self.GPIO_Horario = 20
        self.GPIO_anti = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_PWM, GPIO.OUT)
        GPIO.setup(self.GPIO_Horario, GPIO.OUT)
        GPIO.setup(self.GPIO_anti, GPIO.OUT)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def limpiar_gpio(self):
        GPIO.cleanup()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "Juan Camio Luna Calderon - 90522"))
        self.label_6.setText(_translate("Dialog", "Juan Esteban Sanchez Lamprea - 66912"))
        self.label_8.setText(_translate("Dialog", "Juan Bernal Garcia - 87190"))
        self.label_10.setText(_translate("Dialog", "2024-1"))
        self.label_9.setText(_translate("Dialog", "Ing Mecatronica. Electiva de robotica"))
        self.label_3.setText(_translate("Dialog", "Wendy Dayan Silva Venegas - 66934"))
        self.Antihorario.setText(_translate("Dialog", "Antihorario"))
        self.Horario.setText(_translate("Dialog", "Horario"))
        self.label_2.setText(_translate("Dialog", "Numero de vueltas:"))

    def girar_motor(self, pin, pasos, delay):
        for _ in range(pasos):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(delay)

    def girar_antihorario(self):
        vueltas = float(self.Vueltas.toPlainText())
        pasos_por_vuelta = 118  # Dependiendo del tipo de motor paso a paso
        pasos_totales = int(vueltas * pasos_por_vuelta)
        delay = 0.005  # Retraso en segundos entre pasos

        self.girar_motor(self.GPIO_anti, pasos_totales, delay)

    def girar_horario(self):
        vueltas = float(self.Vueltas.toPlainText())
        pasos_por_vuelta = 118  # Dependiendo del tipo de motor paso a paso
        pasos_totales = int(vueltas * pasos_por_vuelta)
        delay = 0.005  # Retraso en segundos entre pasos

        self.girar_motor(self.GPIO_Horario, pasos_totales, delay)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

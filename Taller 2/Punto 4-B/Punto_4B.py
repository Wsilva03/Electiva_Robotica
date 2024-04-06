
from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(607, 458)
        Dialog.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 270, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 150, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(90, 350, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Logo = QtWidgets.QLabel(Dialog)
        self.Logo.setGeometry(QtCore.QRect(320, 150, 271, 231))
        self.Logo.setText("")
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.Estado = QtWidgets.QLabel(Dialog)
        self.Estado.setGeometry(QtCore.QRect(190, 70, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Estado.setFont(font)
        self.Estado.setText("")
        self.Estado.setObjectName("Estado")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 70, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.GPIO_PIN = 17  # Puedes cambiar este número según el pin que estés utilizando
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_PIN, GPIO.IN)
        self.GPIO_PIN = 26  # Puedes cambiar este número según el pin que estés utilizando
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_PIN, GPIO.IN)
        # Actualizar el estado del pin GPIO cada segundo
        self.updateState()
       

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_9.setText(_translate("Dialog", "Ing Mecatronica. Electiva de robotica"))
        self.label_8.setText(_translate("Dialog", "Juan Bernal Garcia - 87190"))
        self.label_3.setText(_translate("Dialog", "Wendy Dayan Silva Venegas - 66934"))
        self.label_7.setText(_translate("Dialog", "Juan Camio Luna Calderon - 90522"))
        self.label_6.setText(_translate("Dialog", "Juan Esteban Sanchez Lamprea - 66912"))
        self.label_10.setText(_translate("Dialog", "2024-1"))
        self.label_5.setText(_translate("Dialog", "Estado:"))
    def updateState(self):
        # Leer el estado del pin GPIO
        state = GPIO.input(self.GPIO_PIN)

        # Actualizar el texto y el color del Static Text según el estado
        if state == GPIO.LOW:
            self.Estado.setText("alto")
            self.Estado.setStyleSheet("color: red;")
        else:
            self.Estado.setText("bajo")
            self.Estado.setStyleSheet("color: blue;")

        # Actualizar el estado cada segundo
        QtCore.QTimer.singleShot(1000, self.updateState)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

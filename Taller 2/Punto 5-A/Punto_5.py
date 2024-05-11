from PyQt5 import QtCore, QtGui, QtWidgets

import cv2

from PyQt5.QtGui import QImage, QPixmap

from PyQt5.QtWidgets import QFileDialog



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(807, 625)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")

        self.Cargar_imagen = QtWidgets.QPushButton(self.centralwidget)

        self.Cargar_imagen.setGeometry(QtCore.QRect(150, 10, 111, 41))

        self.Cargar_imagen.setObjectName("Cargar_imagen")

        self.Imagen = QtWidgets.QLabel(self.centralwidget)

        self.Imagen.setGeometry(QtCore.QRect(20, 60, 761, 401))

        self.Imagen.setScaledContents(True)

        self.Imagen.setObjectName("Imagen")

        self.Nombre1 = QtWidgets.QLabel(self.centralwidget)

        self.Nombre1.setGeometry(QtCore.QRect(40, 480, 171, 21))

        self.Nombre1.setObjectName("Nombre1")

        self.Nombre2 = QtWidgets.QLabel(self.centralwidget)

        self.Nombre2.setGeometry(QtCore.QRect(40, 500, 151, 21))

        self.Nombre2.setObjectName("Nombre2")

        self.Nombre3 = QtWidgets.QLabel(self.centralwidget)

        self.Nombre3.setGeometry(QtCore.QRect(40, 520, 141, 21))

        self.Nombre3.setObjectName("Nombre3")

        self.Nombre4 = QtWidgets.QLabel(self.centralwidget)

        self.Nombre4.setGeometry(QtCore.QRect(40, 540, 151, 21))

        self.Nombre4.setObjectName("Nombre4")

        self.Universidad = QtWidgets.QLabel(self.centralwidget)

        self.Universidad.setGeometry(QtCore.QRect(240, 490, 211, 21))

        self.Universidad.setObjectName("Universidad")

        self.Fecha = QtWidgets.QLabel(self.centralwidget)

        self.Fecha.setGeometry(QtCore.QRect(300, 520, 47, 13))

        self.Fecha.setObjectName("Fecha")

        self.Logo = QtWidgets.QLabel(self.centralwidget)

        self.Logo.setGeometry(QtCore.QRect(490, 480, 291, 111))

        self.Logo.setText("")

        self.Logo.setPixmap(QtGui.QPixmap("/home/pi/Documents/Electiva_Robotica/Taller 2/logo-ecci.png"))

        self.Logo.setScaledContents(True)

        self.Logo.setObjectName("Logo")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))

        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

        self.Cargar_imagen.clicked.connect(self.cargar_imagen)

        

        self.imagen_cargada = None



    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.Cargar_imagen.setText(_translate("MainWindow", "Cargar_imagen"))

        self.Imagen.setText(_translate("MainWindow", "Imagen"))

        self.Nombre1.setText(_translate("MainWindow", "Juan Esteban Lamprea - 66912"))

        self.Nombre2.setText(_translate("MainWindow", "Wendy Dayan Silva - 66934"))

        self.Nombre3.setText(_translate("MainWindow", "Juan Camilo Luna - 90522"))

        self.Nombre4.setText(_translate("MainWindow", "Juan Bernal Garcia - 87190"))

        self.Universidad.setText(_translate("MainWindow", "Ing. Mecatronica - electiva de robotica"))

        self.Fecha.setText(_translate("MainWindow", "2024-1"))



        

    def cargar_imagen(self):

        print("Cargar imagen")

        filename, _ = QFileDialog.getOpenFileName(None, "Seleccionar imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

        if filename:

            self.imagen_cargada = cv2.imread(filename)

            self.mostrar_imagen(self.imagen_cargada)
            self.detectar_contornos()

    

    

    def mostrar_imagen(self, imagen):

        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        h, w, ch = imagen.shape

        bytesPerLine = ch * w

        qImg = QtGui.QImage(imagen.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)

        pixmap = QtGui.QPixmap.fromImage(qImg)

        self.Imagen.setPixmap(pixmap)

        

    def detectar_contornos(self):

        print("Detectar contornos")

        if self.imagen_cargada is not None:

            imagen_gris = cv2.cvtColor(self.imagen_cargada, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(imagen_gris, 127, 255, 0)

            contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                # Obtener las coordenadas del contorno
                x, y, w, h = cv2.boundingRect(contour)
                print("Coordenadas del contorno: x={}, y={}, w={}, h={}".format(x, y, w, h))


        
            imagen_con_contornos = cv2.drawContours(self.imagen_cargada.copy(), contours, -1, (0, 255, 0), 2)

            self.mostrar_imagen(imagen_con_contornos)

        else:

            QtWidgets.QMessageBox.warning(None, "Advertencia", "Por favor, primero carga una imagen.")





if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())


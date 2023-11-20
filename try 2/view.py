from PyQt5.QtWidgets import QMainWindow, QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('browse.ui', self)
        self.folder=""
    
    def setup(self):
        self.browse.clicked.connect(self.browsefiles)
        self.load.clicked.connect(self.abrirVentanaVisualizacion)
    
    def browsefiles(self):
        folder=QFileDialog.getExistingDirectory(self,"Open File")
        self.filepath.setText(folder)
        self.folder=folder

    def abrirVentanaVisualizacion(self):
        ventana_visualizacion=VentanaVisualizacion(self)
        self.hide()
        ventana_visualizacion.show()

    def recibir_imagen(self,imagen):
        self.__mi_coordinador.img_conextion(imagen)

    def addControler(self,c):
        self.__mi_coordinador=c
        self.setup()

class VentanaVisualizacion(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('visualization.ui',self)
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        folder = self.__ventanaPadre.folder
        archivos = os.listdir(folder)
        filename = archivos[5]
        imagen = f"{folder}/{filename}"
        print(archivos)
        print(imagen)
        self.__ventanaPadre.recibir_imagen(imagen)
        # self.__ventanaPadre.__mi_coordinador.img_conextion(imagen)
        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')
        self.buttonBox.rejected.connect(self.cerrar)

    def cerrar(self):
        print(self.__ventanaPadre.folder)
        self.__ventanaPadre.show()

    # def cargar(self):
    #     folder = self.__ventanaPadre.folder
    #     archivos = os.listdir(folder)
    #     filename = archivos[0]
    #     imagen = f"{folder}\{filename}"
    #     self.__ventanaPadre.__mi_coordinador.img_conextion(imagen)
    #     pixmap = QPixmap("temp_image.png")
    #     self.img.setPixmap(pixmap)
    #     os.remove('temp_image.png')
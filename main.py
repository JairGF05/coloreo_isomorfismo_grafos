
#from functions import *
from analyze_text import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import networkx as nx

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #en este label va la imagen de fondo
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1000, 1500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("book.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        
        #este label tiene el titulo 
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(140, 20, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        
        #esta es la etiqueta nodos
        self.nodos = QtWidgets.QLabel(self.centralwidget)
        self.nodos.setGeometry(QtCore.QRect(40, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.nodos.setFont(font)
        self.nodos.setObjectName("No. Nodos:")

        #esta es la etiqueta arcos
        self.arcos = QtWidgets.QLabel(self.centralwidget)
        self.arcos.setGeometry(QtCore.QRect(40, 221, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.arcos.setFont(font)
        self.arcos.setObjectName("No. Arcos:")

        #esta es la etiqueta de grados
        self.grados = QtWidgets.QLabel(self.centralwidget)
        self.grados.setGeometry(QtCore.QRect(40, 261, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.grados.setFont(font)
        self.grados.setObjectName("Grados:")

        #esta es la etiqueta de euleriano
        self.eulerian = QtWidgets.QLabel(self.centralwidget)
        self.eulerian.setGeometry(QtCore.QRect(40, 351, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.eulerian.setFont(font)
        self.eulerian.setObjectName("Euleriano:")

        #esta es la etiqueta de camino euleriano
        self.eulerian_path = QtWidgets.QLabel(self.centralwidget)
        self.eulerian_path.setGeometry(QtCore.QRect(40, 441, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.eulerian_path.setFont(font)
        self.eulerian_path.setObjectName("Euleriano_path:")
        
         #esta es la etiqueta conexo
        self.conexo = QtWidgets.QLabel(self.centralwidget)
        self.conexo.setGeometry(QtCore.QRect(40, 531, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.conexo.setFont(font)
        self.conexo.setObjectName("conexo:")

         #esta es la etiqueta no_cromatico
        self.cromatico = QtWidgets.QLabel(self.centralwidget)
        self.cromatico.setGeometry(QtCore.QRect(40, 571, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.cromatico.setFont(font)
        self.cromatico.setObjectName("cromatico:")

        #aqui es donde se muestra los nodos
        self.no_nodos_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.no_nodos_1.setGeometry(QtCore.QRect(140, 180, 250, 31))
        self.no_nodos_1.setObjectName("no_nodos_1")
        self.no_nodos_1.setEnabled(False)

        self.no_nodos_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.no_nodos_2.setGeometry(QtCore.QRect(395, 180, 250, 31))
        self.no_nodos_2.setObjectName("no_nodos_2")
        self.no_nodos_2.setEnabled(False)
        
        #aqui es donde se muestra los arcos
        self.no_arcos_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.no_arcos_1.setGeometry(QtCore.QRect(140, 221, 250, 31))
        self.no_arcos_1.setObjectName("no_arcos_1")
        self.no_arcos_1.setEnabled(False)

        self.no_arcos_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.no_arcos_2.setGeometry(QtCore.QRect(395, 221, 250, 31))
        self.no_arcos_2.setObjectName("no_arcos_2")
        self.no_arcos_2.setEnabled(False)

         #aqui es donde se muestra los grados
        self.grados_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.grados_1.setGeometry(QtCore.QRect(140, 261, 250, 80))
        self.grados_1.setObjectName("grados_1")
        self.grados_1.setEnabled(False)

        self.grados_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.grados_2.setGeometry(QtCore.QRect(395, 261, 250, 80))
        self.grados_2.setObjectName("grados_2")
        self.grados_2.setEnabled(False)

        #aqui es donde se muestra si tiene circuito euleriano
        self.eulerian_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.eulerian_1.setGeometry(QtCore.QRect(140, 351, 250, 80))
        self.eulerian_1.setObjectName("eulerian_1")
        self.eulerian_1.setEnabled(False)

        self.eulerian_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.eulerian_2.setGeometry(QtCore.QRect(395, 351, 250, 80))
        self.eulerian_2.setObjectName("eulerian_2")
        self.eulerian_2.setEnabled(False)

         #aqui es donde se muestra si tiene circuito euleriano
        self.eulerian_path_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.eulerian_path_1.setGeometry(QtCore.QRect(140, 441, 250, 80))
        self.eulerian_path_1.setObjectName("eulerian_path_1")
        self.eulerian_path_1.setEnabled(False)

        self.eulerian_path_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.eulerian_path_2.setGeometry(QtCore.QRect(395, 441, 250, 80))
        self.eulerian_path_2.setObjectName("eulerian_path_2")
        self.eulerian_path_2.setEnabled(False)

         #aqui es donde se muestra si es conexo
        self.conexo_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.conexo_1.setGeometry(QtCore.QRect(140, 531, 250, 31))
        self.conexo_1.setObjectName("conexo_1")
        self.conexo_1.setEnabled(False)

        self.conexo_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.conexo_2.setGeometry(QtCore.QRect(395, 531, 250, 31))
        self.conexo_2.setObjectName("conexo_2")
        self.conexo_2.setEnabled(False)

           #aqui es donde se muestra no cromatico
        self.cromatico_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.cromatico_1.setGeometry(QtCore.QRect(140, 571, 250, 31))
        self.cromatico_1.setObjectName("cromatico_1")
        self.cromatico_1.setEnabled(False)

        self.cromatico_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.cromatico_2.setGeometry(QtCore.QRect(395, 571, 250, 31))
        self.cromatico_2.setObjectName("cromatico_2")
        self.cromatico_2.setEnabled(False)


        #boton iniciar
        ''''
        self.iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.iniciar.setGeometry(QtCore.QRect(40, 540, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.iniciar.setFont(font)
        self.iniciar.setObjectName("Iniciar")
        '''

        #boton importar ejemplo
        self.importar_1 = QtWidgets.QPushButton(self.centralwidget)
        self.importar_1.setGeometry(QtCore.QRect(40, 100, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.importar_1.setFont(font)
        self.importar_1.setObjectName("Importar_texto_1")

        #aqui se observa el texto importado
        self.text_path_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.text_path_1.setGeometry(QtCore.QRect(210, 100, 411, 31))
        self.text_path_1.setObjectName("text_1")
        self.text_path_1.setText("Ningún archivo importado")
        self.text_path_1.setEnabled(False)

        #boton importar ejemplo
        self.importar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.importar_2.setGeometry(QtCore.QRect(40, 135, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.importar_2.setFont(font)
        self.importar_2.setObjectName("Importar_texto_2")

        #aqui se observa el texto 2 importado
        self.text_path_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.text_path_2.setGeometry(QtCore.QRect(210, 135, 411, 31))
        self.text_path_2.setObjectName("text_2")
        self.text_path_2.setText("Ningún archivo importado")
        self.text_path_2.setEnabled(False)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #aqui linkeamos el boton
        #self.iniciar.clicked.connect(self.relaciones)
        self.importar_1.clicked.connect(self.importar_texto_1)
        self.importar_2.clicked.connect(self.importar_texto_2)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Comparación textos"))
        self.nodos.setText(_translate("MainWindow", "No. Nodos: "))
        self.arcos.setText(_translate("MainWindow", "No. Arcos: "))
        self.grados.setText(_translate("MainWindow", "Grados: "))
        self.eulerian.setText(_translate("MainWindow", "Cir. Euler: "))
        self.eulerian_path.setText(_translate("MainWindow", "Cam. Euler: "))
        self.conexo.setText(_translate("MainWindow", "Conexo: "))
        self.cromatico.setText(_translate("MainWindow", "No. Crom: "))
        #self.iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.importar_1.setText(_translate("MainWindow", "Importar texto 1"))
        self.importar_2.setText(_translate("MainWindow", "Importar texto 2"))


    def importar_texto_1(self):    
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self.MainWindow,"Elige ejemplo a importar", "","Text Files (*.txt)", options=options)
        if fileName:
            self.text_path_1.setText(str(fileName))
            archivo = open(fileName, encoding="utf8")
            texto = archivo.read()
            
            #creando bigramas
            texto_limpio = limpiar_texto(texto)
            bigramas_texto=[]
            bigramas_texto = crear_bigramas(texto_limpio)
            #obteniendo tags
            partag=[]
            partag = crear_tags(texto_limpio)
            auxpartag = partag[:]

            g = nx.Graph()
            for a,b in bigramas_texto:
                subtag = partag.pop(0)
                g.add_edge(str(a), str(b),label=subtag)

            nodos = get_nodes(g)
            self.no_nodos_1.setText(str(nodos))
            arcos = get_edges(g)
            self.no_arcos_1.setText(str(arcos))
            grados = get_degree(g)
            self.grados_1.setText(str(grados))
            if (nx.is_eulerian(g)):
                self.eulerian_1.setText(str(nx.eulerian_circuit(g)))
            else:
                self.eulerian_1.setText("No tiene circuito")
            if (nx.has_eulerian_path(g)):
                lista = list(nx.eulerian_path(g))
                self.eulerian_path_1.setText(str(lista))
            else:
                self.eulerian_path_1.setText("No tiene camino")
            
            openl = []
            closedl = []
            visitados = []
            inicial = [texto_limpio[0]]
            terminal = texto_limpio[len(texto_limpio) -1 ]
            arcos = subtag
            nodos = texto_limpio
            
            while inicial:
                openl.append(inicial.pop(0))
                while openl:
                    elem = openl.pop(0)
                    closedl.append(elem)
                    #print("New closed:")
                    #print(closedl)
                    for tup in arcos:
                        if tup[0] == elem:
                            if tup[1] not in closedl and tup[1] not in openl:
                                openl.append(tup[1])
                                print(openl)
                    #print("---------------------")
                visitados = visitados + closedl
            novisitados = list(set(nodos) - set(visitados))
            #print("Nodos no visitados")
            #print(novisitados)
            if (novisitados):
                self.conexo_1.setText("No es conexo")
            else:
                self.conexo_1.setText("Si es conexo")
            numero_cromatico=coloreo_grafos(g, auxpartag, bigramas_texto,'grafo1.gv')
            self.cromatico_1.setText(str(numero_cromatico))
            archivo.close()
    
    def importar_texto_2(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self.MainWindow,"Elige ejemplo a importar", "","Text Files (*.txt)", options=options)
        if fileName:
            self.text_path_2.setText(str(fileName))
            archivo = open(fileName, encoding="utf8")
            texto = archivo.read()

            #creando bigramas
            texto_limpio = limpiar_texto(texto)
            bigramas_texto=[]
            bigramas_texto = crear_bigramas(texto_limpio)
            #obteniendo tags
            partag=[]
            partag = crear_tags(texto_limpio)
            auxpartag = partag[:]
            g = nx.Graph()
            for a,b in bigramas_texto:
                subtag = partag.pop(0)
                g.add_edge(str(a), str(b),label=subtag)

            #empieza analisis de isomorfismo   
            nodos = get_nodes(g)
            self.no_nodos_2.setText(str(nodos))
            arcos = get_edges(g)
            self.no_arcos_2.setText(str(arcos))
            grados = get_degree(g)
            self.grados_2.setText(str(grados))
            if (nx.is_eulerian(g)):
                self.eulerian_2.setText(str(nx.eulerian_circuit(g)))
            else:
                self.eulerian_2.setText("No tiene circuito")
            if (nx.has_eulerian_path(g)):
                lista = list(nx.eulerian_path(g))
                self.eulerian_path_2.setText(str(lista))
            else:
                self.eulerian_path_2.setText("No tiene camino")
            

            openl = []
            closedl = []
            visitados = []
            inicial = [texto_limpio[0]]
            terminal = texto_limpio[len(texto_limpio) -1 ]
            arcos = subtag
            nodos = texto_limpio
            
            while inicial:
                openl.append(inicial.pop(0))
                while openl:
                    elem = openl.pop(0)
                    closedl.append(elem)
                    #print("New closed:")
                    #print(closedl)
                    for tup in arcos:
                        if tup[0] == elem:
                            if tup[1] not in closedl and tup[1] not in openl:
                                openl.append(tup[1])
                                print(openl)
                    #print("---------------------")
                visitados = visitados + closedl
            novisitados = list(set(nodos) - set(visitados))
            #print("Nodos no visitados")
            #print(novisitados)
            if (novisitados):
                self.conexo_2.setText("No es conexo")
            else:
                self.conexo_2.setText("Si es conexo")
            numero_cromatico=coloreo_grafos(g, auxpartag, bigramas_texto,'grafo2.gv')
            self.cromatico_2.setText(str(numero_cromatico))
            archivo.close()


    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())


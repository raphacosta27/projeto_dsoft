# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Janela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from servicos import Ui_Servicos
from perfil import Ui_JanelPerfil
from calendario_novo import Ui_Calendario


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
    
        
        self.setupUi()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(759, 587)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.boas_vindas = QtGui.QLabel(self.centralwidget)
        self.boas_vindas.setGeometry(QtCore.QRect(10, 10, 251, 31))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.boas_vindas.setFont(font)
        self.boas_vindas.setObjectName("boas_vindas")
        
        self.pergunta = QtGui.QLabel(self.centralwidget)
        self.pergunta.setGeometry(QtCore.QRect(30, 70, 211, 41))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.pergunta.setFont(font)
        self.pergunta.setObjectName("pergunta")
        
        self.descr_janela = QtGui.QLabel(self.centralwidget)
        self.descr_janela.setGeometry(QtCore.QRect(30, 40, 721, 16))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.descr_janela.setFont(font)
        self.descr_janela.setObjectName("descr_janela")
        
        self.botao_integrantes = QtGui.QPushButton(self.centralwidget)
        self.botao_integrantes.setGeometry(QtCore.QRect(20, 120, 161, 81))
        self.botao_integrantes.setObjectName("botao_integrantes")
        self.descr_integrantes = QtGui.QLabel(self.centralwidget)
        self.descr_integrantes.setGeometry(QtCore.QRect(190, 120, 531, 81))
        self.descr_integrantes.setObjectName("descr_integrantes")
        
        self.botao_servicos = QtGui.QPushButton(self.centralwidget)
        self.botao_servicos.setGeometry(QtCore.QRect(20, 420, 161, 81))
        self.botao_servicos.setObjectName("botao_servicos")
        
        self.botao_aulas = QtGui.QPushButton(self.centralwidget)
        self.botao_aulas.setGeometry(QtCore.QRect(20, 320, 161, 81))
        self.botao_aulas.setObjectName("botao_aulas")
        
        self.pushBubotao_calendariotton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushBubotao_calendariotton_4.setGeometry(QtCore.QRect(20, 220, 161, 81))
        self.pushBubotao_calendariotton_4.setObjectName("pushBubotao_calendariotton_4")
        
        self.data_hoje = QtGui.QDateEdit(self.centralwidget)
        self.data_hoje.setGeometry(QtCore.QRect(250, 250, 110, 22))
        self.data_hoje.setObjectName("data_hoje")
        self.data_hoje.setDateTime(QtCore.QDateTime.currentDateTime())
         
        
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 460, 201, 16))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        
        self.descr_calendario = QtGui.QLabel(self.centralwidget)
        self.descr_calendario.setGeometry(QtCore.QRect(190, 220, 501, 81))
        self.descr_calendario.setObjectName("descr_calendario")
        
        self.descr_calendario2 = QtGui.QLabel(self.centralwidget)
        self.descr_calendario2.setGeometry(QtCore.QRect(370, 250, 351, 20))
        self.descr_calendario2.setObjectName("descr_calendario2")
        
        self.descr_aulas = QtGui.QLabel(self.centralwidget)
        self.descr_aulas.setGeometry(QtCore.QRect(190, 320, 531, 81))
        self.descr_aulas.setObjectName("descr_aulas")
        
        self.descr_servicos = QtGui.QLabel(self.centralwidget)
        self.descr_servicos.setGeometry(QtCore.QRect(190, 420, 531, 81))
        self.descr_servicos.setObjectName("descr_servicos")
        
        self.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        
        self.setStatusBar(self.statusbar)        
        
        self.botao_servicos.clicked.connect(self.ServicosClicked)
        
        self.botao_integrantes.clicked.connect(self.PerfilCLicked)
        
        self.botao_aulas.clicked.connect(self.CalendarioClicked)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.boas_vindas.setText(_translate("MainWindow", "Bem-Vindo ao Integrator !"))
        self.pergunta.setText(_translate("MainWindow", "O que você deseja acessar ?"))
        self.descr_janela.setText(_translate("MainWindow", "Aqui você pode acessar diversos serviços para que sua vida na sala seja muito mais prática e rápida."))
        self.botao_integrantes.setText(_translate("MainWindow", "Integrantes da sala"))
        self.descr_integrantes.setText(_translate("MainWindow", "Aqui você confere os perfis de cada integrante da sala, desde que ele esteja cadastrado no nosso aplicativo."))
        self.botao_servicos.setText(_translate("MainWindow", "Serviços próximos ao Insper"))
        self.botao_aulas.setText(_translate("MainWindow", "Aulas da semana"))
        self.pushBubotao_calendariotton_4.setText(_translate("MainWindow", "Calendário de tarefas"))
        self.descr_calendario.setText(_translate("MainWindow", "Hoje é dia "))
        self.descr_calendario2.setText(_translate("MainWindow", "segundo nossos servidores. Veja aqui o que está pendente na semana."))
        self.descr_aulas.setText(_translate("MainWindow", "Qual a sua próxima aula ? Boa pergunta ! Confira aqui o calendario das aulas da semana toda."))
        self.descr_servicos.setText(_translate("MainWindow", "Não sabe onde comer ? Nem onde sacar dinheiro ? Confira aqui algumas dicas recomendadas pelo Integrator."))
    
    def ServicosClicked(self):
        self.servicos = Ui_Servicos()
        self.servicos.show()
    
    def PerfilCLicked (self): 
        self.perfis = Ui_JanelPerfil()
        self.perfis.show()
    def CalendarioClicked(self):
        self.calendario = Ui_Calendario()   
        self.calendario.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainwindow = Ui_MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())


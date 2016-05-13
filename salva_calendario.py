# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from firebase import firebase
from Calendario import Ui_Calendario

class SalvaCalendario :
    def salvar (self):
        self.calendario = Ui_Calendario()
        
        #pegando textos das labels
        
        #Descrição das aulas
        self.segunda = self.calendario.S_Aula.text()
        self.segunda2 = self.calendario.S_Aula_2.text()
        self.segunda3 = self.calendario.S_Aula_3.text()
        self.segunda4 = self.calendario.S_Aula_4.text()
        self.segunda5 = self.calendario.S_Aula_5.text()
        self.segunda6 = self.calendario.S_Aula_6.text()
        self.segunda7 = self.calendario.S_Aula_7.text()
        
        self.terça = self.calendario.T_Aula.text()
        self.terça2 = self.calendario.T_Aula2.text()
        self.terça3 = self.calendario.T_Aula3.text()
        self.terça4 = self.calendario.T_Aula4.text()
        self.terça5 = self.calendario.T_Aula5.text()
        self.terça6 = self.calendario.T_Aula6.text()
        self.terça7 = self.calendario.T_Aula7.text()
        
        self.quarta = self.calendario.Q_Aula.text()
        self.quarta2 = self.calendario.Q_Aula_2.text()
        self.quarta3 = self.calendario.Q_Aula_3.text()
        self.quarta4 = self.calendario.Q_Aula_4.text()
        self.quarta5 = self.calendario.Q_Aula_5.text()
        self.quarta6 = self.calendario.Q_Aula_6.text()
        self.quarta7 = self.calendario.Q_Aula_7.text()
        
        self.quinta = self.calendario.Qi_Aula.text()
        self.quinta2 = self.calendario.Qi_Aula_2.text()
        
        
        
        
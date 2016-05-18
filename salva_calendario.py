# -*- coding: utf-8 -*-
from firebase import firebase
from PyQt4 import QtCore, QtGui
from calendario_novo import Ui_Calendario


firebase = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com")

class Banco_de_Dados:

    def TentativaLogin(self, user, password, dicionario, botao):
        try: 
           self.user == self.dicionario["name"]
           if self.password == self.dicionario["password"]:
                self.login.buttonBox.accepted.connect(self.OKClicked)

           else:
              QtGui.QMessageBox.warning(self, "Erro de validação", "Senha Inválida!")
        except TypeError:
            QtGui.QMessageBox.warning(self, "Erro de validação", "Usuario Inválido")    
    
    
    
    
#    def salvaCaendario(self):
#        self.calendario = Ui_Calendario()
#        self.login = DialogTest()
#        print(self.)
        
        







#    def tentativalogin (self):
#        self.user = self.lineEdit.text()
#        self.password = str(self.lineEdit_2.text())
#        self.dicionario = firebase.get("/users", "/{0}".format(self.user))        
#        try: 
#           self.user == self.dicionario["name"]
#           if self.password == self.dicionario["password"]:
#                self.buttonBox.accepted.connect(self.OKClicked)
#
#           else:
#              QtGui.QMessageBox.warning(self, "Erro de validação", "Senha Inválida!")
#        except TypeError:
#            QtGui.QMessageBox.warning(self, "Erro de validação", "Usuario Inválido")    



#    def BotaoSaveClicked (self):
#        from Login import DialogTest
#        self.Login = DialogTest()
#        
#        self.nome_do_evento = self.novo_evento.lineEdit_3.text()
#        self.data_do_evento = self.novo_evento.dateEdit.text()
##        firebase.put("/users/{0}".format(self.loginAtual))       
#        print(self.nome_do_evento, self.data_do_evento, self.Login.lineEdit.text())
        
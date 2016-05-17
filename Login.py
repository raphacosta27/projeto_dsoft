# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:05:49 2016
"""

import sys
from PyQt4 import QtGui, QtCore
from NovoUsuario import Ui_Dialog
from Janela_principal import Ui_MainWindow
from firebase import firebase


firebase = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com")

class DialogTest(QtGui.QDialog):
    def __init__(self):
        super(DialogTest, self).__init__()
        
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinimizeButtonHint)
        
        self.setupUi()


        
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(292, 148)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 271, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 20, 31, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 31, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(90, 110, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.rejected.connect(self.CancelClicked)
        self.buttonBox.accepted.connect(self.tentativalogin)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.NovoUsuarioClicked)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Login"))
        self.groupBox.setTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Senha"))
        self.pushButton.setText(_translate("Dialog", "Novo Usuário"))
        

    def tentativalogin (self):
        self.user = self.lineEdit.text()
        self.password = str(self.lineEdit_2.text())
        self.dicionario = firebase.get("/users", "/{0}".format(self.user))        
        try: 
           self.user == self.dicionario["name"]
           if self.password == self.dicionario["password"]:
                self.buttonBox.accepted.connect(self.OKClicked)

           else:
              QtGui.QMessageBox.warning(self, "Erro de validação", "Senha Inválida!")
        except TypeError:
            QtGui.QMessageBox.warning(self, "Erro de validação", "Usuario Inválido")    
              
                
    def NovoUsuarioClicked(self):   
        self.window =  Ui_Dialog()
        self.window.show()
        
    def CancelClicked(self):
        self.close()
        
    def OKClicked(self):
        self.janela = Ui_MainWindow()
        self.janela.show()


# firebase.get("1","2") #Pegar do dicionario 2, dentro do dicionario 1
# firebase.put("2", name="name", data="data") #Adicionar no dicionario, a chave name como valor data


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dialogtest = DialogTest()
    dialogtest.show()
    sys.exit(app.exec_())
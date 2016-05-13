# -*- coding: utf-8 -*-

from firebase import firebase
from PyQt4 import QtCore, QtGui
import sys

firebase = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com")


class fillperfil:
    def __init__(self):
        super(fillperfil, self).__init__()
        self.textoComboBox()
        
    def textoComboBox(self):

        self.nome_dos_usuarios = []
        self.dicionario = firebase.get("/users", None)
        for usuario in self.dicionario:
            self.nome_dos_usuarios.append(usuario)
        print(self.nome_dos_usuarios)    
        return self.nome_dos_usuarios
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    yo = fillperfil()
    sys.exit(app.exec_())

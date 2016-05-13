# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NovoUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from firebase import firebase 
import sys
from perfil import Ui_JanelPerfil

firebase = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com")

class Ui_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
    

        self.setupUi()
        
        self.perfilnovoaluno = Ui_JanelPerfil()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setEnabled(True)
        self.resize(784, 574)
        self.setMouseTracking(True) 
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setAutoFillBackground(False)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 651, 541))
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(490, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(480, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 201, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 211, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 421, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 171, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 141, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 391, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 110, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 110, 361, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(140, 160, 91, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 190, 121, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(140, 220, 111, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(510, 160, 91, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(590, 160, 91, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(270, 160, 91, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(270, 190, 91, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_8.setGeometry(QtCore.QRect(510, 190, 91, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_9.setGeometry(QtCore.QRect(270, 220, 91, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_10.setGeometry(QtCore.QRect(510, 220, 91, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_11.setGeometry(QtCore.QRect(360, 160, 91, 17))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_12.setGeometry(QtCore.QRect(360, 190, 141, 17))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_13.setGeometry(QtCore.QRect(360, 220, 131, 17))
        self.checkBox_13.setObjectName("checkBox_13")
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 290, 631, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 320, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(350, 320, 181, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(530, 320, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 350, 431, 20))
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 370, 631, 71))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(480, 510, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(180, 510, 211, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 450, 31, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(40, 450, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(180, 450, 41, 20))
        self.label_14.setObjectName("label_14")
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(220, 450, 113, 20))
        self.lineEdit_10.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(370, 450, 101, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(480, 450, 113, 20))
        self.lineEdit_11.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.buttonBox.rejected.connect(self.CancelClicked)
        

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Novo Usuário"))
        self.groupBox.setTitle(_translate("Dialog", "Novo Usuário"))
        self.label.setText(_translate("Dialog", "Nome: "))
        self.label_2.setText(_translate("Dialog", "Idade:"))
        self.label_3.setText(_translate("Dialog", "Email (Inper):"))
        self.label_4.setText(_translate("Dialog", "Telefone: "))
        self.label_5.setText(_translate("Dialog", "Algumas informações sobre você !"))
        self.label_6.setText(_translate("Dialog", "Entidades que participa:"))
        self.label_7.setText(_translate("Dialog", "Deixe aqui o link do seu perfil no Facebook para caso as pessoas queiram te adicionar !"))
        self.label_8.setText(_translate("Dialog", "Seu Nome de Usuário no Snapchat:"))
        self.label_9.setText(_translate("Dialog", "Redes Sociais"))
        self.checkBox.setText(_translate("Dialog", "Atlética Insper"))
        self.checkBox_2.setText(_translate("Dialog", "Diretório Acadêmico"))
        self.checkBox_3.setText(_translate("Dialog", "Design Challenge"))
        self.checkBox_4.setText(_translate("Dialog", "GAS"))
        self.checkBox_5.setText(_translate("Dialog", "AISEC"))
        self.checkBox_6.setText(_translate("Dialog", "Infinance"))
        self.checkBox_7.setText(_translate("Dialog", "Bateria"))
        self.checkBox_8.setText(_translate("Dialog", "Enactus"))
        self.checkBox_9.setText(_translate("Dialog", "Bem gasto"))
        self.checkBox_10.setText(_translate("Dialog", "Insper Jr."))
        self.checkBox_11.setText(_translate("Dialog", "Insper Post"))
        self.checkBox_12.setText(_translate("Dialog", "Liga de Empreendedores"))
        self.checkBox_13.setText(_translate("Dialog", "Sementes Culturais"))
        self.label_10.setText(_translate("Dialog", "Seu Nome de Usuário no Instagram:"))
        self.label_11.setText(_translate("Dialog", "Escreva aqui mais alguma informação que você deseja que as pessoas saibam sobre você:"))
        self.label_12.setText(_translate("Dialog", "Seja bem-vindo a família Engenharia 1 º B !"))
        self.label_13.setText(_translate("Dialog", "Login:"))
        self.label_14.setText(_translate("Dialog", "Senha:"))
        self.label_15.setText(_translate("Dialog", "Confirme sua senha:"))
        self.buttonBox.accepted.connect(self.ConfirmaSenha)
        
    
    def CancelClicked (self):
        self.close()
        
        
    def NovoUser(self):
                
        
        
        self.new_user = self.lineEdit_9.text()
        self.new_password = self.lineEdit_10.text()
        
        self.nome = self.lineEdit.text()
        self.idade = self.lineEdit_2.text()
        self.email = self.lineEdit_4.text()
        self.telefone = self.lineEdit_3.text()
        
        self.facebook = self.lineEdit_5.text()
        self.snapchat = self.lineEdit_6.text()
        self.instagram = self.lineEdit_7.text()
        self.add_information = self.lineEdit_8.text()

        user_count = firebase.get("/userCount", "/count")
        user_count += 1
        firebase.put("/userCount",name = "count", data = user_count)

        firebase.put("/users/", name = self.new_user, data = {'name' : self.new_user, 'password' : self.new_password, 'nome': self.nome, 'idade': self.idade, 'email' : self.email, 'telefone' : self.telefone,
        'facebook': self.facebook, 'snapchat': self.snapchat, 'instagram': self.instagram, 'adicional': self.add_information, 'entidade': "-"})
        
        self.checkButtons
        
    def checkButtons(self):
            
        if self.checkBox.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades", data = self.checkBox.text())
        

        if self.checkBox_2.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades1", data = self.checkBox_2.text())

        if self.checkBox_3.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades2", data = self.checkBox_3.text())

            
        if self.checkBox_4.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades3", data = self.checkBox_4.text())

        if self.checkBox_5.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades4", data = self.checkBox_5.text())

        if self.checkBox_6.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades5", data = self.checkBox_6.text())

            
        if self.checkBox_7.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades6", data = self.checkBox_7.text())

            
        if self.checkBox_8.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades7", data = self.checkBox_8.text())

            
        if self.checkBox_9.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades8", data = self.checkBox_9.text())

        if self.checkBox_10.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades9", data = self.checkBox_10.text())

        if self.checkBox_11.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades10", data = self.checkBox_11.text())

            
        if self.checkBox_12.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades11", data = self.checkBox_12.text())

            
        if self.checkBox_13.isChecked():
            firebase.put("/users/{0}/entidade".format(self.new_user), name = "entidades12", data = self.checkBox_13.text())   
            
        self.close()
    
#    def UsuarioNaoRepete(self):
#         user_count = firebase.get("/userCount", "/count")
#         UsuarioCadastrando = self.lineEdit_9.text()
#    
#         for i in range (user_count):
#             if UsuarioCadastrando == 
        
    def ConfirmaSenha (self):
        self.senha_1 = self.lineEdit_10.text()
        self.senha_confirma = self.lineEdit_11.text()
        
        if self.senha_1 == self.senha_confirma:
            self.NovoUser()
            self.checkButtons()
        else:
            QtGui.QMessageBox.warning(self, "Erro na confirmação", "As senhas não coincidem")

        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    novousuario = Ui_Dialog()
    novousuario.show()
    sys.exit(app.exec_())


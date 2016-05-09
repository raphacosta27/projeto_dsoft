# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perfildosalunos.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys

class JanelaPerfil (QtGui.QWidget):
    def __init__ (self):
        super(JanelaPerfil, self).__init__()
        
        self.setupUi()
        

        
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(885, 685)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(370, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.treeWidget = QtGui.QTreeWidget(self)
        self.treeWidget.setGeometry(QtCore.QRect(20, 60, 851, 611))
        self.treeWidget.setObjectName("treeWidget")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.treeWidget = QtGui.QTreeWidget(self)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.move(20,60)
        self.treeWidget.resize(700,400)
        
#        self.item = QtGui.QTreeWidgetItem(["hello world"])
#        self.item.addChild(QtGui.QTreeWidgetItem(["Hello"]))
#        
#        self.treeWidget.addTopLevelItem(self.item)

        
        
#        _translate = QtCore.QCoreApplication.translate
#        self.setWindowTitle(_translate("Form", "Form"))
#        self.label.setText(_translate("Form", "Perfil dos alunos"))
#        self.treeWidget.headerItem().setText(0, _translate("Form", "Nome"))
#        self.treeWidget.headerItem().setText(1, _translate("Form", "Idade"))
#        self.treeWidget.headerItem().setText(2, _translate("Form", "Telefone"))
#        self.treeWidget.headerItem().setText(3, _translate("Form", "Email"))
#        self.treeWidget.headerItem().setText(4, _translate("Form", "Entidades"))
#        self.treeWidget.headerItem().setText(5, _translate("Form", "Facebook"))
#        self.treeWidget.headerItem().setText(6, _translate("Form", "Snapchat"))
#        self.treeWidget.headerItem().setText(7, _translate("Form", "Instagram"))
#        
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    perfil = JanelaPerfil()
    perfil.show()
    sys.exit(app.exec_())

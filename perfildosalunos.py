# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perfildosalunos.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(885, 685)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(20, 60, 851, 611))
        self.treeWidget.setObjectName("treeWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Perfil dos alunos"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Nome"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Idade"))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Telefone"))
        self.treeWidget.headerItem().setText(3, _translate("Form", "Email"))
        self.treeWidget.headerItem().setText(4, _translate("Form", "Entidades"))
        self.treeWidget.headerItem().setText(5, _translate("Form", "Facebook"))
        self.treeWidget.headerItem().setText(6, _translate("Form", "Snapchat"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_event.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

class Ui_aba_addevento(QtGui.QWidget):
    def __init__ (self):
        super(Ui_aba_addevento, self).__init__()
       
        self.setupUi()
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(273, 90)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Adicionar evento"))
        self.label.setText(_translate("Form", "Adicionar evento"))
        self.pushButton.setText(_translate("Form", "Salvar"))
        self.label_2.setText(_translate("Form", "Nome"))
        self.label_3.setText(_translate("Form", "Exemplo: Palestra GDE (Sala Olavo Setubal)"))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    teste = Ui_aba_addevento()
    teste.show()
    sys.exit(app.exec_())
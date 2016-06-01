from PyQt4 import QtCore, QtGui

class Ui_Widget_sobre(object):
    def setupUi(self):
        self.setObjectName("Widget_sobre")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagens/img_icones/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_tela_sobre = QtGui.QLabel(self)
        self.bg_tela_sobre.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_tela_sobre.setStyleSheet("background-image: url(:/tela_sobre/Imagens/img_bg/tela_sobre.png);")
        self.bg_tela_sobre.setText("")
        self.bg_tela_sobre.setObjectName("bg_tela_sobre")
        self.botao_link_stackoverflow = QtGui.QCommandLinkButton(self)
        self.botao_link_stackoverflow.setGeometry(QtCore.QRect(323, 268, 151, 20))
        self.botao_link_stackoverflow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Imagens/img_botoes/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_link_stackoverflow.setIcon(icon1)
        self.botao_link_stackoverflow.setObjectName("botao_link_stackoverflow")
        self.botao_voltar_sobre = QtGui.QCommandLinkButton(self)
        self.botao_voltar_sobre.setGeometry(QtCore.QRect(7, 439, 91, 34))
        self.botao_voltar_sobre.setText("")
        self.botao_voltar_sobre.setIcon(icon1)
        self.botao_voltar_sobre.setObjectName("botao_voltar_sobre")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Widget_sobre", "Integrator"))

import tela_sobre_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_servicos_recomendados.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_tela_servicos_recomendados(object):
    def setupUi(self):
        self.setObjectName("tela_servicos_recomendados")
        self.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagens/img_icones/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_servicos_recomendados = QtGui.QLabel(self)
        self.bg_servicos_recomendados.setGeometry(QtCore.QRect(-1, 0, 640, 480))
        self.bg_servicos_recomendados.setStyleSheet("background-image: url(:/tela_servicos_recomendados/Imagens/img_bg/tela_servicos_recomendados.png);")
        self.bg_servicos_recomendados.setText("")
        self.bg_servicos_recomendados.setObjectName("bg_servicos_recomendados")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_servicos_recomendados", "Integrator"))

import tela_servicos_recomendados_rc

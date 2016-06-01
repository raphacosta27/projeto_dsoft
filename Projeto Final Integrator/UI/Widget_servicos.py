from PyQt4 import QtCore, QtGui

class Ui_tela_servicos(object):
    def setupUi(self):
        self.setObjectName("tela_servicos")
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
        self.bg_servicos = QtGui.QLabel(self)
        self.bg_servicos.setGeometry(QtCore.QRect(-2, 0, 640, 480))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg_servicos.sizePolicy().hasHeightForWidth())
        self.bg_servicos.setSizePolicy(sizePolicy)
        self.bg_servicos.setMinimumSize(QtCore.QSize(640, 480))
        self.bg_servicos.setMaximumSize(QtCore.QSize(640, 480))
        self.bg_servicos.setStyleSheet("background-image: url(:/tela_servicos/Imagens/img_bg/tela_servicos.png);")
        self.bg_servicos.setText("")
        self.bg_servicos.setObjectName("bg_servicos")
        self.webview_mapagoogle = QtWebKitWidgets.QWebView(self)
        self.webview_mapagoogle.setGeometry(QtCore.QRect(10, 12, 616, 406))
        self.webview_mapagoogle.setUrl(QtCore.QUrl("about:blank"))
        self.webview_mapagoogle.setObjectName("webview_mapagoogle")
        self.botao_lugares_reco = QtGui.QCommandLinkButton(self)
        self.botao_lugares_reco.setGeometry(QtCore.QRect(4, 436, 92, 37))
        self.botao_lugares_reco.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Imagens/img_botoes/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_lugares_reco.setIcon(icon1)
        self.botao_lugares_reco.setObjectName("botao_lugares_reco")
        self.botao_voltar_servicos = QtGui.QCommandLinkButton(self)
        self.botao_voltar_servicos.setGeometry(QtCore.QRect(522, 436, 110, 37))
        self.botao_voltar_servicos.setText("")
        self.botao_voltar_servicos.setIcon(icon1)
        self.botao_voltar_servicos.setObjectName("botao_voltar_servicos")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_servicos", "Integrator"))

from PyQt5 import QtWebKitWidgets
import tela_servicos_rc

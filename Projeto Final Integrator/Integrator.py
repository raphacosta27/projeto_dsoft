from PyQt4 import QtCore, QtGui
from firebase import firebase 

import tela_login_rc #Arquivo Resource da tela de login convertido em Py
import tela_principal_rc #Arquivo Resource da tela menu convertido em Py
import tela_cadastro_rc
import tela_servicos_rc
import tela_servicos_recomendados_rc
import tela_sobre_rc
import tela_editarperfil_rc
import tela_perfil_rc
import tela_sobre_rc
import tela_calendario_rc

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        self.setupUi()  
        
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.Widget_login = QtGui.QWidget(self)
        self.Widget_login.setObjectName("Widget_login")
        self.botao_enviar = QtGui.QCommandLinkButton(self.Widget_login)
        self.botao_enviar.setGeometry(QtCore.QRect(474, 203, 46, 44))
        self.botao_enviar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_enviar.setIcon(icon1)
        self.botao_enviar.setIconSize(QtCore.QSize(42, 42))
        self.botao_enviar.setObjectName("botao_enviar")
        self.input_password = QtGui.QLineEdit(self.Widget_login)
        self.input_password.setGeometry(QtCore.QRect(192, 233, 270, 32))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(14)
        self.input_password.setFont(font)
        self.input_password.setMaxLength(15)
        self.input_password.setFrame(False)
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.input_user = QtGui.QLineEdit(self.Widget_login)
        self.input_user.setGeometry(QtCore.QRect(191, 185, 270, 32))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(14)
        self.input_user.setFont(font)
        self.input_user.setMaxLength(15)
        self.input_user.setFrame(False)
        self.input_user.setEchoMode(QtGui.QLineEdit.Normal)
        self.input_user.setObjectName("input_user")
        self.botao_esqueci = QtGui.QCommandLinkButton(self.Widget_login)
        self.botao_esqueci.setGeometry(QtCore.QRect(197, 289, 120, 16))
        self.botao_esqueci.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botao_cadastro - 149x24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_esqueci.setIcon(icon2)
        self.botao_esqueci.setIconSize(QtCore.QSize(149, 24))
        self.botao_esqueci.setObjectName("botao_esqueci")
        self.botao_novouser = QtGui.QCommandLinkButton(self.Widget_login)
        self.botao_novouser.setGeometry(QtCore.QRect(344, 281, 148, 27))
        self.botao_novouser.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botao_cadastro - 149x24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_novouser.setIcon(icon3)
        self.botao_novouser.setIconSize(QtCore.QSize(149, 24))
        self.botao_novouser.setObjectName("botao_novouser")
        self.bg_login = QtGui.QLabel(self.Widget_login)
        self.bg_login.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_login.setStyleSheet("background-image: url(:/tela_login/Imagens/img_bg/background_telalogin.png);")
        self.bg_login.setText("")
        self.bg_login.setObjectName("bg_login")
        self.bg_login.raise_()
        self.input_user.raise_()
        self.input_password.raise_()
        self.botao_novouser.raise_()
        self.botao_esqueci.raise_()
        self.botao_enviar.raise_()
        self.setCentralWidget(self.Widget_login)
        self.botao_enviar.clicked.connect(self.tentativalogin)
        self.botao_novouser.clicked.connect(self.novousuario)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.input_user, self.input_password)
        self.setTabOrder(self.input_password, self.botao_enviar)
        self.setTabOrder(self.botao_enviar, self.botao_novouser)
        self.setTabOrder(self.botao_novouser, self.botao_esqueci)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Integrator"))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    def tentativalogin (self):
        self.user = self.input_user.text()
        self.password = str(self.input_password.text())
        self.dicionario = self.fb.get("/users", "/{0}".format(self.user))
        if not self.user:
            QtGui.QMessageBox.warning(self, 'Erro de validação', 'Usuário faltando')
        elif not self.password:
            QtGui.QMessageBox.warning(self, 'Erro de validação', 'Senha faltando')
        else:  
            try:  
                if self.user == self.dicionario["name"] and self.password == self.dicionario["password"]:
                    Main = MainWindow(self)
                    self.botao_enviar.clicked.connect(self.login)
                else:
                    QtGui.QMessageBox.warning(self, "Erro de validação", "Senha Inválida!")
            except TypeError:
                QtGui.QMessageBox.warning(self, "Erro de validação", "Usuario Inválido")

    def login(self): #Função que vai para o MENU
        self.Tela_menu = LoggedWidget(self)
        self.setCentralWidget(self.Tela_menu)

    def novousuario(self): #Função que vai para o CADASTRO
    	self.cadastro = Widget_Cadastro(self)
    	self.setCentralWidget(self.cadastro)

    def voltar_login(self): #Função que volta para o LOGIN
        self.setupUi()
        self.setCentralWidget(self.Widget_login)
        
    def abrir_servicos(self): #Função que vai para o SERVIÇOS
        servicos = Widget_Servicos(self)
        self.setCentralWidget(servicos)

    def Servicos_reco_click(self): #Função que vai para o SERVIÇOS RECOMENDADOS
        self.servicos_reco = Widget_Servicos_recomendados()
        self.servicos_reco.show()

    def abrir_editar_perfil(self): #Função que vai para o EDITAR PERFIL
        editar_perfil = Widget_editar_perfil(self)
        self.setCentralWidget(editar_perfil)

    def abrir_usuarios(self): #Função que vai para o PERFIL
        tela_perfis = Widget_perfil(self)
        self.setCentralWidget(tela_perfis)

    def abrir_infos(self): #Função que vai para o PERFIL
        tela_sobre = Widget_sobre(self)
        self.setCentralWidget(tela_sobre)

    def abrir_calendario(self):
        tela_calendario = Widget_calendario(self)
        self.setCentralWidget(tela_calendario)

    def abrir_abas(self):
    	self.tela_abas = Widget_abas()
    	self.tela_abas.show()
        
        
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class LoggedWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(LoggedWidget, self).__init__(parent)
        self.setupUi()
        self.fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")

    def setupUi(self):
        self.setObjectName("Inicial")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("")
        self.botao_servicos = QtGui.QCommandLinkButton(self)
        self.botao_servicos.setGeometry(QtCore.QRect(186, 111, 270, 135))
        self.botao_servicos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaog - 269x135.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_servicos.setIcon(icon1)
        self.botao_servicos.setIconSize(QtCore.QSize(42, 42))
        self.botao_servicos.setObjectName("botao_servicos")
        self.bg_inicial = QtGui.QLabel(self)
        self.bg_inicial.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_inicial.setStyleSheet("background-image: url(:/tela_principal/Imagens/img_bg/background_telainicial.png);")
        self.bg_inicial.setText("")
        self.bg_inicial.setObjectName("bg_inicial")
        self.botao_calendario = QtGui.QCommandLinkButton(self)
        self.botao_calendario.setGeometry(QtCore.QRect(187, 261, 270, 135))
        self.botao_calendario.setText("")
        self.botao_calendario.setIcon(icon1)
        self.botao_calendario.setIconSize(QtCore.QSize(42, 42))
        self.botao_calendario.setObjectName("botao_calendario")
        self.botao_infos = QtGui.QCommandLinkButton(self)
        self.botao_infos.setGeometry(QtCore.QRect(469, 111, 150, 135))
        self.botao_infos.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaop - 150x135.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_infos.setIcon(icon2)
        self.botao_infos.setIconSize(QtCore.QSize(42, 42))
        self.botao_infos.setObjectName("botao_infos")
        self.botao_usuarios = QtGui.QCommandLinkButton(self)
        self.botao_usuarios.setGeometry(QtCore.QRect(21, 113, 150, 135))
        self.botao_usuarios.setText("")
        self.botao_usuarios.setIcon(icon2)
        self.botao_usuarios.setIconSize(QtCore.QSize(42, 42))
        self.botao_usuarios.setObjectName("botao_usuarios")
        self.botao_editarperfil = QtGui.QCommandLinkButton(self)
        self.botao_editarperfil.setGeometry(QtCore.QRect(21, 261, 150, 135))
        self.botao_editarperfil.setText("")
        self.botao_editarperfil.setIcon(icon2)
        self.botao_editarperfil.setIconSize(QtCore.QSize(42, 42))
        self.botao_editarperfil.setObjectName("botao_editarperfil")
        self.bg_inicial.raise_()
        self.botao_servicos.raise_()
        self.botao_calendario.raise_()
        self.botao_infos.raise_()
        self.botao_usuarios.raise_()
        self.botao_editarperfil.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        self.botao_servicos.clicked.connect(self.parent().abrir_servicos)
        self.botao_editarperfil.clicked.connect(self.parent().abrir_editar_perfil)
        self.botao_usuarios.clicked.connect(self.parent().abrir_usuarios)
        self.botao_infos.clicked.connect(self.parent().abrir_infos)
        self.botao_calendario.clicked.connect(self.parent().abrir_calendario)        

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Inicial", "Integrator"))

class Widget_Cadastro(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_Cadastro, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Widget_Cadastro")
        self.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setAutoFillBackground(True)
        self.bg_cadastro = QtGui.QLabel(self)
        self.bg_cadastro.setEnabled(True)
        self.bg_cadastro.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_cadastro.setStyleSheet("background-image: url(:/bg/Imagens/img_bg/tela_cadastro.png);")
        self.bg_cadastro.setText("")
        self.bg_cadastro.setObjectName("bg_cadastro")

        self.input_snapchat = QtGui.QLineEdit(self)
        self.input_snapchat.setGeometry(QtCore.QRect(504, 387, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_snapchat.setFont(font)
        self.input_snapchat.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_snapchat.setFrame(False)
        self.input_snapchat.setObjectName("input_snapchat")

        self.input_instagram = QtGui.QLineEdit(self)
        self.input_instagram.setGeometry(QtCore.QRect(324, 388, 124, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_instagram.setFont(font)
        self.input_instagram.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_instagram.setFrame(False)
        self.input_instagram.setObjectName("input_instagram")

        self.input_fb = QtGui.QLineEdit(self)
        self.input_fb.setGeometry(QtCore.QRect(50, 389, 216, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_fb.setFont(font)
        self.input_fb.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_fb.setFrame(False)
        self.input_fb.setObjectName("input_fb")

        self.combo_curso = QtGui.QComboBox(self)
        self.combo_curso.setGeometry(QtCore.QRect(68, 180, 352, 22))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.combo_curso.setFont(font)
        self.combo_curso.setObjectName("combo_curso")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/adm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/eco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/comp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/mec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/meca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon5, "")

        self.combo_semestre = QtGui.QComboBox(self)
        self.combo_semestre.setGeometry(QtCore.QRect(521, 180, 104, 22))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.combo_semestre.setFont(font)
        self.combo_semestre.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combo_semestre.setFrame(True)
        self.combo_semestre.setObjectName("combo_semestre")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")

        self.input_nome = QtGui.QLineEdit(self)
        self.input_nome.setGeometry(QtCore.QRect(75, 40, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_nome.setFont(font)
        self.input_nome.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_nome.setFrame(False)
        self.input_nome.setEchoMode(QtGui.QLineEdit.Normal)
        self.input_nome.setObjectName("input_nome")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        Validador_nome_reg = QtCore.QRegExp("[^0-9\.\,\"\?\!\;\:\#\$\%\&\(\)\*\+\-\/\<\>\=\@\[\]\\\^\_\{\}\|\~]+")
        Nome_valitador = QtGui.QRegExpValidator(Validador_nome_reg, self.input_nome)
        self.input_nome.setValidator(Nome_valitador)
        self.input_nome.setPlaceholderText("Digite seu nome completo")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.input_nasci = QtGui.QDateEdit(self)
        self.input_nasci.setGeometry(QtCore.QRect(548, 40, 78, 22))
        self.input_nasci.setFrame(False)
        self.input_nasci.setReadOnly(False)
        self.input_nasci.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.input_nasci.setDate(QtCore.QDate(1997, 1, 1))
        self.input_nasci.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(23, 59, 59)))
        self.input_nasci.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 9, 14), QtCore.QTime(0, 0, 0)))
        self.input_nasci.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.input_nasci.setCalendarPopup(False)
        self.input_nasci.setObjectName("input_nasci")

        self.input_newuser = QtGui.QLineEdit(self)
        self.input_newuser.setGeometry(QtCore.QRect(82, 85, 116, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_newuser.setFont(font)
        self.input_newuser.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_newuser.setFrame(False)
        self.input_newuser.setObjectName("input_newuser")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        Validador_user_reg = QtCore.QRegExp("[a-z]+")
        User_validator = QtGui.QRegExpValidator(Validador_user_reg, self.input_newuser)
        self.input_newuser.setValidator(User_validator)
        self.input_newuser.setPlaceholderText("a-z")
        # self.input_newuser.setValidator(self.validator_usuario)
        # self.input_newuser.textChanged.connect(self.check_state_usuario)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.input_newpw = QtGui.QLineEdit(self)
        self.input_newpw.setGeometry(QtCore.QRect(270, 86, 103, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_newpw.setFont(font)
        self.input_newpw.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.input_newpw.setText("")
        self.input_newpw.setMaxLength(15)
        self.input_newpw.setFrame(False)
        self.input_newpw.setEchoMode(QtGui.QLineEdit.Password)
        self.input_newpw.setObjectName("input_newpw")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        Validador_senha_reg = QtCore.QRegExp("\w+")
        Senha_validator = QtGui.QRegExpValidator(Validador_senha_reg, self.input_newpw)
        self.input_newpw.setValidator(Senha_validator)
        self.input_newpw.setPlaceholderText("a-z e 0-9")
        # self.input_newpw.setValidator(self.validator_senha)
        # self.input_newpw.textChanged.connect(self.check_state_senha)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.input_newpw_conf = QtGui.QLineEdit(self)
        self.input_newpw_conf.setGeometry(QtCore.QRect(521, 85, 103, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_newpw_conf.setFont(font)
        self.input_newpw_conf.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.input_newpw_conf.setText("")
        self.input_newpw_conf.setMaxLength(15)
        self.input_newpw_conf.setFrame(False)
        self.input_newpw_conf.setEchoMode(QtGui.QLineEdit.Password)
        self.input_newpw_conf.setObjectName("input_newpw_conf")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        Senhaconf_validator = QtGui.QRegExpValidator(Validador_senha_reg, self.input_newpw_conf)
        self.input_newpw_conf.setValidator(Senhaconf_validator)
        self.input_newpw_conf.setPlaceholderText("a-z e 0-9")
        # self.input_newpw_conf.setValidator(self.validator_confsenha)
        # self.input_newpw_conf.textChanged.connect(self.check_state_senha)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.input_email = QtGui.QLineEdit(self)
        self.input_email.setGeometry(QtCore.QRect(63, 351, 314, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_email.setFont(font)
        self.input_email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_email.setFrame(False)
        self.input_email.setObjectName("input_email")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        
        Validador_email_reg = QtCore.QRegExp("^([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}$")
        email_validator = QtGui.QRegExpValidator(Validador_email_reg, self.input_email)
        self.input_email.setValidator(email_validator)
        self.input_email.setPlaceholderText("fulano@al.insper.edu.br")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#                

        self.input_telefone = QtGui.QLineEdit(self)
        self.input_telefone.setGeometry(QtCore.QRect(471, 352, 152, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_telefone.setFont(font)
        self.input_telefone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_telefone.setFrame(False)
        self.input_telefone.setObjectName("input_telefone")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        Validador_telefone_reg = QtCore.QRegExp("(?:^\([0]?[1-9]{2}\)|^[0]?[1-9]{2}[\.-\s]?)[9]?[1-9]\d{3}[\.-\s]?\d{4}$")
        Telefone_validator = QtGui.QRegExpValidator(Validador_telefone_reg, self.input_telefone)
        self.input_telefone.setValidator(Telefone_validator)
        self.input_telefone.setPlaceholderText("Ex: (11)92222-3333")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.check_atletica = QtGui.QCheckBox(self)
        self.check_atletica.setGeometry(QtCore.QRect(20, 238, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_atletica.setFont(font)
        self.check_atletica.setObjectName("check_atletica")

        self.check_aisec = QtGui.QCheckBox(self)
        self.check_aisec.setGeometry(QtCore.QRect(20, 258, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_aisec.setFont(font)
        self.check_aisec.setObjectName("check_aisec")

        self.check_bateria = QtGui.QCheckBox(self)
        self.check_bateria.setGeometry(QtCore.QRect(20, 278, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_bateria.setFont(font)
        self.check_bateria.setObjectName("check_bateria")

        self.check_bemgasto = QtGui.QCheckBox(self)
        self.check_bemgasto.setGeometry(QtCore.QRect(20, 298, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_bemgasto.setFont(font)
        self.check_bemgasto.setObjectName("check_bemgasto")

        self.check_designchallenge = QtGui.QCheckBox(self)
        self.check_designchallenge.setGeometry(QtCore.QRect(190, 258, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_designchallenge.setFont(font)
        self.check_designchallenge.setObjectName("check_designchallenge")

        self.check_da = QtGui.QCheckBox(self)
        self.check_da.setGeometry(QtCore.QRect(190, 278, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_da.setFont(font)
        self.check_da.setObjectName("check_da")

        self.check_infinance = QtGui.QCheckBox(self)
        self.check_infinance.setGeometry(QtCore.QRect(390, 238, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_infinance.setFont(font)
        self.check_infinance.setObjectName("check_infinance")

        self.check_junior = QtGui.QCheckBox(self)
        self.check_junior.setGeometry(QtCore.QRect(390, 258, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_junior.setFont(font)
        self.check_junior.setObjectName("check_junior")

        self.check_post = QtGui.QCheckBox(self)
        self.check_post.setGeometry(QtCore.QRect(390, 278, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_post.setFont(font)
        self.check_post.setObjectName("check_post")

        self.check_ligaemp = QtGui.QCheckBox(self)
        self.check_ligaemp.setGeometry(QtCore.QRect(390, 298, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_ligaemp.setFont(font)
        self.check_ligaemp.setObjectName("check_ligaemp")

        self.check_consilium = QtGui.QCheckBox(self)
        self.check_consilium.setGeometry(QtCore.QRect(190, 238, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_consilium.setFont(font)
        self.check_consilium.setObjectName("check_consilium")

        self.check_enactus = QtGui.QCheckBox(self)
        self.check_enactus.setGeometry(QtCore.QRect(190, 298, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_enactus.setFont(font)
        self.check_enactus.setObjectName("check_enactus")

        self.check_gas = QtGui.QCheckBox(self)
        self.check_gas.setGeometry(QtCore.QRect(190, 318, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_gas.setFont(font)
        self.check_gas.setObjectName("check_gas")

        self.check_sementes = QtGui.QCheckBox(self)
        self.check_sementes.setGeometry(QtCore.QRect(390, 318, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_sementes.setFont(font)
        self.check_sementes.setObjectName("check_sementes")

        self.botao_fb = QtGui.QCommandLinkButton(self)
        self.botao_fb.setGeometry(QtCore.QRect(11, 384, 27, 27))
        self.botao_fb.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_fb.setIcon(icon6)
        self.botao_fb.setIconSize(QtCore.QSize(27, 27))
        self.botao_fb.setObjectName("botao_fb")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        import webbrowser
        self.botao_fb.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/profile.php'))
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.botao_cadastrar = QtGui.QCommandLinkButton(self)
        self.botao_cadastrar.setEnabled(True)
        self.botao_cadastrar.setGeometry(QtCore.QRect(564, 412, 66, 65))
        self.botao_cadastrar.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botao_cadastrar_inac.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botao_cadastrar_act.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_cadastrar.setIcon(icon7)
        self.botao_cadastrar.setIconSize(QtCore.QSize(50, 50))
        self.botao_cadastrar.setDescription("")
        self.botao_cadastrar.setObjectName("botao_cadastrar")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_cadastrar.clicked.connect(self.ConfirmaSenha)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.botao_voltar = QtGui.QCommandLinkButton(self)
        self.botao_voltar.setGeometry(QtCore.QRect(7, 437, 91, 36))
        self.botao_voltar.setText("")
        self.botao_voltar.setIcon(icon6)
        self.botao_voltar.setIconSize(QtCore.QSize(27, 27))
        self.botao_voltar.setObjectName("botao_voltar")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_voltar.clicked.connect(self.parent().voltar_login)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#          

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setTabOrder(self.input_nome, self.input_nasci)
        self.setTabOrder(self.input_nasci, self.input_newuser)
        self.setTabOrder(self.input_newuser, self.input_newpw)
        self.setTabOrder(self.input_newpw, self.input_newpw_conf)
        self.setTabOrder(self.input_newpw_conf, self.combo_curso)
        self.setTabOrder(self.combo_curso, self.combo_semestre)
        self.setTabOrder(self.combo_semestre, self.check_atletica)
        self.setTabOrder(self.check_atletica, self.check_aisec)
        self.setTabOrder(self.check_aisec, self.check_bateria)
        self.setTabOrder(self.check_bateria, self.check_bemgasto)
        self.setTabOrder(self.check_bemgasto, self.check_consilium)
        self.setTabOrder(self.check_consilium, self.check_designchallenge)
        self.setTabOrder(self.check_designchallenge, self.check_da)
        self.setTabOrder(self.check_da, self.check_enactus)
        self.setTabOrder(self.check_enactus, self.check_gas)
        self.setTabOrder(self.check_gas, self.check_infinance)
        self.setTabOrder(self.check_infinance, self.check_junior)
        self.setTabOrder(self.check_junior, self.botao_fb)
        self.setTabOrder(self.botao_fb, self.check_post)
        self.setTabOrder(self.check_post, self.check_ligaemp)
        self.setTabOrder(self.check_ligaemp, self.check_sementes)
        self.setTabOrder(self.check_sementes, self.input_email)
        self.setTabOrder(self.input_email, self.input_telefone)
        self.setTabOrder(self.input_telefone, self.input_fb)
        self.setTabOrder(self.input_fb, self.input_instagram)
        self.setTabOrder(self.input_instagram, self.input_snapchat)
        self.setTabOrder(self.input_snapchat, self.botao_voltar)
        self.setTabOrder(self.botao_voltar, self.botao_cadastrar)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Widget_Cadastro", "Cadastro"))
        self.combo_curso.setItemText(0, _translate("Widget_Cadastro", "Administração"))
        self.combo_curso.setItemText(1, _translate("Widget_Cadastro", "Economia"))
        self.combo_curso.setItemText(2, _translate("Widget_Cadastro", "Engenharia da Computação"))
        self.combo_curso.setItemText(3, _translate("Widget_Cadastro", "Engenharia Mecânica"))
        self.combo_curso.setItemText(4, _translate("Widget_Cadastro", "Engenharia Mecatrônica"))
        self.combo_semestre.setItemText(0, _translate("Widget_Cadastro", "1"))
        self.combo_semestre.setItemText(1, _translate("Widget_Cadastro", "2"))
        self.combo_semestre.setItemText(2, _translate("Widget_Cadastro", "3"))
        self.combo_semestre.setItemText(3, _translate("Widget_Cadastro", "4"))
        self.combo_semestre.setItemText(4, _translate("Widget_Cadastro", "5"))
        self.combo_semestre.setItemText(5, _translate("Widget_Cadastro", "6"))
        self.combo_semestre.setItemText(6, _translate("Widget_Cadastro", "7"))
        self.combo_semestre.setItemText(7, _translate("Widget_Cadastro", "8"))
        self.combo_semestre.setItemText(8, _translate("Widget_Cadastro", "9"))
        self.combo_semestre.setItemText(9, _translate("Widget_Cadastro", "10"))
        self.check_atletica.setText(_translate("Widget_Cadastro", "Atlética Insper"))
        self.check_aisec.setText(_translate("Widget_Cadastro", "AISEC"))
        self.check_bateria.setText(_translate("Widget_Cadastro", "Bateria Imperial"))
        self.check_bemgasto.setText(_translate("Widget_Cadastro", "Bem gasto"))
        self.check_designchallenge.setText(_translate("Widget_Cadastro", "Design Challenge"))
        self.check_da.setText(_translate("Widget_Cadastro", "Diretório Acadêmico"))
        self.check_infinance.setText(_translate("Widget_Cadastro", "Infinance"))
        self.check_junior.setText(_translate("Widget_Cadastro", "Insper Junior"))
        self.check_post.setText(_translate("Widget_Cadastro", "Insper Post"))
        self.check_ligaemp.setText(_translate("Widget_Cadastro", "Liga de Empreendedores"))
        self.check_consilium.setText(_translate("Widget_Cadastro", "Consilium Insper"))
        self.check_enactus.setText(_translate("Widget_Cadastro", "Enactus"))
        self.check_gas.setText(_translate("Widget_Cadastro", "Grupo de Ação Social"))
        self.check_sementes.setText(_translate("Widget_Cadastro", "Sementes Culturais"))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    def newuser(self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        self.nome = self.input_nome.text()
        self.data = self.input_nasci.text()
        self.usuario = self.input_newuser.text()
        self.novasenha = self.input_newpw.text()
        self.confnovasenha = self.input_newpw_conf.text()

        self.curso = self.combo_curso.currentText()
        self.semestre = self.combo_semestre.currentText()
        self.email = self.input_email.text()
        self.telefone = self.input_telefone.text()
        self.faceb = self.input_fb.text()
        self.insta = self.input_instagram.text()
        self.snap = self.input_snapchat.text()

        user_count = fb.get("/userCount", "/count")
        user_count += 1
        fb.put("/userCount",name = "count", data = user_count)

        fb.put("/users/", name = self.usuario, data = {'name' : self.usuario, 'password' : self.novasenha, 'nome': self.nome, 'nascimento': self.data, 'email' : self.email, 'telefone' : self.telefone,
        'facebook': self.faceb, 'snapchat': self.snap, 'instagram': self.insta, 'entidade': "-", 'semestre': self.semestre, 'curso': self.curso, 'bairro': '-', 'colegio': '-', 'transporte': '-', 'eventos': {'Exemplo': "31/05/2016"}})

        self.checkButtons

    def checkButtons(self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")

        if self.check_aisec.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades", data = self.check_aisec.text())
        if self.check_atletica.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades1", data = self.check_atletica.text())
        if self.check_bemgasto.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades2", data = self.check_bemgasto.text())           
        if self.check_bateria.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades3", data = self.check_bateria.text())
        if self.check_consilium.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades4", data = self.check_consilium.text())
        if self.check_da.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades5", data = self.check_da.text())            
        if self.check_designchallenge.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades6", data = self.check_designchallenge.text())           
        if self.check_enactus.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades7", data = self.check_enactus.text())           
        if self.check_infinance.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades8", data = self.check_infinance.text())
        if self.check_gas.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades9", data = self.check_gas.text())
        if self.check_junior.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades10", data = self.check_junior.text())            
        if self.check_post.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades11", data = self.check_post.text())           
        if self.check_ligaemp.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades12", data = self.check_ligaemp.text())
        if self.check_sementes.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades13", data = self.check_sementes.text())
            
        QtGui.QMessageBox.warning(self, "Confirmação", "Usuário Cadastrado")    
        self.parent().voltar_login()

    def ConfirmaSenha(self):
        self.nome = self.input_nome.text()
        self.data = self.input_nasci.text()
        self.usuario = self.input_newuser.text()
        self.novasenha = self.input_newpw.text()
        self.confnovasenha = self.input_newpw_conf.text()

        if self.nome != '' and self.usuario != '' and self.novasenha != '' and self.confnovasenha != '':
	        if self.novasenha == self.confnovasenha:
	            self.newuser()
	            self.checkButtons()
	        else:
	            QtGui.QMessageBox.warning(self, "Erro na confirmação", "As senhas não coincidem")
        else:
            QtGui.QMessageBox.warning(self, "Erro no cadastro", "Por favor digite as informações mínimas")

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Widget_Servicos(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_Servicos, self).__init__(parent)
        self.setupUi()

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
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_servicos = QtGui.QLabel(self)
        self.bg_servicos.setGeometry(QtCore.QRect(0, 0, 640, 480))
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

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.webview_mapagoogle = QWebView(self)
        self.webview_mapagoogle.setGeometry(QtCore.QRect(10, 12, 616, 406))
        self.webview_mapagoogle.setUrl(QtCore.QUrl("about:blank"))
        self.webview_mapagoogle.setObjectName("webview_mapagoogle")
        self.webview_mapagoogle.load(QUrl("https://www.google.com.br/maps/@-23.5979074,-46.6773694,16.96z"))
        QtGui.QMessageBox.warning(self, "Alerta", "Espere a página carregar totalmente para mexer")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.botao_lugares_reco = QtGui.QCommandLinkButton(self)
        self.botao_lugares_reco.setGeometry(QtCore.QRect(522, 436, 110, 37))
        self.botao_lugares_reco.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_lugares_reco.setIcon(icon1)
        self.botao_lugares_reco.setObjectName("botao_lugares_reco")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_lugares_reco.clicked.connect(self.parent().Servicos_reco_click)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        


        self.botao_voltar_servicos = QtGui.QCommandLinkButton(self)
        self.botao_voltar_servicos.setGeometry(QtCore.QRect(4, 436, 92, 37))
        self.botao_voltar_servicos.setText("")
        self.botao_voltar_servicos.setIcon(icon1)
        self.botao_voltar_servicos.setObjectName("botao_voltar_servicos")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_voltar_servicos.clicked.connect(self.parent().login)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#         

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_servicos", "Integrator"))    

class Widget_Servicos_recomendados(QtGui.QWidget):
    def __init__ (self):
        super(Widget_Servicos_recomendados, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("tela_servicos_recomendados")
        self.resize(640, 480)
        self.move(300, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_servicos_recomendados = QtGui.QLabel(self)
        self.bg_servicos_recomendados.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_servicos_recomendados.setStyleSheet("background-image: url(:/tela_servicos_recomendados/Imagens/img_bg/tela_servicos_recomendados.png);")
        self.bg_servicos_recomendados.setText("")
        self.bg_servicos_recomendados.setObjectName("bg_servicos_recomendados")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_servicos_recomendados", "Integrator"))

class Widget_editar_perfil(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_editar_perfil, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("tela_editar_perfil")
        self.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_perfil = QtGui.QLabel(self)
        self.bg_perfil.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_perfil.setStyleSheet("background-image: url(:/tela_editarperfil/Imagens/img_bg/tela_editarperfil.png);")
        self.bg_perfil.setText("")
        self.bg_perfil.setObjectName("bg_perfil")

        self.output_nome = QtGui.QLineEdit(self)
        self.output_nome.setGeometry(QtCore.QRect(73, 102, 353, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_nome.setFont(font)
        self.output_nome.setFrame(False)
        self.output_nome.setReadOnly(False)
        self.output_nome.setObjectName("output_nome")

        self.output_email = QtGui.QLineEdit(self)
        self.output_email.setGeometry(QtCore.QRect(271, 63, 353, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_email.setFont(font)
        self.output_email.setFrame(False)
        self.output_email.setReadOnly(False)
        self.output_email.setObjectName("output_email")

        self.output_curso = QtGui.QLineEdit(self)
        self.output_curso.setGeometry(QtCore.QRect(65, 155, 353, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_curso.setFont(font)
        self.output_curso.setFrame(False)
        self.output_curso.setReadOnly(False)
        self.output_curso.setObjectName("output_curso")

        self.output_entidades = QtGui.QLineEdit(self)
        self.output_entidades.setGeometry(QtCore.QRect(195, 365, 427, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_entidades.setFont(font)
        self.output_entidades.setFrame(False)
        self.output_entidades.setReadOnly(True)
        self.output_entidades.setObjectName("output_entidades")

        self.output_colegio = QtGui.QLineEdit(self)
        self.output_colegio.setGeometry(QtCore.QRect(324, 194, 298, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_colegio.setFont(font)
        self.output_colegio.setFrame(False)
        self.output_colegio.setReadOnly(False)
        self.output_colegio.setObjectName("output_colegio")

        self.output_transporte = QtGui.QLineEdit(self)
        self.output_transporte.setGeometry(QtCore.QRect(395, 251, 227, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_transporte.setFont(font)
        self.output_transporte.setFrame(False)
        self.output_transporte.setReadOnly(False)
        self.output_transporte.setObjectName("output_transporte")

        self.output_telefone = QtGui.QLineEdit(self)
        self.output_telefone.setGeometry(QtCore.QRect(82, 192, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_telefone.setFont(font)
        self.output_telefone.setFrame(False)
        self.output_telefone.setReadOnly(False)
        self.output_telefone.setObjectName("output_telefone")

        self.output_bairro = QtGui.QLineEdit(self)
        self.output_bairro.setGeometry(QtCore.QRect(69, 251, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_bairro.setFont(font)
        self.output_bairro.setFrame(False)
        self.output_bairro.setReadOnly(False)
        self.output_bairro.setObjectName("output_bairro")

        self.output_nascimento = QtGui.QLineEdit(self)
        self.output_nascimento.setGeometry(QtCore.QRect(546, 102, 78, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(11)
        self.output_nascimento.setFont(font)
        self.output_nascimento.setFrame(False)
        self.output_nascimento.setReadOnly(False)
        self.output_nascimento.setObjectName("output_nascimento")

        self.output_semestre = QtGui.QLineEdit(self)
        self.output_semestre.setGeometry(QtCore.QRect(516, 155, 104, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_semestre.setFont(font)
        self.output_semestre.setFrame(False)
        self.output_semestre.setReadOnly(False)
        self.output_semestre.setObjectName("output_semestre")

        self.output_snapchat = QtGui.QLineEdit(self)
        self.output_snapchat.setGeometry(QtCore.QRect(503, 307, 118, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_snapchat.setFont(font)
        self.output_snapchat.setFrame(False)
        self.output_snapchat.setReadOnly(False)
        self.output_snapchat.setObjectName("output_snapchat")

        self.output_instagram = QtGui.QLineEdit(self)
        self.output_instagram.setGeometry(QtCore.QRect(323, 310, 123, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_instagram.setFont(font)
        self.output_instagram.setFrame(False)
        self.output_instagram.setReadOnly(False)
        self.output_instagram.setObjectName("output_instagram")

        self.output_facebook = QtGui.QLineEdit(self)
        self.output_facebook.setGeometry(QtCore.QRect(50, 310, 217, 23))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_facebook.setFont(font)
        self.output_facebook.setFrame(False)
        self.output_facebook.setReadOnly(False)
        self.output_facebook.setObjectName("output_facebook")

        self.output_user = QtGui.QLineEdit(self)
        self.output_user.setGeometry(QtCore.QRect(78, 64, 116, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_user.setFont(font)
        self.output_user.setFrame(False)
        self.output_user.setReadOnly(True)
        self.output_user.setObjectName("output_user")

        self.botao_voltar_editarperfil = QtGui.QCommandLinkButton(self)
        self.botao_voltar_editarperfil.setGeometry(QtCore.QRect(10, 436, 90, 37))
        self.botao_voltar_editarperfil.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_voltar_editarperfil.setIcon(icon1)
        self.botao_voltar_editarperfil.setObjectName("botao_voltar_editarperfil")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_voltar_editarperfil.clicked.connect(self.parent().login)

        self.botao_enviaredicoes = QtGui.QCommandLinkButton(self)
        self.botao_enviaredicoes.setGeometry(QtCore.QRect(537, 435, 90, 36))
        self.botao_enviaredicoes.setText("")
        self.botao_enviaredicoes.setIcon(icon1)
        self.botao_enviaredicoes.setObjectName("botao_enviaredicoes")
        self.botao_enviaredicoes.clicked.connect(self.salvar_edit)
        
        self.nome_usuario = self.parent().user
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        
        fbusu = fb.get("/users", "{0}".format(self.nome_usuario))
        
        self.frase = 0
        self.dicientidades = fb.get("/users/{0}".format(self.nome_usuario), "/entidade")
        self.listadeentidades = []
        print(self.dicientidades)
        for v in self.dicientidades.values():
            self.listadeentidades.append(v)
        if len(self.listadeentidades) == 1 :
            self.frase = "{0}".format(self.listadeentidades[0])
        elif len(self.listadeentidades) == 2 :
            self.frase = "{0} e {1}".format(self.listadeentidades[0], self.listadeentidades[1])
        elif len(self.listadeentidades) == 3:
            self.frase = "{0}, {1} e {2}".format(self.listadeentidades[0], self.listadeentidades[1], self.listadeentidades[2])
        else:
            self.frase = "Nenhuma"

        
        self.output_email.setText(fbusu["email"])
        self.output_entidades.setText(self.frase)
        self.output_facebook.setText(fbusu["facebook"])
        self.output_instagram.setText(fbusu["instagram"])
        self.output_nascimento.setText(fbusu["nascimento"])
        self.output_nome.setText(fbusu["nome"])
        self.output_semestre.setText(fbusu["semestre"])
        self.output_snapchat.setText(fbusu["snapchat"])
        self.output_telefone.setText(fbusu["telefone"])
        self.output_transporte.setText(fbusu["transporte"])
        self.output_user.setText(self.nome_usuario)
        self.output_curso.setText(fbusu["curso"])
        self.output_bairro.setText(fbusu["bairro"])
        self.output_colegio.setText(fbusu["colegio"])
        
    
        self.diciteste = {}        
        for v in self.dicientidades:
            for i in self.listadeentidades:
                self.diciteste[v] = i
        print(self.diciteste)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
     
    
        
    def salvar_edit (self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")        
        
        email = self.output_email.text() 
        facebook = self.output_facebook.text() 
        instagram = self.output_instagram.text() 
        nascimento = self.output_nascimento.text() 
        nome = self.output_nome.text() 
        semestre = self.output_semestre.text() 
        snapchat = self.output_snapchat.text() 
        telefone = self.output_telefone.text() 
        transporte = self.output_transporte.text() 
        bairro = self.output_bairro.text() 
        colegio = self.output_colegio.text()
        curso = self.output_curso.text()
        
        fb.put("/users/", name = self.nome_usuario, data = {'entidade': self.diciteste, 'name': self.parent().user,'password': self.parent().password, 'nome': nome, 'nascimento': nascimento, 'email' : email, 'telefone' : telefone,
        'facebook': facebook, 'snapchat': snapchat, 'instagram': instagram, 'semestre': semestre, 'curso': curso, 'bairro': bairro, 'colegio': colegio, 'transporte': transporte, 'eventos': {'Exemplo': '01/01/2016'}})
        QtGui.QMessageBox.warning(self, "Alerta", "Suas informações foram editadas")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_editar_perfil", "Integrator"))


class Widget_perfil(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_perfil, self).__init__(parent)
        self.setupUi()
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")        

    def setupUi(self):
        self.setObjectName("tela_perfil")
        self.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_perfil = QtGui.QLabel(self)
        self.bg_perfil.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_perfil.setStyleSheet("background-image: url(:/tela_perfil/Imagens/img_bg/tela_perfil.png);")
        self.bg_perfil.setText("")
        self.bg_perfil.setObjectName("bg_perfil")

        self.output_nome = QtGui.QLineEdit(self)
        self.output_nome.setGeometry(QtCore.QRect(74, 121, 353, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_nome.setFont(font)
        self.output_nome.setFrame(False)
        self.output_nome.setReadOnly(True)
        self.output_nome.setObjectName("output_nome")

        self.output_email = QtGui.QLineEdit(self)
        self.output_email.setGeometry(QtCore.QRect(270, 84, 353, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_email.setFont(font)
        self.output_email.setFrame(False)
        self.output_email.setReadOnly(True)
        self.output_email.setObjectName("output_email")

        self.output_curso = QtGui.QLineEdit(self)
        self.output_curso.setGeometry(QtCore.QRect(64, 176, 353, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_curso.setFont(font)
        self.output_curso.setFrame(False)
        self.output_curso.setReadOnly(True)
        self.output_curso.setObjectName("output_curso")

        self.output_entidades = QtGui.QLineEdit(self)
        self.output_entidades.setGeometry(QtCore.QRect(194, 218, 427, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_entidades.setFont(font)
        self.output_entidades.setFrame(False)
        self.output_entidades.setReadOnly(True)
        self.output_entidades.setObjectName("output_entidades")

        self.output_colegio = QtGui.QLineEdit(self)
        self.output_colegio.setGeometry(QtCore.QRect(322, 260, 298, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_colegio.setFont(font)
        self.output_colegio.setFrame(False)
        self.output_colegio.setReadOnly(True)
        self.output_colegio.setObjectName("output_colegio")

        self.output_transporte = QtGui.QLineEdit(self)
        self.output_transporte.setGeometry(QtCore.QRect(394, 317, 227, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_transporte.setFont(font)
        self.output_transporte.setFrame(False)
        self.output_transporte.setReadOnly(True)
        self.output_transporte.setObjectName("output_transporte")

        self.output_telefone = QtGui.QLineEdit(self)
        self.output_telefone.setGeometry(QtCore.QRect(81, 259, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_telefone.setFont(font)
        self.output_telefone.setFrame(False)
        self.output_telefone.setReadOnly(True)
        self.output_telefone.setObjectName("output_telefone")

        self.output_bairro = QtGui.QLineEdit(self)
        self.output_bairro.setGeometry(QtCore.QRect(70, 317, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_bairro.setFont(font)
        self.output_bairro.setFrame(False)
        self.output_bairro.setReadOnly(True)
        self.output_bairro.setObjectName("output_bairro")

        self.output_nascimento = QtGui.QLineEdit(self)
        self.output_nascimento.setGeometry(QtCore.QRect(547, 121, 78, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(11)
        self.output_nascimento.setFont(font)
        self.output_nascimento.setFrame(False)
        self.output_nascimento.setReadOnly(True)
        self.output_nascimento.setObjectName("output_nascimento")

        self.output_semestre = QtGui.QLineEdit(self)
        self.output_semestre.setGeometry(QtCore.QRect(519, 177, 104, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_semestre.setFont(font)
        self.output_semestre.setFrame(False)
        self.output_semestre.setReadOnly(True)
        self.output_semestre.setObjectName("output_semestre")

        self.output_snapchat = QtGui.QLineEdit(self)
        self.output_snapchat.setGeometry(QtCore.QRect(504, 375, 118, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_snapchat.setFont(font)
        self.output_snapchat.setFrame(False)
        self.output_snapchat.setReadOnly(True)
        self.output_snapchat.setObjectName("output_snapchat")

        self.output_instagram = QtGui.QLineEdit(self)
        self.output_instagram.setGeometry(QtCore.QRect(323, 376, 123, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_instagram.setFont(font)
        self.output_instagram.setFrame(False)
        self.output_instagram.setReadOnly(True)
        self.output_instagram.setObjectName("output_instagram")

        self.output_facebook = QtGui.QLineEdit(self)
        self.output_facebook.setGeometry(QtCore.QRect(48, 376, 217, 23))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.output_facebook.setFont(font)
        self.output_facebook.setFrame(False)
        self.output_facebook.setReadOnly(True)
        self.output_facebook.setObjectName("output_facebook")

        self.select_user = QtGui.QComboBox(self)
        self.select_user.setGeometry(QtCore.QRect(76, 84, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.select_user.setFont(font)
        self.select_user.setObjectName("select_user")

        self.botao_voltar_perfiluser = QtGui.QCommandLinkButton(self)
        self.botao_voltar_perfiluser.setGeometry(QtCore.QRect(11, 435, 90, 36))
        self.botao_voltar_perfiluser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_voltar_perfiluser.setIcon(icon1)
        self.botao_voltar_perfiluser.setObjectName("botao_voltar_perfiluser")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_voltar_perfiluser.clicked.connect(self.parent().login)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")

        self.nome_dos_usuarios = []
        dicionario = fb.get("/users", None)
        for usuario in dicionario:
            self.nome_dos_usuarios.append(usuario)
            self.select_user.currentIndexChanged.connect(self.slot)
            
        self.select_user.addItems(self.nome_dos_usuarios)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_perfil", "Integrator"))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    def textoComboBox(self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        self.nome_dos_usuarios = []
        self.dicionario = fb.get("/users", None)
        for usuario in self.dicionario:
            self.nome_dos_usuarios.append(usuario)

    def slot (self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        self.current_slot = self.select_user.currentText()
        self.current_name = fb.get("/users", "{0}".format(self.current_slot))
        
        self.output_nome.setText(self.current_name["nome"])
        self.output_nascimento.setText(self.current_name["nascimento"])
        self.output_email.setText(self.current_name["email"])
        self.output_telefone.setText(self.current_name["telefone"])
        self.output_facebook.setText(self.current_name["facebook"])
        self.output_snapchat.setText(self.current_name["snapchat"])
        self.output_instagram.setText(self.current_name["instagram"])
        self.output_transporte.setText(self.current_name["transporte"])
        self.output_curso.setText(self.current_name["curso"])
        self.output_colegio.setText(self.current_name["colegio"])
        self.output_bairro.setText(self.current_name["bairro"])
        self.output_semestre.setText(self.current_name["semestre"])
        
        
        self.frase = 0
        dicientidades = fb.get("/users/{0}".format(self.current_slot), "/entidade")
        listadeentidades = []
        for v in dicientidades.values():
            listadeentidades.append(v)
        if len(listadeentidades) == 1 :
            self.output_entidades.setText("{0}".format(listadeentidades[0]))
        elif len(listadeentidades) == 2 :
            self.output_entidades.setText("{0} e {1}".format(listadeentidades[0], listadeentidades[1]))
        elif len(listadeentidades) == 3:
            self.output_entidades.setText("{0}, {1} e {2}".format(listadeentidades[0], listadeentidades[1], listadeentidades[2]))
        else:
            self.output_entidades.setText("Nenhuma")



    def TextoEntidades(self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        self.frase = 0
        dicientidades = fb.get("/users/{0}".format(self.current_slot), "/entidade")
        listadeentidades = []
        for v in dicientidades.values():
            listadeentidades.append(v)
        if len(listadeentidades) == 1 :
            self.frase = "{0}".format(listadeentidades[0])
        elif len(listadeentidades) == 2 :
            self.frase = "{0} e {1}".format(listadeentidades[0], listadeentidades[1])
        elif len(listadeentidades) == 3:
            self.frase = "{0}, {1} e {2}".format(listadeentidades[0], listadeentidades[1], listadeentidades[2])
        else:
            self.frase = "Nenhuma"
        return self.frase

class Widget_sobre(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_sobre, self).__init__(parent)
        self.setupUi()       

    def setupUi(self):
        self.setObjectName("Widget_sobre")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_link_stackoverflow.setIcon(icon1)
        self.botao_link_stackoverflow.setObjectName("botao_link_stackoverflow")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        
        import webbrowser
        self.botao_link_stackoverflow.clicked.connect(lambda: webbrowser.open('http://stackoverflow.com/questions/22697901/how-do-i-switch-layouts-in-a-window-using-pyqt-without-closing-opening-window'))
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.botao_voltar_sobre = QtGui.QCommandLinkButton(self)
        self.botao_voltar_sobre.setGeometry(QtCore.QRect(7, 439, 91, 34))
        self.botao_voltar_sobre.setText("")
        self.botao_voltar_sobre.setIcon(icon1)
        self.botao_voltar_sobre.setObjectName("botao_voltar_sobre")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_voltar_sobre.clicked.connect(self.parent().login)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Widget_sobre", "Integrator"))


class Widget_calendario(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_calendario, self).__init__(parent)
        self.setupUi()
        self.fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")

    def setupUi(self):        
        self.setObjectName("Widget_calendario")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_calendario = QtGui.QLabel(self)
        self.bg_calendario.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg_calendario.setStyleSheet("background-image: url(:/tela_calendario/Imagens/img_bg/tela_calendario.png);")
        self.bg_calendario.setText("")
        self.bg_calendario.setObjectName("bg_calendario")

        self.but_Seg = QtGui.QCommandLinkButton(self)
        self.but_Seg.setGeometry(QtCore.QRect(53, 24, 86, 54))
        self.but_Seg.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Projeto Final Integrator/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_Seg.setIcon(icon1)
        self.but_Seg.setObjectName("but_Seg")
        self.but_Seg_2 = QtGui.QCommandLinkButton(self)
        self.but_Seg_2.setGeometry(QtCore.QRect(51, 84, 88, 51))
        self.but_Seg_2.setText("")
        self.but_Seg_2.setIcon(icon1)
        self.but_Seg_2.setObjectName("but_Seg_2")
        self.but_Seg_4 = QtGui.QCommandLinkButton(self)
        self.but_Seg_4.setGeometry(QtCore.QRect(52, 201, 86, 51))
        self.but_Seg_4.setText("")
        self.but_Seg_4.setIcon(icon1)
        self.but_Seg_4.setObjectName("but_Seg_4")
        self.but_ter_4 = QtGui.QCommandLinkButton(self)
        self.but_ter_4.setGeometry(QtCore.QRect(142, 200, 87, 112))
        self.but_ter_4.setText("")
        self.but_ter_4.setIcon(icon1)
        self.but_ter_4.setObjectName("but_ter_4")
        self.but_ter = QtGui.QCommandLinkButton(self)
        self.but_ter.setGeometry(QtCore.QRect(142, 23, 87, 54))
        self.but_ter.setText("")
        self.but_ter.setIcon(icon1)
        self.but_ter.setObjectName("but_ter")
        self.but_ter_2 = QtGui.QCommandLinkButton(self)
        self.but_ter_2.setGeometry(QtCore.QRect(142, 82, 87, 52))
        self.but_ter_2.setText("")
        self.but_ter_2.setIcon(icon1)
        self.but_ter_2.setObjectName("but_ter_2")
        self.but_Qua = QtGui.QCommandLinkButton(self)
        self.but_Qua.setGeometry(QtCore.QRect(232, 23, 87, 54))
        self.but_Qua.setText("")
        self.but_Qua.setIcon(icon1)
        self.but_Qua.setObjectName("but_Qua")
        self.but_Qua_2 = QtGui.QCommandLinkButton(self)
        self.but_Qua_2.setGeometry(QtCore.QRect(232, 82, 87, 54))
        self.but_Qua_2.setText("")
        self.but_Qua_2.setIcon(icon1)
        self.but_Qua_2.setObjectName("but_Qua_2")
        self.but_Qua_4 = QtGui.QCommandLinkButton(self)
        self.but_Qua_4.setGeometry(QtCore.QRect(232, 201, 86, 110))
        self.but_Qua_4.setText("")
        self.but_Qua_4.setIcon(icon1)
        self.but_Qua_4.setObjectName("but_Qua_4")
        self.but_Qui = QtGui.QCommandLinkButton(self)
        self.but_Qui.setGeometry(QtCore.QRect(321, 24, 84, 52))
        self.but_Qui.setText("")
        self.but_Qui.setIcon(icon1)
        self.but_Qui.setObjectName("but_Qui")
        self.but_Qui_2 = QtGui.QCommandLinkButton(self)
        self.but_Qui_2.setGeometry(QtCore.QRect(321, 82, 84, 52))
        self.but_Qui_2.setText("")
        self.but_Qui_2.setIcon(icon1)
        self.but_Qui_2.setObjectName("but_Qui_2")
        self.but_Qui_5 = QtGui.QCommandLinkButton(self)
        self.but_Qui_5.setGeometry(QtCore.QRect(322, 259, 84, 52))
        self.but_Qui_5.setText("")
        self.but_Qui_5.setIcon(icon1)
        self.but_Qui_5.setObjectName("but_Qui_5")
        self.but_sex = QtGui.QCommandLinkButton(self)
        self.but_sex.setGeometry(QtCore.QRect(412, 24, 84, 55))
        self.but_sex.setText("")
        self.but_sex.setIcon(icon1)
        self.but_sex.setObjectName("but_sex")
        self.but_sex_2 = QtGui.QCommandLinkButton(self)
        self.but_sex_2.setGeometry(QtCore.QRect(409, 82, 87, 53))
        self.but_sex_2.setText("")
        self.but_sex_2.setIcon(icon1)
        self.but_sex_2.setObjectName("but_sex_2")

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        
        self.but_Seg.clicked.connect(self.GDESegundaClicked)
        self.but_Seg_2.clicked.connect(self.MODSIM1Clicked)
        self.but_Seg_4.clicked.connect(self.MODSIM1Clicked)

        self.but_ter.clicked.connect(self.INSTRUMEDClicked) #atendimento instrumed 401
        self.but_ter_2.clicked.connect(self.DESOFTatClicked) #atendimento desoft albertor bandeira queiroz 2
        self.but_ter_4.clicked.connect(self.INSTRUMEDClicked) #aula instrumed 401

        self.but_Qua.clicked.connect(self.DESOFTClicked) #aula desoft 403
        self.but_Qua_2.clicked.connect(self.GDEatClicked) #Atendimento GDE 403
        self.but_Qua_4.clicked.connect(self.NATDESClicked) #aula natureza 403
        # self.but_Qua_6.clicked.connect(self.NATDESatClicked) #atendimento natureza 403

        self.but_Qui.clicked.connect(self.GDEQuintaClicked) #aula gde 307
        self.but_Qui_2.clicked.connect(self.GDETutClicked) #tutoria gde 408
        self.but_Qui_5.clicked.connect(self.MODSIM1Clicked)

        self.but_sex.clicked.connect(self.DESOFTClicked)
        self.but_sex_2.clicked.connect(self.MODSIM1Clicked)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#



        self.seg_3 = QtGui.QLabel(self)
        self.seg_3.setGeometry(QtCore.QRect(51, 143, 88, 50))
        self.seg_3.setAlignment(QtCore.Qt.AlignCenter)
        self.seg_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.seg_3.setObjectName("seg_3")
        self.seg_5 = QtGui.QLabel(self)
        self.seg_5.setGeometry(QtCore.QRect(51, 259, 86, 51))
        self.seg_5.setAlignment(QtCore.Qt.AlignCenter)
        self.seg_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.seg_5.setObjectName("seg_5")
        self.seg_6 = QtGui.QLabel(self)
        self.seg_6.setGeometry(QtCore.QRect(52, 319, 86, 51))
        self.seg_6.setAlignment(QtCore.Qt.AlignCenter)
        self.seg_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.seg_6.setObjectName("seg_6")
        self.seg_7 = QtGui.QLabel(self)
        self.seg_7.setGeometry(QtCore.QRect(52, 377, 86, 51))
        self.seg_7.setAlignment(QtCore.Qt.AlignCenter)
        self.seg_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.seg_7.setObjectName("seg_7")
        self.ter_3 = QtGui.QLabel(self)
        self.ter_3.setGeometry(QtCore.QRect(142, 142, 88, 50))
        self.ter_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ter_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ter_3.setObjectName("ter_3")
        self.ter_6 = QtGui.QLabel(self)
        self.ter_6.setGeometry(QtCore.QRect(143, 318, 86, 51))
        self.ter_6.setAlignment(QtCore.Qt.AlignCenter)
        self.ter_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ter_6.setObjectName("ter_6")
        self.ter_7 = QtGui.QLabel(self)
        self.ter_7.setGeometry(QtCore.QRect(143, 376, 86, 51))
        self.ter_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ter_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ter_7.setObjectName("ter_7")
        self.Qua_3 = QtGui.QLabel(self)
        self.Qua_3.setGeometry(QtCore.QRect(233, 144, 84, 50))
        self.Qua_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Qua_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Qua_3.setObjectName("Qua_3")
        self.Qua_7 = QtGui.QLabel(self)
        self.Qua_7.setGeometry(QtCore.QRect(234, 378, 84, 51))
        self.Qua_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Qua_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Qua_7.setObjectName("Qua_7")
        self.Qua_6 = QtGui.QLabel(self)
        self.Qua_6.setGeometry(QtCore.QRect(234, 320, 84, 51))
        self.Qua_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Qua_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Qua_6.setObjectName("Qua_6")
        self.Qui_3 = QtGui.QLabel(self)
        self.Qui_3.setGeometry(QtCore.QRect(322, 143, 84, 50))
        self.Qui_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Qui_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Qui_3.setObjectName("Qui_3")
        self.Qui_6 = QtGui.QLabel(self)
        self.Qui_6.setGeometry(QtCore.QRect(323, 319, 84, 51))
        self.Qui_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Qui_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Qui_6.setObjectName("Qui_6")
        self.Qui_7 = QtGui.QLabel(self)
        self.Qui_7.setGeometry(QtCore.QRect(323, 377, 84, 51))
        self.Qui_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Qui_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Qui_7.setObjectName("Qui_7")
        self.Qui_4 = QtGui.QLabel(self)
        self.Qui_4.setGeometry(QtCore.QRect(322, 201, 84, 51))
        self.Qui_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Qui_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Qui_4.setObjectName("Qui_4")
        self.sex_6 = QtGui.QLabel(self)
        self.sex_6.setGeometry(QtCore.QRect(412, 320, 84, 51))
        self.sex_6.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sex_6.setObjectName("sex_6")
        self.sex_3 = QtGui.QLabel(self)
        self.sex_3.setGeometry(QtCore.QRect(411, 144, 84, 50))
        self.sex_3.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sex_3.setObjectName("sex_3")
        self.sex_4 = QtGui.QLabel(self)
        self.sex_4.setGeometry(QtCore.QRect(411, 202, 84, 51))
        self.sex_4.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sex_4.setObjectName("sex_4")
        self.sab_1 = QtGui.QLabel(self)
        self.sab_1.setGeometry(QtCore.QRect(502, 26, 62, 51))
        self.sab_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sab_1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sab_1.setObjectName("sab_1")
        self.sex_5 = QtGui.QLabel(self)
        self.sex_5.setGeometry(QtCore.QRect(411, 258, 84, 51))
        self.sex_5.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sex_5.setObjectName("sex_5")
        self.botao_salvar_calendario = QtGui.QCommandLinkButton(self)
        self.botao_salvar_calendario.setGeometry(QtCore.QRect(524, 437, 106, 37))
        self.botao_salvar_calendario.setText("")
        self.botao_salvar_calendario.setIcon(icon1)
        self.botao_salvar_calendario.setObjectName("botao_salvar_calendario")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        #self.botao_salvar_calendario.clicked.connect(self.salvar_calendario)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        

        self.botao_voltar_calendario = QtGui.QCommandLinkButton(self)
        self.botao_voltar_calendario.setGeometry(QtCore.QRect(6, 436, 92, 39))
        self.botao_voltar_calendario.setText("")
        self.botao_voltar_calendario.setIcon(icon1)
        self.botao_voltar_calendario.setObjectName("botao_voltar_calendario")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        self.botao_voltar_calendario.clicked.connect(self.parent().login)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        self.sab_2 = QtGui.QLabel(self)
        self.sab_2.setGeometry(QtCore.QRect(501, 81, 62, 51))
        self.sab_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sab_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sab_2.setObjectName("sab_2")
        self.sab_3 = QtGui.QLabel(self)
        self.sab_3.setGeometry(QtCore.QRect(501, 142, 62, 51))
        self.sab_3.setAlignment(QtCore.Qt.AlignCenter)
        self.sab_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sab_3.setObjectName("sab_3")
        self.sab_4 = QtGui.QLabel(self)
        self.sab_4.setGeometry(QtCore.QRect(501, 201, 62, 51))
        self.sab_4.setAlignment(QtCore.Qt.AlignCenter)
        self.sab_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sab_4.setObjectName("sab_4")
        self.sab_5 = QtGui.QLabel(self)
        self.sab_5.setGeometry(QtCore.QRect(501, 259, 62, 51))
        self.sab_5.setAlignment(QtCore.Qt.AlignCenter)
        self.sab_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sab_5.setObjectName("sab_5")
        self.sab_6 = QtGui.QLabel(self)
        self.sab_6.setGeometry(QtCore.QRect(501, 319, 62, 51))
        self.sab_6.setAlignment(QtCore.Qt.AlignCenter)
        self.sab_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sab_6.setObjectName("sab_6")
        self.sab_7 = QtGui.QLabel(self)
        self.sab_7.setGeometry(QtCore.QRect(502, 378, 62, 51))
        self.sab_7.setAlignment(QtCore.Qt.AlignCenter)
        self.sab_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sab_7.setObjectName("sab_7")
        self.dom_1 = QtGui.QLabel(self)
        self.dom_1.setGeometry(QtCore.QRect(569, 25, 62, 51))
        self.dom_1.setAlignment(QtCore.Qt.AlignCenter)
        self.dom_1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dom_1.setObjectName("dom_1")
        self.dom_2 = QtGui.QLabel(self)
        self.dom_2.setGeometry(QtCore.QRect(570, 83, 62, 51))
        self.dom_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dom_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dom_2.setObjectName("dom_2")
        self.dom_3 = QtGui.QLabel(self)
        self.dom_3.setGeometry(QtCore.QRect(568, 142, 62, 51))
        self.dom_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dom_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dom_3.setObjectName("dom_3")
        self.dom_4 = QtGui.QLabel(self)
        self.dom_4.setGeometry(QtCore.QRect(569, 201, 62, 51))
        self.dom_4.setAlignment(QtCore.Qt.AlignCenter)
        self.dom_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dom_4.setObjectName("dom_4")
        self.dom_5 = QtGui.QLabel(self)
        self.dom_5.setGeometry(QtCore.QRect(569, 262, 62, 51))
        self.dom_5.setAlignment(QtCore.Qt.AlignCenter)
        self.dom_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dom_5.setObjectName("dom_5")
        self.dom_6 = QtGui.QLabel(self)
        self.dom_6.setGeometry(QtCore.QRect(569, 317, 62, 51))
        self.dom_6.setAlignment(QtCore.Qt.AlignCenter)
        self.dom_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dom_6.setObjectName("dom_6")
        self.dom_7 = QtGui.QLabel(self)
        self.dom_7.setGeometry(QtCore.QRect(570, 378, 62, 51))
        self.dom_7.setAlignment(QtCore.Qt.AlignCenter)
        self.dom_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.dom_7.setObjectName("dom_7")
        self.sex_7 = QtGui.QLabel(self)
        self.sex_7.setGeometry(QtCore.QRect(411, 380, 84, 51))
        self.sex_7.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sex_7.setObjectName("sex_7")
        self.bg_calendario.raise_()
        self.but_Seg.raise_()
        self.but_Seg_2.raise_()
        self.but_Seg_4.raise_()
        self.but_ter_4.raise_()
        self.but_ter.raise_()
        self.but_ter_2.raise_()
        self.but_Qua.raise_()
        self.but_Qua_2.raise_()
        self.but_Qua_4.raise_()
        self.but_Qui.raise_()
        self.but_Qui_2.raise_()
        self.but_Qui_5.raise_()
        self.but_sex.raise_()
        self.but_sex_2.raise_()
        self.seg_3.raise_()
        self.seg_6.raise_()
        self.seg_7.raise_()
        self.seg_5.raise_()
        self.ter_3.raise_()
        self.ter_6.raise_()
        self.ter_7.raise_()
        self.Qua_3.raise_()
        self.Qua_7.raise_()
        self.Qua_6.raise_()
        self.Qui_3.raise_()
        self.Qui_6.raise_()
        self.Qui_7.raise_()
        self.Qui_4.raise_()
        self.sex_6.raise_()
        self.sex_3.raise_()
        self.sex_4.raise_()
        self.sab_1.raise_()
        self.sex_5.raise_()
        self.botao_salvar_calendario.raise_()
        self.botao_voltar_calendario.raise_()
        self.sab_2.raise_()
        self.sab_3.raise_()
        self.sab_4.raise_()
        self.sab_5.raise_()
        self.sab_6.raise_()
        self.sab_7.raise_()
        self.dom_1.raise_()
        self.dom_2.raise_()
        self.dom_3.raise_()
        self.dom_4.raise_()
        self.dom_5.raise_()
        self.dom_6.raise_()
        self.dom_7.raise_()
        self.sex_7.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Widget_calendario", "Integrator"))
        self.seg_3.setText(_translate("Widget_calendario", "-"))
        self.seg_5.setText(_translate("Widget_calendario", "-"))
        self.seg_6.setText(_translate("Widget_calendario", "-"))
        self.seg_7.setText(_translate("Widget_calendario", "-"))
        self.ter_3.setText(_translate("Widget_calendario", "-"))
        self.ter_6.setText(_translate("Widget_calendario", "-"))
        self.ter_7.setText(_translate("Widget_calendario", "-"))
        self.Qua_3.setText(_translate("Widget_calendario", "-"))
        self.Qua_7.setText(_translate("Widget_calendario", "-"))
        self.Qua_6.setText(_translate("Widget_calendario", "-"))
        self.Qui_3.setText(_translate("Widget_calendario", "-"))
        self.Qui_6.setText(_translate("Widget_calendario", "-"))
        self.Qui_7.setText(_translate("Widget_calendario", "-"))
        self.Qui_4.setText(_translate("Widget_calendario", "-"))
        self.sex_6.setText(_translate("Widget_calendario", "-"))
        self.sex_3.setText(_translate("Widget_calendario", "-"))
        self.sex_4.setText(_translate("Widget_calendario", "-"))
        self.sab_1.setText(_translate("Widget_calendario", "-"))
        self.sex_5.setText(_translate("Widget_calendario", "-"))
        self.sab_2.setText(_translate("Widget_calendario", "-"))
        self.sab_3.setText(_translate("Widget_calendario", "-"))
        self.sab_4.setText(_translate("Widget_calendario", "-"))
        self.sab_5.setText(_translate("Widget_calendario", "-"))
        self.sab_6.setText(_translate("Widget_calendario", "-"))
        self.sab_7.setText(_translate("Widget_calendario", "-"))
        self.dom_1.setText(_translate("Widget_calendario", "-"))
        self.dom_2.setText(_translate("Widget_calendario", "-"))
        self.dom_3.setText(_translate("Widget_calendario", "-"))
        self.dom_4.setText(_translate("Widget_calendario", "-"))
        self.dom_5.setText(_translate("Widget_calendario", "-"))
        self.dom_6.setText(_translate("Widget_calendario", "-"))
        self.dom_7.setText(_translate("Widget_calendario", "-"))
        self.sex_7.setText(_translate("Widget_calendario", "-"))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #     self.nome_usuario = self.parent().user

    # def salvar_edicoes(self):
    # 	self.l_seg3 = self.seg_3.text()
    #     self.l_seg5 = self.seg_5.text()
    #     self.l_seg6 = self.seg_6.text()
    #     self.l_seg6 = self.seg_7.text()
    #     self.l_ter3 = self.ter_3.text()
    #     self.l_ter6 = self.ter_6.text()
    #     self.l_ter7 = self.ter_7.text()
    #     self.l_qua3 = self.Qua_3.text()
    #     self.l_qua7 = self.Qua_7.text()
    #     self.l_qua6 = self.Qua_6.text()
    #     self.l_qui3 = self.Qui_3.text()
    #     self.l_qui6 = self.Qui_6.text()
    #     self.l_qui7 = self.Qui_7.text()
    #     self.l_qui4 = self.Qui_4.text()
    #     self.l_sex6 = self.sex_6.text()
    #     self.l_sex3 = self.sex_3.text()
    #     self.l_sex4 = self.sex_4.text()
    #     self.l_sab1 = self.sab_1.text()
    #     self.l_sab5 = self.sex_5.text()
    #     self.l_sab2 = self.sab_2.text()
    #     self.l_sab3 = self.sab_3.text()
    #     self.l_sab4 = self.sab_4.text()
    #     self.l_sab5 = self.sab_5.text()
    #     self.l_sab6 = self.sab_6.text()
    #     self.l_sab7 = self.sab_7.text()
    #     self.l_dom1 = self.dom_1.text()
    #     self.l_dom2 = self.dom_2.text()
    #     self.l_dom3 = self.dom_3.text()
    #     self.l_dom4 = self.dom_4.text()
    #     self.l_dom5 = self.dom_5.text()
    #     self.l_dom6 = self.dom_6.text()
    #     self.l_dom7 = self.dom_7.text()
    #     self.l_sex7 = self.sex_7.text()
    # 	pega o que ta escrito nas labels (gettext) e salva no fire botao_servicos

    # def pegar_edicoes(self): modificar a funcao abaixo
        # fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        # self.current_slot = self.select_user.currentText()
        # self.current_name = fb.get("/users", "{0}".format(self.current_slot))
        
        # self.output_nome.setText(self.current_name["nome"])
        # self.output_nascimento.setText(self.current_name["nascimento"])
        # self.output_email.setText(self.current_name["email"])
        # self.output_telefone.setText(self.current_name["telefone"])
        # self.output_facebook.setText(self.current_name["facebook"])
        # self.output_snapchat.setText(self.current_name["snapchat"])
        # self.output_instagram.setText(self.current_name["instagram"])
        # self.output_transporte.setText(self.current_name["transporte"])
        # self.output_curso.setText(self.current_name["curso"])
        # self.output_colegio.setText(self.current_name["colegio"])
        # self.output_bairro.setText(self.current_name["bairro"])
        # self.output_semestre.setText(self.current_name["semestre"])
        

    def BotaoSaveClicked (self):
        _translate = QtCore.QCoreApplication.translate
        nome_do_evento = self.novo_evento.lineEdit_3.text()
        data_do_evento = self.novo_evento.dateEdit.text()
        self.fb.put("/users/{0}/eventos".format(self.parent().user), 
                     name = nome_do_evento, 
                     data = data_do_evento)
          
        item = QtGui.QTableWidgetItem()
        item.setText(_translate("Form", data_do_evento))
        self.novo_evento.tableWidget.setVerticalHeaderItem(len(self.listdatas), item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(_translate("Form", nome_do_evento))
        self.novo_evento.tableWidget.setItem(len(self.listevents), 0, item)

    def GDESegundaClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Grandes Desafios da Engenharia")
        self.novo_evento.input_abreviacao.setText("GDE")
        self.novo_evento.input_sobremateria.setText(
            'O curso de Grandes Desafios da Engenharia problematiza a “neutralidade” ' +
            'da produção tecnológica pois entende o desenvolvimento da técnica ' +
            'e da tecnologia como dimensões da humanidade. Dessa forma, a ciência, ' +
            'a tecnologia e a inovação devem ser entendidas como “fatos sociais”. ' +
            'A partir desses parâmetros o curso permitirá que o engenheiro em ' +
            'formação tenha contato com os métodos e os objetos de estudos de outra matriz científica que não a das ciências da natureza (ciências duras). Dessa forma, o treinamento do engenheiro lhe capacitará a dialogar com profissionais de outras formações ao longo de sua vida profissional. Além disso, o curso explorará as múltiplas relações que se colocam no trinômio ciência-tecnologia-sociedade. Ou seja, os caminhos pelos quais a ciência e a tecnologia pautam os desdobramentos dos fatos sociais (tecnolfilia) e, alternativamente, a forma como os fatos sociais moldam as escolhas tecnológicas (tecnofobia). Neste diapasão, a bibliografia sugerida trabalhará textos afeitos à filosofia, à economia, à sociologia e à própria engenharia (além, é claro, de textos que forneçam subsídios aos estudos dos temas sugeridos no primeiro módulo das tutorias, sobremaneira aqueles da esfera da linguística).')
        self.novo_evento.input_professor.setText("Fernando Ribeiro Leite Neto")
        self.novo_evento.input_sobreprof.setText("Possui graduação em Ciências Econômicas pela Pontifícia Universidade Católica de São Paulo (1999), mestrado em Economia Política (2002) e doutorado em Ciências Sociais (2010) pela mesma instituição. Atualmente é professor assistente mestre da Pontifícia Universidade Católica de São Paulo, professor assistente do Insper Instituto de Ensino e Pesquisa e sócio-consultor da Urbana Consultoria em Desenvolvimento Econômico e Social. Tem experiência na área de Economia, com ênfase em História do Pensamento Econômico, Economia Regional e Urbana e América Latina atuando principalmente nos seguintes temas: Período pré-clássico, atividade econômica regional e setor externo.")
        self.novo_evento.lineEdit.setText("Marcos Lopes" )
        self.novo_evento.lineEdit_2.setText("Segundo Andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        
        self.novo_evento.show()

    def MODSIM1Clicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Modelagem e Simulação do Mundo Físico")
        self.novo_evento.input_abreviacao.setText("MODSIM")
        self.novo_evento.input_sobremateria.setText("Por três vezes o ciclo de Modelagem e Simulação será percorrido de forma completa neste curso. Cada ciclo corresponderá a um projeto realizado pelos alunos. Os projetos serão realizados com grau crescente de autonomia por parte dos alunos. ")
        self.novo_evento.input_professor.setText("Fabio Sismotto El Hage")
        self.novo_evento.input_sobreprof.setText("Professor de Engenharia do Insper, Doutor em Engenharia pela Escola Politécnica da USP e pós-doutor em Política Energética pela Suffolk University, em Boston, EUA. Além de professor, atua também como consultor da Associação Brasileira de Distribuidores de Energia Elétrica (ABRADEE) nas áreas regulatória e de modelagem e simulação.")
        self.novo_evento.lineEdit.setText("403" )
        self.novo_evento.lineEdit_2.setText("4º andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        self.novo_evento.show()

    def INSTRUMEDClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Instrumentação e Medição")
        self.novo_evento.input_abreviacao.setText("INSTRUMED")
        self.novo_evento.input_sobremateria.setText("O Objetivo da disciplina é capacitar o aluno para aquisição, análise e tratamento de dados através do uso de sensores, transdutores e circuitos eletro-eletrônicos dedicados. As aulas serão compostas de partes teóricas e práticas de forma sequencial, permitindo a imediata aplicação dos conhecimentos teóricos apresentados. Serão realizados diversos projetos em grupo cujos objetivos são capacitar os alunos a: Identificar componentes elétricos e sua função em circuitos; Interpretar diagramas de circuitos básicos e montá-los em protoboard; Projetar circuitos simples e confeccionar placas de circuito impresso dedicadas; Utilizar instrumentação básica em eletricidade; Fazer aquisição de dados de fenômenos físicos com o emprego de sensores e circuitos eletro- eletrônicos; Analisar e apresentar dados utilizando ferramentas estatísticas básicas; Aplicar os conceitos de incerteza, exatidão, precisão, resolução e sensibilidade. ")
        self.novo_evento.input_professor.setText("Fábio Ferraz Júnior")
        self.novo_evento.input_sobreprof.setText("Possui graduação em Engenharia Mecânica (Mecatrônica) pela Universidade de São Paulo / EESC - São Carlos (1999), mestrado em Engenharia Mecânica (Automação de Processos de Fabricação) pela Universidade de São Paulo / EESC - São Carlos (2002) e doutorado em Engenharia Mecânica (Automação de Processos de Fabricação) pela Universidade de São Paulo / EESC - São Carlos (2007). Atualmente é diretor da SENSOFT Indústria e Automação Ltda e professor do Centro Universitário de Araraquara (UNIARA). Tem experiência na área de Engenharia Mecânica, com ênfase em Automação de Processos de Fabricação, atuando principalmente nos seguintes temas: instrumentação, monitoramento, supervisão (SCADA), CNC de arquitetura aberta, controle de processos de fabricação.")
        self.novo_evento.lineEdit.setText("401" )
        self.novo_evento.lineEdit_2.setText("4º andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)        
        self.novo_evento.show()

    def DESOFTatClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Design de Software")
        self.novo_evento.input_abreviacao.setText("DESOFT")
        self.novo_evento.input_sobremateria.setText("O objetivo da disciplina é capacitar os alunos a codificar e depurar programas de computador, individualmente e em grupos, identificando necessidades funcionais e desenvolvendo heurísticas para a resolução de requisitos. O aluno trabalhará em projetos de desenvolvimento de software simples e em um projeto principal proposto pelo grupo, e que também deve ser submetido a validação, revisão e documentação do projeto. Para isso, técnicas elementares de gestão de projeto de software serão praticadas durante o curso. ")
        self.novo_evento.input_professor.setText("Fábio Ayres")
        self.novo_evento.input_sobreprof.setText("Fábio Ayres é professor adjunto do Insper, envolvido no desenvolvimento dos cursos de engenharia. Possui graduação e mestrado em Engenharia Elétrica pela Escola Politécnica da USP e doutorado em Engenharia Elétrica pela University of Calgary, Canadá. Foi pós-doutorando em Engenharia Biomédica pela University of Calgary, pesquisador associado do National Research Council of Canada, engenheiro de software na Opal-RT Technologies, Canadá, e no Google. Interessa-se por visão computacional, aprendizado de máquina, processamento de imagens, recuperação de informação, computação de alto desempenho.")
        self.novo_evento.lineEdit.setText("Antônio Bandeira")
        self.novo_evento.lineEdit_2.setText("2º andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)        
        self.novo_evento.show()

    def DESOFTClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Design de Software")
        self.novo_evento.input_abreviacao.setText("DESOFT")
        self.novo_evento.input_sobremateria.setText("O objetivo da disciplina é capacitar os alunos a codificar e depurar programas de computador, individualmente e em grupos, identificando necessidades funcionais e desenvolvendo heurísticas para a resolução de requisitos. O aluno trabalhará em projetos de desenvolvimento de software simples e em um projeto principal proposto pelo grupo, e que também deve ser submetido a validação, revisão e documentação do projeto. Para isso, técnicas elementares de gestão de projeto de software serão praticadas durante o curso. ")
        self.novo_evento.input_professor.setText("Fábio Ayres")
        self.novo_evento.input_sobreprof.setText("Fábio Ayres é professor adjunto do Insper, envolvido no desenvolvimento dos cursos de engenharia. Possui graduação e mestrado em Engenharia Elétrica pela Escola Politécnica da USP e doutorado em Engenharia Elétrica pela University of Calgary, Canadá. Foi pós-doutorando em Engenharia Biomédica pela University of Calgary, pesquisador associado do National Research Council of Canada, engenheiro de software na Opal-RT Technologies, Canadá, e no Google. Interessa-se por visão computacional, aprendizado de máquina, processamento de imagens, recuperação de informação, computação de alto desempenho.")
        self.novo_evento.lineEdit.setText("403")
        self.novo_evento.lineEdit_2.setText("4º andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        self.novo_evento.show()

    def GDEatClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Grandes Desafios da Engenharia")
        self.novo_evento.input_abreviacao.setText("GDE")
        self.novo_evento.input_sobremateria.setText("O curso de Grandes Desafios da Engenharia problematiza a “neutralidade” da produção tecnológica pois entende o desenvolvimento da técnica e da tecnologia como dimensões da humanidade. Dessa forma, a ciência, a tecnologia e a inovação devem ser entendidas como “fatos sociais”. A partir desses parâmetros o curso permitirá que o engenheiro em formação tenha contato com os métodos e os objetos de estudos de outra matriz científica que não a das ciências da natureza (ciências duras). Dessa forma, o treinamento do engenheiro lhe capacitará a dialogar com profissionais de outras formações ao longo de sua vida profissional. Além disso, o curso explorará as múltiplas relações que se colocam no trinômio ciência-tecnologia-sociedade. Ou seja, os caminhos pelos quais a ciência e a tecnologia pautam os desdobramentos dos fatos sociais (tecnolfilia) e, alternativamente, a forma como os fatos sociais moldam as escolhas tecnológicas (tecnofobia). Neste diapasão, a bibliografia sugerida trabalhará textos afeitos à filosofia, à economia, à sociologia e à própria engenharia (além, é claro, de textos que forneçam subsídios aos estudos dos temas sugeridos no primeiro módulo das tutorias, sobremaneira aqueles da esfera da linguística).")
        self.novo_evento.input_professor.setText("Fernando Ribeiro Leite Neto")
        self.novo_evento.input_sobreprof.setText("Possui graduação em Ciências Econômicas pela Pontifícia Universidade Católica de São Paulo (1999), mestrado em Economia Política (2002) e doutorado em Ciências Sociais (2010) pela mesma instituição. Atualmente é professor assistente mestre da Pontifícia Universidade Católica de São Paulo, professor assistente do Insper Instituto de Ensino e Pesquisa e sócio-consultor da Urbana Consultoria em Desenvolvimento Econômico e Social. Tem experiência na área de Economia, com ênfase em História do Pensamento Econômico, Economia Regional e Urbana e América Latina atuando principalmente nos seguintes temas: Período pré-clássico, atividade econômica regional e setor externo.")
        self.novo_evento.lineEdit.setText("403" )
        self.novo_evento.lineEdit_2.setText("4º andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        self.novo_evento.show()

    def NATDESatClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Natureza do Design")
        self.novo_evento.input_abreviacao.setText("NATDES")
        self.novo_evento.input_sobremateria.setText("Vivenciar a experiência do projeto e suas fases (concepção, desenvolvimento, fabricação e validação),sempre tendo o usuário como foco central do problema e construindo um raciocínio crítico diante das especificidades de cada tema. Compreender o projeto enquanto processo de aprendizado pelo fazer (hands-on). Comunicar de forma gráfica não verbal, textual e oral.")    
        self.novo_evento.input_professor.setText("Heloisa Neves, Roberto Fialho")
        self.novo_evento.input_sobreprof.setText("Doutora em Design e Arquitetura – USP, Doutor em Arquitetura e Urbanismo – USP")
        self.novo_evento.lineEdit.setText("Fablab")
        self.novo_evento.lineEdit_2.setText("4º Andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        self.novo_evento.show()
        
    def NATDESClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Natureza do Design")
        self.novo_evento.input_abreviacao.setText("NATDES")
        self.novo_evento.input_sobremateria.setText("Vivenciar a experiência do projeto e suas fases (concepção, desenvolvimento, fabricação e validação),sempre tendo o usuário como foco central do problema e construindo um raciocínio crítico diante das especificidades de cada tema. Compreender o projeto enquanto processo de aprendizado pelo fazer (hands-on). Comunicar de forma gráfica não verbal, textual e oral.")    
        self.novo_evento.input_professor.setText("Heloisa Neves, Roberto Fialho")
        self.novo_evento.input_sobreprof.setText("Doutora em Design e Arquitetura – USP, Doutor em Arquitetura e Urbanismo – USP")
        self.novo_evento.lineEdit.setText("403")
        self.novo_evento.lineEdit_2.setText("4º Andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        self.novo_evento.show()

    def GDETutClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Grandes Desafios da Engenharia - Tutoria")
        self.novo_evento.input_abreviacao.setText("GDE")
        self.novo_evento.input_sobremateria.setText("O curso de Grandes Desafios da Engenharia problematiza a “neutralidade” da produção tecnológica pois entende o desenvolvimento da técnica e da tecnologia como dimensões da humanidade. Dessa forma, a ciência, a tecnologia e a inovação devem ser entendidas como “fatos sociais”. A partir desses parâmetros o curso permitirá que o engenheiro em formação tenha contato com os métodos e os objetos de estudos de outra matriz científica que não a das ciências da natureza (ciências duras). Dessa forma, o treinamento do engenheiro lhe capacitará a dialogar com profissionais de outras formações ao longo de sua vida profissional. Além disso, o curso explorará as múltiplas relações que se colocam no trinômio ciência-tecnologia-sociedade. Ou seja, os caminhos pelos quais a ciência e a tecnologia pautam os desdobramentos dos fatos sociais (tecnolfilia) e, alternativamente, a forma como os fatos sociais moldam as escolhas tecnológicas (tecnofobia). Neste diapasão, a bibliografia sugerida trabalhará textos afeitos à filosofia, à economia, à sociologia e à própria engenharia (além, é claro, de textos que forneçam subsídios aos estudos dos temas sugeridos no primeiro módulo das tutorias, sobremaneira aqueles da esfera da linguística).")
        self.novo_evento.input_professor.setText("Sérgio Roberto Cardoso")
        self.novo_evento.input_sobreprof.setText("Possui Mestrado em Filosofia pelo Programa de Pós-Graduação em Estudos Culturais da Universidade de São Paulo (USP) e Especialização em Docência de Sociologia pela mesma universidade. Tem graduação em Ciências Sociais (Licenciatura Plena e Bacharelado em Antropologia) pela Universidade Estadual Paulista (UNESP) e formação em nível técnico na área de Alimentos pelo Centro Paula Souza (Etec). É servidor público estadual, concursado como Professor de Sociologia na Educação Básica pela Secretaria da Educação do Estado de São Paulo, onde já ocupou também função de Técnico Educacional em Sociologia na equipe curricular de Ciências Humanas e cargo de Diretor Técnico do Núcleo de Inclusão Educacional da Coordenadoria de Gestão da Educação Básica. No ensino superior ministra aulas da área de Humanidades em cursos de graduação em Engenharia da Computação, Mecânica e Mecatrônica. Como Sociólogo (Mtb 2174/SP) desenvolve pesquisas, projetos e palestras sobre antropologia da alimentação, cultura afro-brasileira, ensino de Sociologia, inclusão de grupos sociais na educação básica e educação para as relações étnico-raciais.")
        self.novo_evento.lineEdit.setText("408")
        self.novo_evento.lineEdit_2.setText("4º Andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        self.novo_evento.show()

    def GDEQuintaClicked (self):
        self.novo_evento = Widget_abas(self)
        self.novo_evento.input_materia.setText("Grandes Desafios da Engenharia")
        self.novo_evento.input_abreviacao.setText("GDE")
        self.novo_evento.input_sobremateria.setText("O curso de Grandes Desafios da Engenharia problematiza a “neutralidade” da produção tecnológica pois entende o desenvolvimento da técnica e da tecnologia como dimensões da humanidade. Dessa forma, a ciência, a tecnologia e a inovação devem ser entendidas como “fatos sociais”. A partir desses parâmetros o curso permitirá que o engenheiro em formação tenha contato com os métodos e os objetos de estudos de outra matriz científica que não a das ciências da natureza (ciências duras). Dessa forma, o treinamento do engenheiro lhe capacitará a dialogar com profissionais de outras formações ao longo de sua vida profissional. Além disso, o curso explorará as múltiplas relações que se colocam no trinômio ciência-tecnologia-sociedade. Ou seja, os caminhos pelos quais a ciência e a tecnologia pautam os desdobramentos dos fatos sociais (tecnolfilia) e, alternativamente, a forma como os fatos sociais moldam as escolhas tecnológicas (tecnofobia). Neste diapasão, a bibliografia sugerida trabalhará textos afeitos à filosofia, à economia, à sociologia e à própria engenharia (além, é claro, de textos que forneçam subsídios aos estudos dos temas sugeridos no primeiro módulo das tutorias, sobremaneira aqueles da esfera da linguística).")
        self.novo_evento.input_professor.setText("Fernando Ribeiro Leite Neto")
        self.novo_evento.input_sobreprof.setText("Possui graduação em Ciências Econômicas pela Pontifícia Universidade Católica de São Paulo (1999), mestrado em Economia Política (2002) e doutorado em Ciências Sociais (2010) pela mesma instituição. Atualmente é professor assistente mestre da Pontifícia Universidade Católica de São Paulo, professor assistente do Insper Instituto de Ensino e Pesquisa e sócio-consultor da Urbana Consultoria em Desenvolvimento Econômico e Social. Tem experiência na área de Economia, com ênfase em História do Pensamento Econômico, Economia Regional e Urbana e América Latina atuando principalmente nos seguintes temas: Período pré-clássico, atividade econômica regional e setor externo.")
        self.novo_evento.lineEdit.setText("307")
        self.novo_evento.lineEdit_2.setText("3º Andar")
        self.novo_evento.pushButton.clicked.connect(self.BotaoSaveClicked)
        _translate = QtCore.QCoreApplication.translate
        dicieventos = self.fb.get("/users/{0}".format(self.parent().user), "/eventos")
        self.listevents = []
        self.listdatas = []            
        for i, j in dicieventos.items():
            self.listevents.append(i)
            self.listdatas.append(j)
        print(self.listevents)
        
        for r in range (len(self.listdatas)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listdatas[r]))
            self.novo_evento.tableWidget.setVerticalHeaderItem(r, item)
            
        for p in range (len(self.listevents)):
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("Form", self.listevents[p]))
            self.novo_evento.tableWidget.setItem(p, 0, item)
        self.novo_evento.show()
              
class Widget_abas(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_abas, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(280, 342)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Documents/GitHub/projeto_dsoft/datails.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        # self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.aba_aula = QtGui.QWidget()
        self.aba_aula.setObjectName("aba_aula")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.aba_aula)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.materia = QtGui.QHBoxLayout()
        self.materia.setObjectName("materia")
        self.label_materia = QtGui.QLabel(self.aba_aula)
        self.label_materia.setObjectName("label_materia")
        self.materia.addWidget(self.label_materia)
        self.input_materia = QtGui.QLineEdit(self.aba_aula)
        self.input_materia.setText("")
        self.input_materia.setObjectName("input_materia")
        self.materia.addWidget(self.input_materia)
        self.verticalLayout.addLayout(self.materia)
        self.abreviacao = QtGui.QHBoxLayout()
        self.abreviacao.setObjectName("abreviacao")
        self.label_abreviacao = QtGui.QLabel(self.aba_aula)
        self.label_abreviacao.setObjectName("label_abreviacao")
        self.abreviacao.addWidget(self.label_abreviacao)
        self.input_abreviacao = QtGui.QLineEdit(self.aba_aula)
        self.input_abreviacao.setText("")
        self.input_abreviacao.setObjectName("input_abreviacao")
        self.abreviacao.addWidget(self.input_abreviacao)
        self.verticalLayout.addLayout(self.abreviacao)
        self.sobre_materia = QtGui.QVBoxLayout()
        self.sobre_materia.setObjectName("sobre_materia")
        self.label_sobremateria = QtGui.QLabel(self.aba_aula)
        self.label_sobremateria.setObjectName("label_sobremateria")
        self.sobre_materia.addWidget(self.label_sobremateria)
        self.input_sobremateria = QtGui.QTextEdit(self.aba_aula)
        self.input_sobremateria.setReadOnly(True)
        self.input_sobremateria.setObjectName("input_sobremateria")
        self.sobre_materia.addWidget(self.input_sobremateria)
        self.verticalLayout.addLayout(self.sobre_materia)
        self.professor = QtGui.QHBoxLayout()
        self.professor.setObjectName("professor")
        self.label_professor = QtGui.QLabel(self.aba_aula)
        self.label_professor.setObjectName("label_professor")
        self.professor.addWidget(self.label_professor)
        self.input_professor = QtGui.QLineEdit(self.aba_aula)
        self.input_professor.setText("")
        self.input_professor.setObjectName("input_professor")
        self.professor.addWidget(self.input_professor)
        self.verticalLayout.addLayout(self.professor)
        self.sobre_prof = QtGui.QVBoxLayout()
        self.sobre_prof.setObjectName("sobre_prof")
        self.lavel_sobreprof = QtGui.QLabel(self.aba_aula)
        self.lavel_sobreprof.setObjectName("lavel_sobreprof")
        self.sobre_prof.addWidget(self.lavel_sobreprof)
        self.input_sobreprof = QtGui.QTextEdit(self.aba_aula)
        self.input_sobreprof.setReadOnly(True)
        self.input_sobreprof.setObjectName("input_sobreprof")
        self.sobre_prof.addWidget(self.input_sobreprof)
        self.verticalLayout.addLayout(self.sobre_prof)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.aba_aula, "")
        self.aba_sala = QtGui.QWidget()
        self.aba_sala.setObjectName("aba_sala")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.aba_sala)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.aba_sala)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.aba_sala)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(self.aba_sala)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.aba_sala)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_3 = QtGui.QLabel(self.aba_sala)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.aba_sala, "")
        self.aba_tpdo = QtGui.QWidget()
        self.aba_tpdo.setObjectName("aba_tpdo")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.aba_tpdo)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtGui.QTableWidget(self.aba_tpdo)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(20)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(193)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtGui.QLabel(self.aba_tpdo)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.aba_tpdo)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtGui.QLabel(self.aba_tpdo)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.aba_tpdo)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtGui.QLabel(self.aba_tpdo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.dateEdit = QtGui.QDateEdit(self.aba_tpdo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_7.addWidget(self.dateEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.aba_tpdo, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Detalhes"))
        self.label_materia.setText(_translate("Form", "Matéria"))
        self.label_abreviacao.setText(_translate("Form", "Abreviação"))
        self.label_sobremateria.setText(_translate("Form", "Sobre a matéria:"))
        self.label_professor.setText(_translate("Form", "Professor"))
        self.lavel_sobreprof.setText(_translate("Form", "Sobre o professor:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aba_aula), _translate("Form", "Aula"))
        self.label.setText(_translate("Form", "Sala"))
        self.label_2.setText(_translate("Form", "Andar"))
        self.label_3.setText(_translate("Form", "Imagem"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aba_sala), _translate("Form", "Sala"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "13/05"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "Modsim"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("Form", "Adicionar um lembrete"))
        self.pushButton.setText(_translate("Form", "Salvar"))
        self.label_4.setText(_translate("Form", "Nome"))
        self.label_5.setText(_translate("Form", "Data"))
        self.dateEdit.setDisplayFormat(_translate("Form", "dd/MM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aba_tpdo), _translate("Form", "To do"))
if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()        


#Fazer a função para aba editar perfil

#



#fazer a qline edit mudar de cor conforme o texto ta certo ou errado
#checar se o usuario ja existe
#confirmação de cadastro via email
#preencha os campos mínimos por favor
#esqueci a senha, manda email para a pessoa
#linkar o calendário com o menu
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abas.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

class Ui_abas_calendario(QtGui.QWidget):
    def __init__ (self):
        super(Ui_abas_calendario, self).__init__()
       
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
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
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
        self.tabWidget.setCurrentIndex(2)
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
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("Form", "13/05"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("Form", "Modsim"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("Form", "Adicionar um lembrete"))
        self.pushButton.setText(_translate("Form", "Salvar"))
        self.label_4.setText(_translate("Form", "Nome"))
        self.label_5.setText(_translate("Form", "Data"))
        self.dateEdit.setDisplayFormat(_translate("Form", "dd/MM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aba_tpdo), _translate("Form", "To do"))
      

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    teste = Ui_abas_calendario()
    teste.show()
    sys.exit(app.exec_())
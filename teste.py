# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:05:49 2016

@author: Matheus
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog
import Layouts

app = QApplication(sys.argv)
window = QDialog()
ui = Layouts.Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
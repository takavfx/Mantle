#!/usr/bin/env python

from PySide import QtCore, QtGui
from PySide.QtUiTools import QUiLoader

import define as DEFINE

class Preferences(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Preferences, self).__init__(parent)
        self._parent = parent
        
        self.initGUI()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.UI)
        self.setLayout(layout)

    def initGUI(self):
        loader = QUiLoader()
        self.UI = loader.load(DEFINE.preferencesUIPath)

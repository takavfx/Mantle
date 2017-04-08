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

        self.setSignals()


    def initGUI(self):
        loader = QUiLoader()
        self.UI = loader.load(DEFINE.preferencesUIPath)


    def setSignals(self):
        self.UI.setMovableCheckBox.clicked.connect(self.setMovableToggle)
        self.UI.setCloseableCheckBox.clicked.connect(self.setClosableToggle)


    def setMovableToggle(self):
        toggle = self.UI.setMovableCheckBox.checkState()
        if toggle:
            self._parent.setMovable(True)
        else:
            self._parent.setMovable(False)


    def setClosableToggle(self):
        toggle = self.UI.setCloseableCheckBox.checkState()
        if toggle:
            self._parent.setTabsClosable(True)
        else:
            self._parent.setTabsClosable(False)

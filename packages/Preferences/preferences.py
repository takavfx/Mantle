#!/usr/bin/env python

import os
import platform
import ConfigParser

from PySide import QtCore, QtGui
from PySide.QtUiTools import QUiLoader

import define as DEFINE



class Preferences(QtGui.QWidget):


    def __init__(self, parent=None):
        super(Preferences, self).__init__(parent)
        self._parent = parent
        self._config = ConfigParser.SafeConfigParser()

        self.initGUI()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.UI)
        self.setLayout(layout)

        self.setSignals()

        self.loadConfig()


    def initGUI(self):
        loader = QUiLoader()
        self.UI = loader.load(DEFINE.preferencesUIPath)


    def setSignals(self):
        self.UI.setMovableCheckBox.clicked.connect(self.setMovableToggle)
        self.UI.setClosableCheckBox.clicked.connect(self.setClosableToggle)


    def loadConfig(self):
        system = platform.system()
        if system == 'Linux':
            self._ini_file = os.path.join(os.environ.get('HOME'), DEFINE.config_name)
        elif system == 'Mac':
            self._ini_file = os.path.join(os.environ.get('HOME'), DEFINE.config_name)
        elif system == 'Windows':
            self._ini_file = os.path.join(os.environ.get('APPDATA'), DEFINE.config_name)

        if os.path.exists(self._ini_file):
            self._config.read(self._ini_file)
        else:
            self.writeAction()

        if self._config.has_section('Preferences'):
            self.loadAction()


    def loadAction(self):
        if self._config.get('Preferences', 'movable'):
            self.UI.setMovableCheckBox.setCheckState(QtCore.Qt.CheckState(int(self._config.get('Preferences', 'movable'))))
            self.setMovableToggle()

        if self._config.get('Preferences', 'closable'):
            self.UI.setClosableCheckBox.setCheckState(QtCore.Qt.CheckState(int(self._config.get('Preferences', 'closable'))))
            self.setClosableToggle()


    def writeAction(self):
        if not self._config.has_section('Preferences'):
            self._config.add_section('Preferences')
        self._config.set('Preferences', 'movable', str(int(self.UI.setMovableCheckBox.checkState())))
        self._config.set('Preferences', 'closable', str(int(self.UI.setClosableCheckBox.checkState())))

        with open(self._ini_file, 'w') as f:
            self._config.write(f)


    def writeConfigFile(self):
        with open(self._ini_file, 'w') as f:
            self._config.write(f)


    def setMovableToggle(self):
        toggle = self.UI.setMovableCheckBox.checkState()
        if toggle:
            self._parent.setMovable(True)
        else:
            self._parent.setMovable(False)
        self._config.set('Preferences', 'movable', str(int(toggle)))

        self.writeConfigFile()


    def setClosableToggle(self):
        toggle = self.UI.setClosableCheckBox.checkState()
        if toggle:
            self._parent.setTabsClosable(True)
        else:
            self._parent.setTabsClosable(False)
        self._config.set('Preferences', 'closable', str(int(toggle)))

        self.writeConfigFile()

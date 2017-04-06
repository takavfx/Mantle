#!/usr/bin/env python

from PySide import QtCore, QtGui, QtSvg

import define as DEFINE
reload(DEFINE)
import preferences as Prefs
reload(Prefs)

class MantraMainWindow(QtGui.QMainWindow):

    _windowTitle  = DEFINE.windowTitle
    _windowHeight = DEFINE.windowHeight
    _windowWidth  = DEFINE.windowWidth
    _mantleIcon   = DEFINE.mantleIconPath
    _prefsIcon    = DEFINE.preferencesIconPath

    def __init__(self, parent=None):
        super(MantraMainWindow, self).__init__(parent)

        self.initGUI()

        self.createActions()
        self.createTrayIcon()
        self.trayIcon.show()

        self.setWindowTitle(self._windowTitle)
        self.setWindowIcon(self._mantleIcon)

        self.createBaseTabWidget()
        self.setCentralWidget(self.baseTabWidget)

        self.setGeometry(0, 0, self._windowWidth, self._windowHeight)


    def initGUI(self):
        self.resize(self._windowWidth, self._windowHeight)


    def setSignals(self):
        pass


    def createActions(self):
        self.showAction = QtGui.QAction("Show", self,
                triggered=self.show)

        self.hideAction = QtGui.QAction("Hide", self,
                triggered=self.hide)

        self.raiseAction = QtGui.QAction("Bring to Top", self,
                triggered=self.raise_)

        self.maximizeAction = QtGui.QAction("Maximize", self,
                triggered=self.showMaximized)

        self.quitAction = QtGui.QAction("Quit", self,
                triggered=QtGui.qApp.quit)


    def createTrayIcon(self):
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.showAction)
        self.trayIconMenu.addAction(self.hideAction)
        self.trayIconMenu.addAction(self.raiseAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        self.trayIcon.setIcon(self._mantleIcon)


    def createBaseTabWidget(self):
        self.baseTabWidget = QtGui.QTabWidget(self)
        self.baseTabWidget.addTab(Prefs.Preferences(self), self._prefsIcon, "Preferences")



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    mainWindow = MantraMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

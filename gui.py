#!/usr/bin/env python

import webbrowser
from PySide import QtCore, QtGui, QtSvg

import define as DEFINE
reload(DEFINE)
import preferences as Prefs
reload(Prefs)

class MainWindow(QtGui.QMainWindow):
    """
    Main window class of this tool.
    """
    _windowTitle  = DEFINE.windowTitle
    _windowHeight = DEFINE.windowHeight
    _windowWidth  = DEFINE.windowWidth
    _mantleIcon   = DEFINE.mantleIconPath

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initGUI()

        self.createActions()
        self.createTrayIcon()
        self.trayIcon.show()

        self.setWindowTitle(self._windowTitle)
        self.setWindowIcon(self._mantleIcon)

        ## Generate Widgets
        tabs = TabController(self)
        self.setCentralWidget(tabs)

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

        self.openGitHubAction = QtGui.QAction("GitHub on Mantle", self,
                triggered=self.openGitHubButtonTriggered)


    def openGitHubButtonTriggered(self):
        webbrowser.open('http://github.com/takavfx/Mantle')


    def createTrayIcon(self):
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.showAction)
        self.trayIconMenu.addAction(self.hideAction)
        self.trayIconMenu.addAction(self.raiseAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.openGitHubAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        self.trayIcon.setIcon(self._mantleIcon)



class TabController(QtGui.QTabWidget):
    """
    Tab Controller cantains get tabs from packages and set tabs.
    """

    def __init__(self, parent=None):
        super(TabController, self).__init__(parent)
        self._parent = parent

        self.createBaseTabWidget()


    def createBaseTabWidget(self):
        self.setMovable(True)
        self.setInitialTabs()


    def setInitialTabs(self):
        self.setPareferences()


    def setPareferences(self):
        self.addTab(Prefs.Preferences(self._parent),
                DEFINE.preferencesIconPath, "Preferences")


    def getTabIndex(self, name):
        while index in self.count():
            if self.tabText(i) == name:
                return index



def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()

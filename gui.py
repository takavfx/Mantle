#!/usr/bin/env python

import os
import webbrowser
from PySide import QtCore, QtGui, QtSvg

import define as DEFINE
import preferences as Prefs

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))



class MainWindow(QtGui.QMainWindow):
    """
    Main window class of this tool.
    """
    _windowTitle  = DEFINE.windowTitle
    _windowHeight = DEFINE.windowHeight
    _windowWidth  = DEFINE.windowWidth
    mantleIcon    = QtGui.QIcon(DEFINE.mantleIconPath)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initGUI()

        self.createActions()
        self.createTrayIcon()
        self.trayIcon.show()

        self.setWindowTitle(self._windowTitle)
        self.setWindowIcon(self.mantleIcon)

        ## Generate Widgets
        tabs = TabController(self)
        self.setCentralWidget(tabs)

        self.setGeometry(0, 0, self._windowWidth, self._windowHeight)


    def initGUI(self):
        self.resize(self._windowWidth, self._windowHeight)


    def openGitHubButtonTriggered(self):
        webbrowser.open('http://github.com/takavfx/Mantle')


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


    def createTrayIcon(self):
        trayIconMenu = QtGui.QMenu(self)
        trayIconMenu.addAction(self.showAction)
        trayIconMenu.addAction(self.hideAction)
        trayIconMenu.addAction(self.raiseAction)
        trayIconMenu.addAction(self.maximizeAction)
        trayIconMenu.addSeparator()
        trayIconMenu.addAction(self.openGitHubAction)
        trayIconMenu.addSeparator()
        trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(trayIconMenu)

        self.trayIcon.setIcon(self.mantleIcon)




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
        self.setImportedPackageTabs()
        self.setInitialTabs()


    def setInitialTabs(self):
        self.setPareferences()


    def setPareferences(self):
        self.addTab(Prefs.Preferences(self._parent),
                QtGui.QIcon(DEFINE.preferencesIconPath), "Preferences")


    def setImportedPackageTabs(self):
        packageNames = ['packages.%s'%x for x in os.listdir('%s/packages'%_CURRENTPATH)]
        packageNames.remove('packages.__init__.py')
        packageNames.remove('packages.__init__.pyc')

        import importlib
        for package in packageNames:
            module = importlib.import_module(package)
            widget, icon,title = module.getWidget(self._parent)
            if icon is None:
                icon = QtGui.QIcon(DEFINE.defaultIconPath)
                self.addTab(widget, icon, title)
            else:
                self.addTab(widget, icon, title)


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

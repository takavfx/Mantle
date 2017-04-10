#!/usr/bin/env python

import os
import webbrowser
from functools import partial
import importlib

from PySide import QtCore, QtGui, QtSvg

import define as DEFINE

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

        self.resize(self._windowWidth, self._windowHeight)
        # self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())

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

        self.openGitHubAction = QtGui.QAction("Mantle on GitHub", self,
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

        self.createBaseTabWidget()
        self.setSignals()


    def createBaseTabWidget(self):
        self.setCornerWidget(self.createAddButton())
        self.setImportedPackageTabs()


    def setSignals(self):
        self.tabCloseRequested.connect(self.close_handler)


    def close_handler(self, index):
        if self.count() != 1:
            self.removeTab(index)


    def createAddButton(self):
        self.addTabMenu = QtGui.QMenu(self)

        button = QtGui.QPushButton()
        button.setFlat(True)
        button.setIcon(QtGui.QIcon(os.path.join(_CURRENTPATH, 'static', 'plus.svg')))
        button.setMenu(self.addTabMenu)
        return button


    def setImportedPackageTabs(self):
        packageNames = ['packages.%s'%x for x in os.listdir('%s/packages'%_CURRENTPATH)]
        try:
            packageNames.remove('packages.__init__.py')
            packageNames.remove('packages.__init__.pyc')
        except:
            pass

        for package in packageNames:
            widget, icon, title = self.addTabByPackage(package)

            ## Add tab action
            cmd    = partial(self.addTabByPackage, package)
            action = QtGui.QAction(title, self,
                    triggered=cmd)
            self.addTabMenu.addAction(action)


    def addTabByPackage(self, package):
        module = importlib.import_module(package)
        widget, icon, title = module.getWidget(self)
        index = self.getTabIndexByTitle(title)
        if index is None:
            if icon is None:
                icon = QtGui.QIcon(DEFINE.defaultIconPath)
                self.addTab(widget, icon, title)
            else:
                self.addTab(widget, icon, title)

            return widget, icon, title


    def getTabIndexByTitle(self, title):
        index = 0
        while index < self.count():
            if self.tabText(index) == title:
                return index

            index += 1

        return None





def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()

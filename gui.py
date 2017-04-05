#!/usr/bin/env python

from PySide import QtCore, QtGui, QtSvg

import define as DEFINE
reload(DEFINE)

class MantraMainWindow(QtGui.QMainWindow):

    _windowTitle = DEFINE.windowTitle
    _mantleIcon  = QtGui.QIcon(DEFINE.mantleIconPath)

    def __init__(self, parent=None):
        super(MantraMainWindow, self).__init__(parent)

        self.initGUI()

        self.createActions()
        self.createTrayIcon()
        self.trayIcon.show()

        self.setWindowTitle(self._windowTitle)
        self.setWindowIcon(self._mantleIcon)
        self.setWindowsPosition()

    def initGUI(self):
        self.resize(1200, 800)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def setWindowsPosition(self):
        pos = self.pos()

        if pos.x() < 0:
            pos.setX(0)

        if pos.y() < 0:
            pos.setY(0)


    def createActions(self):
        self.showAction = QtGui.QAction("Show", self,
                triggered=self.show)

        self.hideAction = QtGui.QAction("Hide", self,
                triggered=self.hide)

        self.maximizeAction = QtGui.QAction("Ma&ximize", self,
                triggered=self.showMaximized)

        self.quitAction = QtGui.QAction("&Quit", self,
                triggered=QtGui.qApp.quit)


    def createTrayIcon(self):
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.showAction)
        self.trayIconMenu.addAction(self.hideAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        self.trayIcon.setIcon(self._mantleIcon)


    # def mousePressEvent(self, event):
    #     if QtCore.Qt.FramelessWindowHint:
    #         self.offset = event.pos()
    #
    # def mouseMoveEvent(self, event):
    #     x=event.globalX()
    #     y=event.globalY()
    #     x_w = self.offset.x()
    #     y_w = self.offset.y()
    #     self.move(x-x_w, y-y_w)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWindow = MantraMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

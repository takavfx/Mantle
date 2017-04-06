#!/usr/bin/env python


from PySide import QtCore, QtGui

import define as DEFINE
reload(DEFINE)

class Preferences(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Preferences, self).__init__(parent)

        textEdit = QtGui.QTextEdit()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(textEdit)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

import os
import sys

from PySide import QtGui

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))



mantleIconPath = QtGui.QIcon(os.path.join(_CURRENTPATH, 'static', 'mantle_icon.svg'))

preferencesIconPath = QtGui.QIcon(os.path.join(_CURRENTPATH, 'static', 'gear.svg'))
preferencesUIPath = os.path.join(_CURRENTPATH, 'ui', 'preferences.ui')

version = '0.1.0'

windowHeight = 800
windowName   = 'mantleWindow'
windowTitle  = "Mantle"
windowWidth  = 1200

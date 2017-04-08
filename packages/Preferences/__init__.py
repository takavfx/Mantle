#!/usr/bin/env python

import os
from PySide import QtGui
import preferences

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))

def getWidget(parent):
    widget = preferences.Preferences(parent)
    icon   = QtGui.QIcon(os.path.join(_CURRENTPATH, 'static', 'gear.svg'))
    title  = 'Preferences'
    return widget, icon, title

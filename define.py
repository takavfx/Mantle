import os
import sys

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))

defaultIconPath = os.path.join(_CURRENTPATH, 'static', 'cubes.svg')

gitHubIconPath = os.path.join(_CURRENTPATH, 'static', 'github.svg')

mantleIconPath = os.path.join(_CURRENTPATH, 'static', 'mantle_icon.svg')

preferencesIconPath = os.path.join(_CURRENTPATH, 'static', 'gear.svg')
preferencesUIPath = os.path.join(_CURRENTPATH, 'ui', 'preferences.ui')

version = '0.1.0'

windowHeight = 800
windowName   = 'mantleWindow'
windowTitle  = "Mantle"
windowWidth  = 1200

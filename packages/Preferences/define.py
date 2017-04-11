import os

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))

config_name = 'mantle_config.ini'

preferencesIconPath = os.path.join(_CURRENTPATH, 'static', 'gear.svg')
preferencesUIPath = os.path.join(_CURRENTPATH, 'ui', 'preferences.ui')

version = '0.1.0'

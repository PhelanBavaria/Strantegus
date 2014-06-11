

import os
from importlib import import_module

maps = {}

for module in os.listdir(os.path.dirname(__file__)):
    if module != '__init__.py' and module[-3:] == '.py':
        gmap = import_module('maps.'+module[:-3])
        maps[module[:-3]] = gmap

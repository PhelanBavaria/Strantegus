

import os
from importlib import import_module

from maps import test
maps = {'test': test}

#maps = {}
#
#path = os.path.dirname(__file__)
#for module in os.listdir(path):
#    if module != '__init__.py' and module[-3:] == '.py':
#        gmap = import_module('maps.'+module[:-3])
#        maps[module[:-3]] = gmap

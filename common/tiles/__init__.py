

from common.tiles.tile import BaseTile
from common.tiles.scent import Scent
from common.tiles.resource import Resource
from common.tiles.grass import Grass
from common.tiles.stone import Stone
from common.tiles.water import Water
from common.tiles.leave import Leave
from common.tiles.sugar import Sugar
from common.tiles.fungus import Fungus
from common.tiles.colony_entrance import ColonyEntrance
from common.tiles.colony_wall import ColonyWall


tiles = {
    'base': BaseTile,
    'scent': Scent,
    'grass': Grass,
    'stone': Stone,
    'water': Water,
    'leave': Leave,
    'sugar': Sugar,
    'fungus': Fungus,
    'colony_entrance': ColonyEntrance,
    'colony_wall': ColonyWall
}

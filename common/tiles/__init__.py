from common.tiles.tile import BaseTile
from common.tiles.resource import Resource
from common.tiles.grass import Grass
from common.tiles.dirt import Dirt
from common.tiles.resources.stone import Stone
from common.tiles.resources.water import Water
from common.tiles.resources.leave import Leave
from common.tiles.resources.sugar import Sugar
from common.tiles.resources.fungus import Fungus
from common.tiles.dirt_wall import DirtWall
from common.tiles.colony_entrance import ColonyEntrance
from common.tiles.colony_wall import ColonyWall


tiles = {
    'base': BaseTile,
    'grass': Grass,
    'dirt': Dirt,
    'stone': Stone,
    'water': Water,
    'leave': Leave,
    'sugar': Sugar,
    'fungus': Fungus,
    'dirt_wall': DirtWall,
    'colony_entrance': ColonyEntrance,
    'colony_wall': ColonyWall
}

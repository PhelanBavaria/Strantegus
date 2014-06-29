from common.tiles.tile import BaseTile
from common.tiles.scent import Scent
from common.tiles.resource import Resource
from common.tiles.grass import Grass
from common.tiles.dirt import Dirt
from common.tiles.dirt_wall import DirtWall
from common.tiles.colony_entrance import ColonyEntrance
from common.tiles.colony_wall import ColonyWall
from common.tiles.resources import Stone
from common.tiles.resources import Water
from common.tiles.resources import Leave
from common.tiles.resources import Sugar
from common.tiles.resources import Fungus


tiles = {
    'grass': Grass,
    'dirt': Dirt,
    'dirt_wall': DirtWall,
    'colony_entrance': ColonyEntrance,
    'colony_wall': ColonyWall,
    'stone': Stone,
    'water': Water,
    'leave': Leave,
    'sugar': Sugar,
    'fungus': Fungus
}

import collections

import mobs

TILE_TYPES = {
    'door': '+',
    'floor': '.',
    'wall': '#',
}

TILE_TYPES.update(
    {'L{} {}'.format(level, name): char for char, name, level in mobs.MOB_TYPES.values()})

TILE_TYPE_SELECT = collections.OrderedDict(sorted(zip(
    TILE_TYPES.keys(), ["{} {}".format(char, name) for name, char in TILE_TYPES.items()])))


class Tile(object):

    def __init__(self, tile_type):
        self.name = tile_type
        self.char = TILE_TYPES[tile_type]

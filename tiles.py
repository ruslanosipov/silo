import collections

TILE_TYPES = {
    'door': '+',
    'floor': '.',
    'wall': '#',

    'enemy': 'e',

    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
}

TILE_TYPE_SELECT = collections.OrderedDict(sorted(zip(
    TILE_TYPES.keys(), ["{} {}".format(char, name) for name, char in TILE_TYPES.items()])))


class Tile(object):

    def __init__(self, tile_type):
        self.name = tile_type
        self.char = TILE_TYPES[tile_type]

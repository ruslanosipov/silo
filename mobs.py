import collections

Mob = collections.namedtuple('Mob', ['char', 'name', 'level'])

MIN_LEVEL = 1
MAX_LEVEL = 20

MOB_TYPES = {
    'rat': Mob(char='r', name='rat', level=1),
    'farmer': Mob(char='f', name='farmer', level=2),
    'bandit': Mob(char='b', name='bandit', level=3),
    'mutant': Mob(char='M', name='mutant', level=20),
}

MOB_TYPE_SELECT = collections.OrderedDict(
    sorted(
        zip(
            MOB_TYPES.keys(),
            ["{} L{} {}".format(char, level, name) for name, (char, _, level) in MOB_TYPES.items()]
        )))


class Mob(object):

    def __init__(self, mob_type):
        self.char, self.name, self.level = MOB_TYPES[mob_type]


def generate_random_mob(player_level):
    pass

import bisect
import collections
import random

Mob = collections.namedtuple('Mob', ['char', 'name', 'level'])

RANDOM_INTERVAL_SIZE = 100
RANDOM_MOB_LEVEL_FACTOR = 0.3  # Float 0..1, lower numbers decrease probability of diff level mobs.

MOB_TYPES = {
    'rat': Mob(char='r', name='rat', level=1),
    'dog': Mob(char='d', name='dog', level=1),
    'cat': Mob(char='c', name='cat', level=1),
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
    """Generate a random mob accounting for player level.

    Mobs of level close to player level have higher chance of spawning, while
    mobs way off have 0 chance to spawn. Mob level scaling is governed by
    RANDOM_MOB_LEVEL_FACTOR, with 0.5 halving the probability of getting a
    higher/lower level mob with each level delta.
    """
    intervals, next_i = [], 0
    for name, (_, _, level) in MOB_TYPES.iteritems():
        diff = max(player_level, level) - min(player_level, level)
        interval_size = RANDOM_INTERVAL_SIZE
        while diff > 0:
            interval_size *= RANDOM_MOB_LEVEL_FACTOR
            diff -= 1
        interval_size = int(interval_size)
        if interval_size == 0:
            continue
        intervals.append((next_i, interval_size, name))
        next_i += interval_size + 1
    fst, _, _ = zip(*intervals)
    rnd = random.randint(0, next_i - 1)
    idx = bisect.bisect(fst, rnd)
    mob_name = intervals[idx - 1][2]
    return Mob(mob_name)

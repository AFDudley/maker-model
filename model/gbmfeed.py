import math
import random


class GBMFeed:
    '''
    A price feed class that generates a random price index
    based on geometric brownian motion.
    '''

    MU = 0  # drift factor
    SIGMA = 0.0001  # volatility in %

    def __init__(self, start_value):
        self.values = [start_value]

    def next_value(self, delta_t):
        new_value = self.values[-1] * math.exp(
            (GBMFeed.MU - GBMFeed.SIGMA**2 / 2) * delta_t +
            GBMFeed.SIGMA * random.normalvariate(0, delta_t**2))
        self.values.append(new_value)
        return new_value

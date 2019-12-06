import numpy as np

from be.kdg.rl.Environment import Environment


class Policy:
    def __init__(self, env: Environment):
        self._π = np.full((env.observation_space_size, env.action_space_size), 1 / env.action_space_size, dtype=float)

    @property
    def π(self):
        return self._π

    @π.setter
    def π(self, value):
        self._π = value
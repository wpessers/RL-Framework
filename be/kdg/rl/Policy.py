import numpy as np

from be.kdg.rl.Environment import Environment


class Policy:
    def __init__(self, env: Environment):
        self._pi = np.full((env.observation_space_size, env.action_space_size), 1 / env.action_space_size, dtype=float)

    @property
    def pi(self):
        return self._pi

    @pi.setter
    def pi(self, value):
        self._pi = value

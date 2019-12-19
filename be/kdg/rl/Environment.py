import time

import gym

from be.kdg.rl.Percept import Percept
from gym.envs.registration import register


class Environment(gym.Wrapper):
    def __init__(self):
        env = gym.make("FrozenLake-v0")
        super().__init__(env)
        self._s = self.reset()

    @property
    def state(self):
        return self._s

    @state.setter
    def state(self, value):
        self._s = value

    @property
    def action_space_size(self):
        return self.action_space.n

    @property
    def observation_space_size(self):
        return self.observation_space.n

    def step(self, action):
        next_state, reward, final, info = super().step(action)
        percept = Percept(self.state, action, next_state, reward, final)
        self.state = next_state
        return percept

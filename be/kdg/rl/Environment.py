import gym

from be.kdg.rl.Percept import Percept


class Environment(gym.Wrapper):
    def __init__(self):
        env = gym.make("FrozenLake-v0")
        super().__init__(env)
        self._s = self.reset()

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value

    @property
    def action_space_size(self):
        return self.action_space.n

    @property
    def observation_space_size(self):
        return self.observation_space.n

    def step(self, a):
        t, r, final, info = super().step(a)
        percept = Percept(self.s, a, r, t, final)
        return percept

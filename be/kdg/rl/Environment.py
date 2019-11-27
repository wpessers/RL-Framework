import gym

from be.kdg.rl.Percept import Percept


class Environment:
    def __init__(self):
        self.env = gym.make("FrozenLake-v0")
        self.s = self.env.reset()
        self.observation_space_size = self.env.observation_space.n
        self.action_space_size = self.env.action_space.n

    def step(self, a):
        st, r, final, info = self.env.step(a)
        percept = Percept(self.s, a, r, st, final)
        self.s = st
        return percept

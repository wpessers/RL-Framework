import math
import time
from numpy.random import choice

import emoji as emoji
import numpy as np
from tabulate import tabulate

from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Policy import Policy


class QLearnStrategy(LearningStrategy):
    def __init__(self, α, γ, λ, εmax, εmin, mdp: MDP, policy: Policy):
        super().__init__(α, γ, λ, εmax, εmin)
        self.mdp = mdp
        self.q = np.zeros(mdp.Nsa.shape)
        self.policy = policy

    def evaluate(self, percept):
        s, a, t = percept.s, percept.a, percept.t
        self.mdp.update(percept)
        # Gebruik van np.sum(Rtsa[s][a]) of zoals dit?
        self.q[s][a] = self.q[s][a] + self.α * (percept.r + self.γ * np.max(self.q[t]) - self.q[s][a])

    def improve(self, episode_count):
        for s in range(16):
            a_ster = self.random_argmax(self.q[s])
            for a in range(4):
                if a == a_ster:
                    self.policy.π[s][a] = 1 - self.ε + (self.ε / self.mdp.action_space_size)
                else:
                    self.policy.π[s][a] = self.ε / self.mdp.action_space_size
        self.ε = self.εmin + (self.εmax - self.εmin) * math.exp(-self.λ * episode_count)

        # print(tabulate(self.q))

    def print(self):
        action_text = [':arrow_left:', ':arrow_down:', ':arrow_right:', ':arrow_up:']
        for state in range(len(self.policy.π)):
            if state % 4 == 0:
                print()
            if state % 16 == 0:
                print()
            print(emoji.emojize(action_text[np.argmax(self.policy.π[state])], use_aliases=True), end='')

    def next_action(self, s):
        # TODO change implementation of exploration
        return choice(np.arange(0, 4, 1), 1, p=self.policy.π[s])[0]
        # return np.random.choice(range(len(self.policy.π[s])), p=self.policy.π[s])

    def random_argmax(self, array):
        return np.random.choice(np.flatnonzero(np.isclose(array, array.max())))

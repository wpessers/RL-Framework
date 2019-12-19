import math
import time
import numpy as np

from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Policy import Policy
from numpy.random import choice

'''
    - α : learning_rate
    - γ : discount_factor
    - λ : exploration_decay_rate
    - ε : exploration_rate
    - π : policy
'''


class QLearnStrategy(LearningStrategy):
    def __init__(self, learning_rate, discount_factor, exploration_decay_rate, min_exploration_rate,
                 max_exploration_rate, policy, mdp: MDP):
        super().__init__(learning_rate, discount_factor, exploration_decay_rate, min_exploration_rate,
                         max_exploration_rate, policy)
        self._mdp = mdp
        self._qsa = np.zeros(mdp.Nsa.shape)

    def evaluate(self, percept):
        state, action, next_state, reward = percept.state, percept.action, percept.next_state, percept.reward
        self._mdp.update(percept)
        self._qsa[state, action] += \
            self.learning_rate * (
                    reward + (self.discount_factor * np.max(self._qsa[next_state])) - self._qsa[state, action]
            )

    @property
    def qsa(self):
        return self._qsa

    def random_argmax(self, array):
        return np.random.choice(np.flatnonzero(np.isclose(array, array.max())))

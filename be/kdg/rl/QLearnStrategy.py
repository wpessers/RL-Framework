import math
import time
import numpy as np

from be.kdg.rl.Environment import Environment
from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.MDP import MDP
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
                 max_exploration_rate, mdp: MDP, env: Environment):
        super().__init__(learning_rate, discount_factor, exploration_decay_rate, min_exploration_rate,
                         max_exploration_rate, env)
        self._mdp = mdp
        self._qsa = np.zeros(mdp.Nsa.shape, dtype=float)
        self.temp_epct = 1

    def evaluate(self, percept):
        self._mdp.update(percept)
        self._qsa[percept.state, percept.action] = self._qsa[percept.state, percept.action] + self.learning_rate * (
                percept.reward
                + self.exploration_decay_rate * max(self._qsa[percept.next_state]) -
                self._qsa[percept.state, percept.action]
        )

    def improve(self, episode_count):
        if self.temp_epct != episode_count and self.exploration_rate == self.min_exploration_rate:
            print("episode: " + str(episode_count))
            print(self._qsa)
        for state in range(self.environment.observation_space.n):
            a_best = self.random_argmax(self._qsa[state])

            action = 0
            while action < self.environment.action_space.n:
                if action == a_best:
                    self.policy[state, action] = 1 - self.exploration_rate + (
                            self.exploration_rate / self.environment.action_space.n)
                else:
                    self.policy[state, action] = self.exploration_rate / self.environment.action_space.n

                action += 1

        self.exploration_rate = self.min_exploration_rate + (
                self.max_eploration_rate - self.min_exploration_rate) * math.e ** (
                                        -self.exploration_decay_rate * episode_count)
        self.temp_epct = episode_count


    def random_argmax(self, array):
        return np.random.choice(np.flatnonzero(np.isclose(array, array.max())))

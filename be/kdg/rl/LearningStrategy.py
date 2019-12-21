import abc
from numpy.random import choice

import emoji as emoji
import numpy as np

from be.kdg.rl.Environment import Environment
from be.kdg.rl.Percept import Percept

'''
    - α : learning_rate
    - γ : discount_factor
    - λ : exploration_decay_rate
    - ε : exploration_rate
    - π : policy
'''


class LearningStrategy:
    def __init__(self, learning_rate, discount_factor, exploration_decay_rate, min_exploration_rate,
                 max_exploration_rate, environment: Environment):
        __metaclass__ = abc.ABCMeta
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self._exploration_decay_rate = exploration_decay_rate
        self._exploration_rate = max_exploration_rate
        self._min_exploration_rate = min_exploration_rate
        self._max_exploration_rate = max_exploration_rate
        self._policy = np.full((environment.observation_space.n, environment.action_space.n),
                               1 / environment.action_space.n, dtype=float)
        self._environment = environment

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def discount_factor(self):
        return self._discount_factor

    @property
    def exploration_decay_rate(self):
        return self._exploration_decay_rate

    @property
    def exploration_rate(self):
        return self._exploration_rate

    @exploration_rate.setter
    def exploration_rate(self, value):
        self._exploration_rate = value

    @property
    def min_exploration_rate(self):
        return self._min_exploration_rate

    @property
    def max_eploration_rate(self):
        return self._max_exploration_rate

    @property
    def policy(self):
        return self._policy

    @property
    def environment(self):
        return self._environment

    def learn(self, percept: Percept, episode_count):
        self.evaluate(percept)
        self.improve(episode_count)

    @abc.abstractmethod
    def improve(self, episode_count):
        return

    @abc.abstractmethod
    def evaluate(self, percept):
        return

    def next_action(self, state):
        return choice(np.arange(0, self.environment.action_space.n, 1), 1, p=self.policy[state])[0]

    def print(self):
        action_text = [':arrow_left:', ':arrow_down:', ':arrow_right:', ':arrow_up:']
        for state in range(self.environment.observation_space.n):
            if state % self.environment.action_space.n == 0:
                print()
            print(emoji.emojize(action_text[np.argmax(self.policy[state])], use_aliases=True), end='')
        print()
        print('Exploration probability: ' + str(self.exploration_rate))
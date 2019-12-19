import abc

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
                 max_exploration_rate, policy):
        __metaclass__ = abc.ABCMeta
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self._exploration_decay_rate = exploration_decay_rate
        self._exploration_rate = max_exploration_rate
        self._min_exploration_rate = min_exploration_rate
        self._max_exploration_rate = max_exploration_rate
        self._policy = policy

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def discount_factor(self):
        return self._discount_factor

    @property
    def eploration_decay_rate(self):
        return self._exploration_decay_rate

    @property
    def eploration_rate(self):
        return self._exploration_rate

    @property
    def min_eploration_decay_rate(self):
        return self._min_exploration_rate

    @property
    def max_eploration_decay_rate(self):
        return self._max_exploration_rate

    @property
    def policy(self):
        return self._policy

    def learn(self, percept: Percept, episode_count):
        self.evaluate(percept)
        self.improve(episode_count)

    @abc.abstractmethod
    def improve(self, episode_count):
        return

    @abc.abstractmethod
    def evaluate(self, percept):
        return

    @abc.abstractmethod
    def next_action(self, state):
        return

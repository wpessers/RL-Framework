import numpy as np

from be.kdg.rl.Environment import Environment
from be.kdg.rl.Episode import Episode
from be.kdg.rl.MDP import MDP
from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.QLearnStrategy import QLearnStrategy


class Agent:
    def __init__(self, strategy: LearningStrategy, environment: Environment):
        self._strategy = strategy
        self._environment = environment
        self._policy = np.full((self.environment.observation_space_size, self.environment.action_space_size),
                               1 / self.environment.action_space_size, dtype=float)

    @property
    def strategy(self):
        return self._strategy

    @property
    def environment(self):
        return self._environment

    def learn(self, n_episodes):
        episode_count = 0
        while episode_count < n_episodes:
            episode = Episode()
            state = self.environment.state
            while not episode.done:
                action = self.strategy.next_action(state)
                percept = self.environment.step(action)
                self.strategy.learn(percept)
                state = percept.next_state
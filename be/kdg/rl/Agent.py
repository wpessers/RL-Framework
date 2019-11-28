from be.kdg.rl.Environment import Environment
from be.kdg.rl.Episode import Episode


class Agent:
    def __init__(self, strategy, environment: Environment):
        self._strategy = strategy
        self._environment = environment

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
            state = self.environment.s

            while not episode.done:
                #TODO: action uit strategy halen
                action = 1
                percept = self.environment.step(1)
                #TODO: strategy.learn implementeren

                state = percept.t
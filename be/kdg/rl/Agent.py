from be.kdg.rl.Environment import Environment
from be.kdg.rl.Episode import Episode
from be.kdg.rl.MDP import MDP


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
        mdp = MDP(self.environment.observation_space_size, self.environment.action_space_size)
        episode_count = 0
        for episode_count in range(n_episodes):
            episode = Episode()
            state = self.environment.s

            while not episode.done:
                #TODO: action uit strategy halen
                action = 1
                percept = self.environment.step(1)
                self.environment.render()
                print(percept)
                #TODO: strategy.learn implementeren
                mdp.update(percept)
                state = percept.t

                episode.add_percept(percept)

            self.environment.reset()

        print("Nsa:")
        print(mdp.Nsa)
        print("Ntsa:")
        print(mdp.Ntsa[0])
        print("Ptsa")
        print(mdp.Ptsa[0])
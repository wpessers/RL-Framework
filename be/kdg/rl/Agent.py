from be.kdg.rl.Environment import Environment
from be.kdg.rl.Episode import Episode
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Policy import Policy
from be.kdg.rl.QLearnStrategy import QLearnStrategy


class Agent:
    def __init__(self, strategy, environment: Environment):
        self._strategy = strategy
        self._environment = environment
        self._policy = Policy(self.environment)

    @property
    def strategy(self):
        return self._strategy

    @property
    def environment(self):
        return self._environment

    def learn(self, n_episodes):
        # TODO MDP meegeven aan QLearnStrategy of environment meegeven?
        mdp = MDP(self.environment.observation_space_size, self.environment.action_space_size)
        learning_strategy = QLearnStrategy(mdp=mdp, α=0.1, γ=0.1, ε=0.05, εmax=0.1, εmin=0.01, policy=self._policy)
        episode_count = 0
        for episode_count in range(n_episodes):
            if(episode_count>990):
                print('debug')
            # TODO: gebrik episode count
            episode = Episode()
            state = self.environment.s

            while not episode.done:
                # TODO: action uit strategy halen
                next_action = learning_strategy.next_action(state)
                percept = self.environment.step(next_action)
                self.environment.render()
                print(percept)
                learning_strategy.learn(eposiode_count=episode_count, percept=percept)
                # TODO: strategy.learn implementeren
                mdp.update(percept)
                state = percept.t

                episode.add_percept(percept)

            self.environment.reset()

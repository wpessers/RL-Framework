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
        learning_strategy = QLearnStrategy(mdp=mdp, α=0.3, γ=0.1, ε=0.005, εmax=0.01, εmin=0.001, policy=self._policy)
        episode_count = 0
        # gebruikt voor statistieken
        goal_reached_count = 0

        for episode_count in range(n_episodes):
            episode = Episode()
            state = self.environment.s

            while not episode.done:
                # TODO: action uit strategy halen
                next_action = learning_strategy.next_action(state)
                percept = self.environment.step(next_action)
                learning_strategy.learn(eposiode_count=episode_count, percept=percept)
                # TODO: strategy.learn implementeren
                mdp.update(percept)
                state = percept.t
                episode.add_percept(percept)

            if episode.percepts[-1].r == 1:
                goal_reached_count += 1

            if (episode_count % 500 == 0) & (episode_count > 0):
                print(
                    'Episode ' + str(episode_count) + ' Achieved goal in last 500 episodes: ' + str(
                        goal_reached_count) + ' (' + str(goal_reached_count / 500 * 100) + '%)')
                goal_reached_count = 0

            self.environment.reset()

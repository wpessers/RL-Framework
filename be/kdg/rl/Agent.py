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
        learning_strategy = QLearnStrategy(mdp=mdp, α=0.8, γ=0.95, εmax=1, εmin=0.0001, λ=0.01,
                                           policy=self._policy)
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
                state = percept.t
                episode.add_percept(percept)

            if episode.percepts[-1].r > 0:
                goal_reached_count += 1


            if episode_count % 500 == 0:
                print()
                print(episode_count)
                learning_strategy.print()
                print()

            print_statistics_per_episodes = 500
            if (episode_count % print_statistics_per_episodes == 0) & (episode_count > 0):
                print(
                    'Episode ' + str(episode_count) + ' Achieved goal in last ' + str(
                        print_statistics_per_episodes) + ' episodes: ' + str(
                        goal_reached_count) + ' (' + str(
                        goal_reached_count / print_statistics_per_episodes * 100) + '%)')
                goal_reached_count = 0
                print(learning_strategy.ε)

            self.environment.reset()

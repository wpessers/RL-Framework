from be.kdg.rl.Environment import Environment
from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.Percept import Percept


class Agent:
    def __init__(self, strategy: LearningStrategy, environment: Environment):
        self.strategy = strategy
        self.environment = environment

    def learn(self, n_episodes):
        episode_count = 0
        ct_goal = 0
        avg_reward_100_episode = 0
        max_avg_reward_100ep = 0
        ct_finished_100ep = 0
        max_finished_100ep = 0

        while episode_count < n_episodes:
            state = self.environment.reset()
            percept = Percept(0, 0, 0, 0, False)
            ct_percept = 0
            tot_reward_episode = 0
            while not percept.final:
                ct_percept += 1
                action = self.strategy.next_action(state)
                t, r, final, info = self.environment.step(action)
                percept = Percept(state, action, t, r, final)
                self.strategy.learn(percept, episode_count)
                state = percept.next_state
                #episode.add_percept(percept)

                #HIER BEGINNEN DE FUCKING STATISTIEKEN!!!
            #     if percept.reward > 0:
            #         tot_reward_episode += percept.reward
            #         ct_finished_100ep += 1
            #
            # avg_reward_100_episode += tot_reward_episode / ct_percept
            # '''
            # if episode_count % 50 == 0:
            #     #print(self.strategy.policy)
            #     self.strategy.print()
            # '''
            #
            # if episode_count > 0 and episode_count % 100 == 0:
            #     if avg_reward_100_episode > max_avg_reward_100ep:
            #         # print("New best! Average reward last 100 episodes: " + str(avg_reward_100_episode / 100))
            #         max_avg_reward_100ep = avg_reward_100_episode
            #
            #     if ct_finished_100ep > max_finished_100ep:
            #         max_finished_100ep = ct_finished_100ep
            #     avg_reward_100_episode = 0
            #     ct_finished_100ep = 0
            #
            # if percept.reward > 0:
            #     ct_goal += 1
            #     # print("GOAL!")
            #
            # if episode_count % 500 == 0 and episode_count > 0:
            #     print("Episode " + str(episode_count) + " Achieved goal in last 500ep: " + str(ct_goal) + " (" + str(
            #         (ct_goal / 500) * 100) + "%)")
            #     print("Best success rate over 100 episodes in last 500 episodes: " + str(max_finished_100ep) + "%")
            #
            #     max_finished_100ep = 0
            #     ct_goal = 0
            #     self.strategy.print()
            if self.strategy.exploration_rate == self.strategy.min_exploration_rate:
                print("\npolicy:\n")
                self.strategy.print()

            episode_count += 1


            '''
                def learn(self, n_episodes: int):
        stats = StatGenerator()
        episode_count = 0
        ct_goal = 0
        avg_reward_100_episode = 0
        max_avg_reward_100ep = 0
        ct_finished_100ep = 0
        max_finished_100ep = 0
        starttime = datetime.now()
        while episode_count <= n_episodes:
            current_state = self._environment.reset()
            percept = Percept(0, 0, 0, 0, False)
            ct_percept = 0
            tot_reward_episode = 0
            while not percept.done:
                ct_percept += 1
                action = self._strategy.next_action(current_state)
                next_state, reward, done, info = self._environment.step(action)
                percept = Percept(current_state, action, reward, next_state, done)
                self._strategy.learn(percept, episode_count)
                current_state = percept.next_state
                if percept.reward > 0:
                    tot_reward_episode += percept.reward
                    ct_finished_100ep += 1
                # if episode_count > 50000:
                #     print(self._environment.render())
                #     print("Episode: " + str(episode_count))
                #     self._strategy.print()
                #     time.sleep(2)
            avg_reward_100_episode += tot_reward_episode / ct_percept

            if episode_count > 0 and episode_count % 100 == 0:
                stats.add_episodes_success_rate(ct_finished_100ep)
                if avg_reward_100_episode > max_avg_reward_100ep:
                    # print("New best! Average reward last 100 episodes: " + str(avg_reward_100_episode / 100))
                    max_avg_reward_100ep = avg_reward_100_episode

                if ct_finished_100ep > max_finished_100ep:
                    max_finished_100ep = ct_finished_100ep
                avg_reward_100_episode = 0
                ct_finished_100ep = 0

            if percept.reward > 0:
                ct_goal += 1
                # print("GOAL!")

            if episode_count % 500 == 0 and episode_count > 0:
                print("Episode " + str(episode_count) + " Achieved goal in last 500ep: " + str(ct_goal) + " (" + str(
                    (ct_goal / 500) * 100) + "%)")
                print("Best success rate over 100 episodes in last 500 episodes: " + str(max_finished_100ep) + "%")

                print("Duurtijd: " + str(datetime.now() - starttime))
                starttime = datetime.now()
                max_finished_100ep = 0
                ct_goal = 0
                self._strategy.print()

            episode_count += 1
            '''
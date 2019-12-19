import random
import numpy as np

from be.kdg.rl.Policy import Policy
from be.kdg.rl.Agent import Agent
from be.kdg.rl.Environment import Environment
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Percept import Percept
from be.kdg.rl.QLearnStrategy import QLearnStrategy


def main():
    '''
    agent = Agent(0, environment)
    agent.learn(10001)
    '''
    np.set_printoptions(threshold=np.inf)

    environment = Environment()
    mdp = MDP(environment.observation_space_size, environment.action_space_size)
    policy = Policy(environment)
    #print(policy.pi)

    environment.render()
    print("\nstate: " + str(environment.state))
    print()

    qlearn = QLearnStrategy(learning_rate=0.8, discount_factor=0.95, min_exploration_rate=0.0001, max_exploration_rate=1,
                            exploration_decay_rate=0.01, mdp=mdp, policy=policy)

    print(qlearn.qsa)

    for x in range(1000):
        test = environment.step(random.randrange(0, 4, 1))
        mdp.update(test)
        print("========\nRENDER #" + str(x))
        environment.render()
        if test.final is True:
            environment.reset()

        print("\nstate: " + str(test.state))
        print("action: " + str(test.action))
        print("next state: " + str(test.next_state))
        print("reward: " + str(test.reward))
        print("final: " + str(test.final))

        qlearn.evaluate(test)
        print(qlearn.qsa)

        '''
        print("============\nNsa:")
        print(mdp.Nsa)
        print("\n============\nNtsa:")
        print(mdp.Ntsa)
        print("\n============\nPtsa:")
        print(mdp.Ptsa)
        '''

        '''
        print("\nReward:")
        print(mdp.Rtsa)
        '''

    #print(policy.pi)


if __name__ == "__main__":
    main()

import numpy as np

from be.kdg.rl.Agent import Agent
from be.kdg.rl.Environment import Environment
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Percept import Percept

if __name__ == "__main__":
    environment = Environment()
    agent = Agent(0, environment)
    agent.learn(10001)


    '''
    for x in range(50):
        test = environment.step(1)
        environment.render()
        print(test.s, test.a, test.r, test.st, test.final)

    mdp.update(Percept(0, 2, 1, 1, False))
    mdp.update(Percept(0, 2, 1, 4, False))
    mdp.update(Percept(0, 2, 1, 2, False))
    mdp.update(Percept(0, 2, 1, 2, False))
    mdp.update(Percept(0, 2, 1, 2, False))

    print(mdp.Ptsa[0])
    '''
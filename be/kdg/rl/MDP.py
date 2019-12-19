import numpy as np

from be.kdg.rl import Percept

'''
    - t = s' (=> observation_space_size)
    - s = s (=> observation_space_size)
    - a = a (=> action_space_size)
'''


class MDP:
    def __init__(self, observation_space_size, action_space_size):
        self.Rtsa = np.zeros((observation_space_size, observation_space_size, action_space_size))
        self.Nsa = np.zeros((observation_space_size, action_space_size), dtype=int)
        self.Ntsa = np.zeros((observation_space_size, observation_space_size, action_space_size), dtype=int)
        self.Ptsa = np.zeros((observation_space_size, observation_space_size, action_space_size), dtype=float)

    def update(self, percept: Percept):
        self.Rtsa[percept.next_state, percept.state, percept.action] = percept.reward
        self.Nsa[percept.state, percept.action] += 1
        self.Ntsa[percept.next_state, percept.state, percept.action] += 1

        for action in range(len(self.Ptsa[percept.next_state, percept.state])):
            if self.Nsa[percept.state, action] != 0:
                self.Ptsa[percept.next_state, percept.state, action] = \
                    self.Ntsa[percept.next_state, percept.state, action] / self.Nsa[percept.state, action]
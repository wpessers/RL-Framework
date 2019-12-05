import numpy

from be.kdg.rl import Percept


class MDP:
    def __init__(self, observation_space_size, action_space_size):
        self.Rtsa = numpy.zeros((observation_space_size, action_space_size, observation_space_size), dtype=int)
        self.Nsa = numpy.zeros((observation_space_size, action_space_size), dtype=int)
        self.Ntsa = numpy.zeros((observation_space_size, action_space_size, observation_space_size), dtype=int)
        self.Ptsa = numpy.zeros((observation_space_size, action_space_size, observation_space_size))

    def update(self, percept: Percept):
        # update R,Nsa, Ntsa, Ptsa with percept info
        self.update_R(percept.r, percept.t)
        self.update_Nsa(percept.s, percept.a)
        self.update_Ntsa(percept.s, percept.a, percept.t)
        self.update_Ptsa(percept.s, percept.a, percept.t)

    def update_R(self, s, a, t, r):
        self.Rtsa[s][a][t] = ((self.Rtsa[s][a][t] * self.Ntsa[s][a][t]) + r) / (self.Ntsa[s][a][t] + 1)

    def update_Nsa(self, s, a):
        self.Nsa[s][a] += 1

    def update_Ntsa(self, s, a, t):
        self.Ntsa[s][a][t] += 1

    def update_Ptsa(self, s, a, t):
        state_action_count = self.Nsa[s][a]
        state_action_new_states_counts = self.Ntsa[s][a]
        state_action_new_states_probabilities = self.Ptsa[s][a]

        for new_state_id in range(len(state_action_new_states_counts)):
            state_action_new_states_probabilities[new_state_id] = state_action_new_states_counts[
                                                                      new_state_id] / state_action_count

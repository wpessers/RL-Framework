import numpy

from be.kdg.rl import Percept


class MDP:
    def __init__(self, observation_space_size, action_space_size):
        self._Rtsa = numpy.zeros((observation_space_size, action_space_size, observation_space_size), dtype=int)
        self._Nsa = numpy.zeros((observation_space_size, action_space_size), dtype=int)
        self._Ntsa = numpy.zeros((observation_space_size, action_space_size, observation_space_size), dtype=int)
        self._Ptsa = numpy.zeros((observation_space_size, action_space_size, observation_space_size))

    def update(self, percept: Percept):
        # update R,Nsa, Ntsa, Ptsa with percept info
        self.update_Rtsa(percept.s, percept.a, percept.t, percept.r)
        self.update_Nsa(percept.s, percept.a)
        self.update_Ntsa(percept.s, percept.a, percept.t)
        self.update_Ptsa(percept.s, percept.a, percept.t)

    @property
    def Rtsa(self):
        return self._Rtsa

    @property
    def Nsa(self):
        return self._Nsa

    @property
    def Ntsa(self):
        return self._Ntsa

    @property
    def Ptsa(self):
        return self._Ptsa

    def update_Rtsa(self, s, a, t, r):
        self._Rtsa[s][a][t] = ((self.Rtsa[s][a][t] * self.Ntsa[s][a][t]) + r) / (self.Ntsa[s][a][t] + 1)

    def update_Nsa(self, s, a):
        self._Nsa[s][a] += 1

    def update_Ntsa(self, s, a, t):
        self._Ntsa[s][a][t] += 1

    def update_Ptsa(self, s, a, t):
        state_action_count = self._Nsa[s][a]
        state_action_new_states_counts = self._Ntsa[s][a]
        state_action_new_states_probabilities = self._Ptsa[s][a]

        for new_state_id in range(len(state_action_new_states_counts)):
            state_action_new_states_probabilities[new_state_id] = state_action_new_states_counts[
                                                                      new_state_id] / state_action_count

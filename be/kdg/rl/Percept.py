class Percept:
    def __init__(self, state, action, next_state, reward, final):
        self._state = state
        self._action = action
        self._next_state = next_state
        self._reward = reward
        self._final = final

    @property
    def state(self):
        return self._state

    @property
    def action(self):
        return self._action

    @property
    def next_state(self):
        return self._next_state

    @property
    def reward(self):
        return self._reward

    @property
    def final(self):
        return self._final

    def __repr__(self):
        return "state: " + str(self.state) + "\naction: " + str(self.action) + "\nreward: " + str(self.reward) \
               + "\nnext state: " + str(self.next_state) + "\nfinal: " + str(self.final)

class Episode:
    def __init__(self):
        self._percepts = []
        self._done = False

    @property
    def percepts(self):
        return self._percepts

    @property
    def done(self):
        return self._done

    def add_percept(self, percept):
        self._done = percept.final
        self._percepts.append(percept)
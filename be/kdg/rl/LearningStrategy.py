import abc

class LearningStrategy:
    def __init__(self, α, λ, ε, εmax, εmin):
        __metaclass__ = abc.ABCMeta
        self._α = α
        self._λ = λ
        self._ε = ε
        self._εmax = εmax
        self._εmin = εmin

    @property
    def α(self):
        return self._α

    @property
    def λ(self):
        return self._λ
    
    @property
    def ε(self):
        return self._ε

    @property
    def εmax(self):
        return self._εmax

    @property
    def εmin(self):
        return self._εmin

    def learn(self, percept):
        self.evaluate(percept)
        self.improve()

    @abc.abstractmethod
    def improve(self):
        return

    @abc.abstractmethod
    def evaluate(self, percept):
        return

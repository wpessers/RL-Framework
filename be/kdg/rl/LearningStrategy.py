import abc

class LearningStrategy:
    def __init__(self, α, γ, λ, ε, εmax, εmin):
        __metaclass__ = abc.ABCMeta
        self._α = α
        self._γ = γ
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
    def γ(self):
        return self._γ
    
    @property
    def ε(self):
        return self._ε

    @ε.setter
    def ε(self, value):
        self._ε = value

    @property
    def εmax(self):
        return self._εmax

    @property
    def εmin(self):
        return self._εmin

    def learn(self, percept, eposiode_count):
        self.evaluate(percept)
        self.improve(eposiode_count)

    @abc.abstractmethod
    def improve(self, episode_count):
        return

    @abc.abstractmethod
    def evaluate(self, percept):
        return

    @abc.abstractmethod
    def next_action(self, s):
        return

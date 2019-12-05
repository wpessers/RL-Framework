import numpy as np

from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.MDP import MDP


class QLearnStrategy(LearningStrategy):

    def __init__(self, α, γ, ε, εmax, εmin, mdp):
        super().__init__(α, γ, ε, εmax, εmin)
        self.mdp = mdp
        #TODO where does pi come from?
        self.π
        #TODO add shape
        self.qsa = np.zeros(mdp.Ptsa.shape)

    def evaluate(self, percept):
        self.mdp.update(percept)
        self.qsa = self.qsa + (self.α * ())

    def improve(self):
        #TODO do something
        pass

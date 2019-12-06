import math
import numpy as np

from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Policy import Policy


class QLearnStrategy(LearningStrategy):
    def __init__(self, α, γ, ε, εmax, εmin, mdp: MDP, policy: Policy):
        super().__init__(α, γ, ε, εmax, εmin)
        self.mdp = mdp
        self.q = np.zeros(mdp.Nsa.shape)
        self.policy = policy

    def evaluate(self, percept):
        s, a, t = percept.s, percept.a, percept.t
        self.mdp.update(percept)
        self.q[s][a] = \
            self.q[s][a] + (self.α * (self.mdp.Rtsa[s][a][t] + (self.γ * (np.amax(self.q[s]) - self.q[s][a]))))

    def improve(self):
        for s in range(self.mdp.observation_space_size):
            # TODO: randomness
            a_ster = np.argmax(self.q)

            for a in self.policy.π[s]:
                if (a == a_ster):
                    # TODO: "Verzameling van acties" -> verandert aantal (mogelijke) acties per state???
                    self.policy.π[s][a] = 1 - self.ε + (self.ε / self.mdp.action_space_size)
                elif (self.ε / self.mdp.action_space_size):
                    self.policy.π[s][a] = self.ε / self.mdp.action_space_size

            self.ε = self.εmin + ((self.εmax - self.εmin) * math.exp((-self.λ) * ))
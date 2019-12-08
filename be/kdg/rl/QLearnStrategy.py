import math
import numpy as np

from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Policy import Policy


class QLearnStrategy(LearningStrategy):
    def __init__(self, α, γ, λ, ε, εmax, εmin, mdp: MDP, policy: Policy):
        super().__init__(α, γ, λ, ε, εmax, εmin)
        self.mdp = mdp
        self.q = np.zeros(mdp.Nsa.shape)
        self.policy = policy

    def evaluate(self, percept):
        s, a, t = percept.s, percept.a, percept.t
        self.mdp.update(percept)
        # Gebruik van np.sum(Rtsa[s][a]) of zoals dit?
        self.q[s][a] = self.q[s][a] + self.α * (self.mdp.Rtsa[s][a][t] + self.γ * (np.max(self.q[t]) - self.q[s][a]))
        # TODO moeten we de v(s) updaten of niet? Wordt verder niet gebruikt in Q-learning

    def improve(self, episode_count):
        for s in range(self.mdp.observation_space_size):
            a_ster = self.random_argmax(self.q[s])
            for a in range(len(self.policy.π[s])):
                if a == a_ster:
                    # TODO: "Verzameling van acties" -> verandert aantal (mogelijke) acties per state???
                    self.policy.π[s][a] = 1 - self.ε + (self.ε / self.mdp.action_space_size)
                #TODO moet dit niet gewoon een else zijn?
                elif self.ε / self.mdp.action_space_size:
                    self.policy.π[s][a] = self.ε / self.mdp.action_space_size
            # TODO is e  de math.e constante?
            self.ε = self.εmin + (self.εmax - self.εmin) * math.e ** (-self.λ * episode_count)

    def next_action(self, s):
        # TODO change implementation of exploration
        if np.random.choice([0, 1], p=[self.ε, 1 - self.ε]) == 0:
            return np.random.choice(range(len(self.policy.π[s])))
        else:
            return self.random_argmax(self.policy.π[s])

    def random_argmax(self, array):
        return np.random.choice(np.flatnonzero(array == array.max()))

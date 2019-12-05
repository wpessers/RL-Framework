import numpy as np

from be.kdg.rl.LearningStrategy import LearningStrategy
from be.kdg.rl.MDP import MDP
from be.kdg.rl.Policy import Policy


class QLearnStrategy(LearningStrategy):

    def __init__(self, α, γ, ε, εmax, εmin, mdp: MDP, policy: Policy):
        super().__init__(α, γ, ε, εmax, εmin)
        self.mdp = mdp
        self.q = np.zeros(mdp.Nsa.shape)
        self.π = policy.π

    def evaluate(self, percept):
        s, a, t = percept.s, percept.a, percept.t
        self.mdp.update(percept)
        self.q[s][a] = \
            self.q[s][a] + (self.α * (self.mdp.Rtsa[s][a][t] + (self.γ * (np.amax(self.q[s]) - self.q[s][a]))))

        #TODO: v(s) waarde geven op basis van max q-waarde, volgens de slides bereken je dus IN q-learning een v-waarde
        # mbv de q-waarden die je zonet berekend hebt... d.w.z. dat we hier dus ook een nieuw attribuut voor moeten
        # hebben (?)... v(s) is een 1-dim tabel want is gewoon 1 value per mogelijke state... (lengte van 1-dim tabel is
        # dus environment.observation_space_sice ???) -> Moeten we dan dus ook de environment meegeven aan onze
        # constructor? Op den duur hebben we deze overal nodig precies?

    def improve(self):
        # TODO do something
        pass

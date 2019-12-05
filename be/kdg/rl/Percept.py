import numpy


class Percept:
    #TODO: Hier datatypes bijvoegen?
    def __init__(self, s, a, r, t, final):
        self._s = s
        self._a = a
        self._r = r
        self._t = t
        self._final = final

    @property
    def s(self):
        return self._s

    @property
    def a(self):
        return self._a

    @property
    def r(self):
        return self._r

    @property
    def t(self):
        return self._t

    @property
    def final(self):
        return self._final


    def __repr__(self):
        return "state: " + str(self.s) + "\naction: " + str(self.a) + "\nreward: " + str(self.r) + "\nnext state: " \
               + str(self.t) + "\nfinal: " + str(self.final)

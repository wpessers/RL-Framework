import numpy


class Percept:
    def __init__(self, s, a, r, t, final):
        self.s = s
        self.a = a
        self.r = r
        self.t = t
        self.final = final
import numpy


class Percept:
    def __init__(self, s, a, r, st, final):
        self.s = s
        self.a = a
        self.r = r
        self.st = st
        self.final = final

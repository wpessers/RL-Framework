import numpy


class Percept:
    def __init__(self, s, a, r, t, final):
        self.s = s
        self.a = a
        self.r = r
        self.t = t
        self.final = final

    def __repr__(self):
        return "state: " + str(self.s) + "\naction: " + str(self.a) + "\nreward: " + str(self.r) + "\nnext state: " \
               + str(self.t) + "\nfinal: " + str(self.final)

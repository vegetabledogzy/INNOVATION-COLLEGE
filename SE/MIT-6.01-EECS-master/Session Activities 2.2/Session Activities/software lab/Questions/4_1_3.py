from lib601.sig import Signal


class SummedSignal(Signal):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def sample(self, n):
        return self.s1.sample(n) + self.s2.sample(n)


class ScaledSignal(Signal):
    def __init__(self, s, c):
        self.s = s
        self.c = c

    def sample(self, n):
        return self.s.sample(n) * self.c

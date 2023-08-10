from lib601.sig import Signal

#  R(S).sample(n+1) = S.sample(n)


class R(Signal):
    def __init__(self, s):
        self.s = s

    def sample(self, n):
        return self.s.sample(n - 1)


class Rn(Signal):
    def __init__(self, s, k):
        self.s = s
        self.k = k

    def sample(self, n):
        return self.s.sample(n - self.k)

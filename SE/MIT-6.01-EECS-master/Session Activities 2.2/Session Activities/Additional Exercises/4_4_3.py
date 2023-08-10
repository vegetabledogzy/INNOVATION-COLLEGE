import lib601.sm as sm
import lib601.sig as sig


class TransduceSignal(sig.Signal):
    def __init__(self, s, m):
        self.s = s
        self.m = m

    def sample(self, n):
        if n < 0:
            return 0
        else:
            return self.m.step(self.s.sample(n))

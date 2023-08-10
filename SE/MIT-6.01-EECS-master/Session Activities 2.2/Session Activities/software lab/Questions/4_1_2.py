from lib601.sig import Signal


class StepSignal(Signal):
    def sample(self, n):
        if n < 0:
            return 0
        else:
            return 1

from lib601 import dist
from lib601 import sm


class StatePreprocessor(sm.SM):
    def __init__(self):
        pass
        

class StateEstimator(sm.SM):
    def __init__(self, model):
        self.model = model
        self.startState = model.startDistribution

    def getNextValues(self, state, inp):
        if inp == None:
            return (state, state)
        (o, i) = inp
        sGo = dist.bayesEvidence(state, self.model.observationDistribution, o)
        dSPrime = dist.totalProbability(sGo,
        self.model.transitionDistribution(i))
        return (dSPrime, dSPrime)
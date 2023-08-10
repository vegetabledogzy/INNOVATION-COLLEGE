# uncompyle6 version 3.8.0
# Python bytecode 2.6 (62161)
# Decompiled from: Python 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: c:\Users\robot\Desktop\newversion\codesandbox\lib601\seFast.py
# Compiled at: 2011-01-02 23:09:02
"""Just like se, but a more efficient implementation"""
import sm, ssm, dist, util

class StateEstimator(sm.SM):
    """
    A state machine that performs state estimation, based on an input
    stream of (input, output pairs) and a stochastic state-machine
    model.  The output at time t is a C{dist.DDist} object, representing
    the 'belief' distribution P(s | i_0, ... i_t, o_0, ..., o_t)
    """

    def __init__(self, model):
        """
        @param model: a C{ssm.StochasticStateMachine} object,
        specifying the transition and observation models
        """
        self.model = model
        self.startState = model.startDistribution

    def getNextValues(self, state, inp):
        """
        @param state: Distribution over states of the subject machine,
        represented as a C{dist.Dist} object
        @param inp: A pair C{(o, a)} of the input and output of the
        subject machine on this time step.  If this parameter is
        C{None}, then no update occurs and the state is returned,
        unchanged. 
        """
        if inp == None:
            return (state, state)
        else:
            (o, i) = inp
            total = 0
            afterObs = state.d.copy()
            for s in state.support():
                afterObs[s] *= self.model.observationDistribution(s).prob(o)
                total += afterObs[s]

            if total == 0:
                raise Exception('Observation ' + str(o) + ' has 0 probability in all possible states.')
            new = {}
            tDist = self.model.transitionDistribution(i)
            for s in state.support():
                tDistS = tDist(s)
                oldP = afterObs[s] / total
                for sPrime in tDistS.support():
                    dist.incrDictEntry(new, sPrime, tDistS.prob(sPrime) * oldP)

            dSPrime = dist.DDist(new)
            return (
             dSPrime, dSPrime)
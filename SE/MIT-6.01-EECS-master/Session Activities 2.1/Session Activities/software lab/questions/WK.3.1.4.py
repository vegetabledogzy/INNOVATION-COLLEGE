import lib601.sm as sm

# sm.PureFunction
# sm.Cascade, sm.Parallel, sm.Parallel2
class BA1(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        if inp != 0:
            newState = state * 1.02 + inp - 100
        else:
            newState = state * 1.02
        return newState, newState


class BA2(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        newState = state * 1.01 + inp
        return newState, newState


ba1 = BA1()
ba2 = BA2()
# maxAccount = sm.Cascade(sm.Parallel(ba1, ba2), sm.PureFunction(lambda x: x[1] if x[1] > x[0] else x[0]))
switchAccount = sm.Cascade(sm.Parallel2(ba1, ba2), sm.PureFunction(lambda x: x[1] if x[1] > x[0] else x[0]))

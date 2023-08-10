import lib601.sm as sm
import lib601.util as util


class LTISM(sm.SM):
    def __init__(self, dCoeffs, cCoeffs, previousInputs=[], previousOutputs=[]):
        self.cCoeffs = cCoeffs
        self.dCoeffs = dCoeffs
        # State is last input values and last k output values
        self.startState = (previousInputs, previousOutputs)

    def getNextValues(self, state, input):
        (inputs, outputs) = state
        inputs = [input] + inputs

        currentOutput = util.dotProd(outputs, self.cCoeffs) + \
                        util.dotProd(inputs, self.dCoeffs)
        return ((inputs[:-1], ([currentOutput] + outputs)[:-1]),
                currentOutput)

def dotProd(a, b):
    if len(a) == 0 or len(b) == 0: return 0
    if len(a) != len(b):
        print 'dotProd mismatch error ' + str(len(a)) + ' != ' + str(len(b))
    return sum([ai*bi for (ai, bi) in zip(a, b)])


print dotProd([1, 2, 3], [1, 2, 3])
m = LTISM([1, 2], [1], [3], [4])
o = m.transduce([1, 2, 3, 4, 5])
print o


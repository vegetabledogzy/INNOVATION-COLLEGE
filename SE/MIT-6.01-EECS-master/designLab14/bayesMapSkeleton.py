import lib601.dist as dist
import lib601.util as util
import lib601.colors as colors
import lib601.ssm as ssm
import lib601.seFast as seFast
import lib601.dynamicGridMap as dynamicGridMap


# Define the stochastic state-machine model for a given cell here.

# Observation model:  P(obs | state)


def oGivenS(s):
    # s == 'hit' or 'free'
    if s == 'occupied':
        return dist.DDist({'hit': 0.9, 'free': 0.1})
    else:
        return dist.DDist({'hit': 0.1, 'free': 0.9})
    pass


# Transition model: P(newState | s | a)
def uGivenAS(a):
    def x(s):
        if s == 'occupied':
            return dist.DDist({'occupied': 0.9, 'not': 0.1})
        else:
            return dist.DDist({'not': 0.9, 'occupied': 0.1})
    return x
    pass


cellSSM = ssm.StochasticSM(dist.DeltaDist('free'), uGivenAS, oGivenS)  # Your code here


class BayesGridMap(dynamicGridMap.DynamicGridMap):

    def squareColor(self, (xIndex, yIndex)):
        p = self.occProb((xIndex, yIndex))

        if self.robotCanOccupy((xIndex, yIndex)):
            return colors.probToMapColor(p, colors.greenHue)
        elif self.occupied((xIndex, yIndex)):
            return 'black'
        else:
            return 'red'

    def occProb(self, (xIndex, yIndex)):
        # if self.grid[xIndex][yIndex] == 'hit':
        #     return 0.8
        # else:
        #     return 0.2
        return self.grid[xIndex][yIndex].state.prob('occupied')

    def makeStartingGrid(self):
        array = util.make2DArrayFill(self.xN, self.yN, lambda x, y: seFast.StateEstimator(cellSSM))
        # array = []
        for x in range(self.xN):
            for y in range(self.yN):
                array[x][y].start()

        return array

    def setCell(self, (xIndex, yIndex)):
        self.grid[xIndex][yIndex].step(('hit', None))
        self.drawSquare((xIndex, yIndex))

    def clearCell(self, (xIndex, yIndex)):
        print 'xIndex:', xIndex, 'yIndex:', yIndex
        self.grid[xIndex][yIndex].step(('free', None))
        self.drawSquare((xIndex, yIndex))

    def occupied(self, (xIndex, yIndex)):
        if self.occProb((xIndex, yIndex)) > 0.5:
            return True
        else:
            return False


mostlyHits = [('hit', None), ('hit', None), ('hit', None), ('free', None)]
mostlyFree = [('free', None), ('free', None), ('free', None), ('hit', None)]


def testCellDynamics(cellSSM, input):
    se = seFast.StateEstimator(cellSSM)
    return se.transduce(input)


# testCellDynamics(cellSSM, mostlyHits)

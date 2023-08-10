from lib601 import dist
from lib601.coloredHall import makeObservationModel

possibleColors = ['black', 'white', 'red', 'green', 'blue']
standardHallway = ['white', 'white', 'green', 'white', 'white']


def whiteEqGreenObsDist(actualColor):
    if actualColor == 'white' or actualColor == 'green':
        return dist.DDist({'white': 0.5, 'green': 0.5})
    else:
        return dist.DDist({actualColor: 1.0})


print "whiteEqGreenObsDist('white'):"
print whiteEqGreenObsDist('white')
print "whiteEqGreenObsDist('green'):"
print whiteEqGreenObsDist('green')
print '\n'

def whiteVsGreenObsDist(actualColor):
    if actualColor == 'white':
        return dist.DDist({'green': 1.0})
    elif actualColor == 'green':
        return dist.DDist({'white': 1.0})
    else:
        return dist.DDist({actualColor: 1.0})


print "whiteVsGreenObsDist('white'):"
print whiteVsGreenObsDist('white')
print "whiteVsGreenObsDist('green'):"
print whiteVsGreenObsDist('green')
print '\n'


def noisyObs(actualColor):
    dict = {actualColor: 0.8}
    possibleColors_length = len(possibleColors)
    for color in possibleColors:
        if color != actualColor:
            dict[color] = 0.2 / (possibleColors_length - 1)
    return dist.DDist(dict)


print "noisyObs('white')"
print noisyObs('white')


noisyObsModel = makeObservationModel(standardHallway, noisyObs)

from lib601 import dist
from lib601 import util
from lib601.coloredHall import makeTransitionModel

standardHallway = ['white', 'white', 'green', 'white', 'white']


def incrDictEntry(d, k, v):
    if d.has_key(k):
        d[k] += v
    else:
        d[k] = v


def ringDynamics(loc, act, hallwayLength):
    if loc + act > (hallwayLength - 1):
        step = loc + act - hallwayLength
    elif loc + act < 0:
        step = loc + act + hallwayLength
    else:
        step = loc + act
    return step


print "ringDynamics"
print ringDynamics(1, 2, 3)
print ringDynamics(0, -2, 3)
print ringDynamics(0, -1, 3)
print "= = = = = = = = = = = = = = = "


def leftSlipTrans(nominalLoc, hallwayLength):
    dict = {}
    if nominalLoc == 0:
        dict = {nominalLoc: 1}
    else:
        dict = {(nominalLoc - 1): 0.1, nominalLoc: 0.9}
    return dist.DDist(dict)


print "leftSlipTrans"
print leftSlipTrans(0, 5)
print leftSlipTrans(1, 5)
print "= = = = = = = = = = = = = = = "


def noisyTrans(nominalLoc, hallwayLength):
    if nominalLoc == 0:
        dict = {nominalLoc: 0.9, nominalLoc + 1: 0.1}
    elif nominalLoc == hallwayLength - 1:
        dict = {nominalLoc: 0.9, nominalLoc - 1: 0.1}
    else:
        dict = {nominalLoc - 1: 0.1, nominalLoc: 0.8, nominalLoc + 1: 0.1}
    return dist.DDist(dict)


def standardDynamics(loc, act, hallwayLength):
    return util.clip(loc + act, 0, hallwayLength-1)


print "noisyTrans"
print noisyTrans(4,5)
print noisyTrans(3,5)
print noisyTrans(2,5)
print noisyTrans(1,5)
print noisyTrans(0,5)
print "= = = = = = = = = = = = = = = "

noisyTransModel = makeTransitionModel(standardDynamics, noisyTrans, 5)


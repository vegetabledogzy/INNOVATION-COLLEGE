import lib601.sf as sf
import lib601.optimize as optimize
import operator


def delayPlusPropModel(k1, k2):
    T = 0.1
    V = 0.1
    
    # Controller:  your code here
    controller = sf.FeedforwardAdd(sf.Gain(k1), sf.Cascade(sf.R(), sf.Gain(k2)))
    # The plant is like the one for the proportional controller.  Use
    # your definition from last week.

    plant1 = sf.Cascade(sf.Cascade(sf.R(), sf.Gain(T)), sf.FeedbackAdd(sf.Gain(1), sf.R()))

    plant2 = sf.Cascade(sf.Cascade(sf.Gain(V*T), sf.R()), sf.FeedbackAdd(sf.Gain(1), sf.R()))

    # Combine the three parts
    sys = sf.FeedbackSubtract(sf.Cascade(controller, sf.Cascade(plant1, plant2)))
    return sys

# You might want to define, and then use this function to find a good
# value for k2.

# Given k1, return the value of k2 for which the system converges most
# quickly, within the range k2Min, k2Max.  Should call optimize.optOverLine.


def f1(k1):
    # return x * x - x
    # return sf.FeedforwardAdd(delayPlusPropModel(k1, x), sf.Cascade(sf.R(), delayPlusPropModel(k1, x)))
    return lambda k2: abs(delayPlusPropModel(k1, k2).dominantPole())


def bestk2(k1, k2Min, k2Max, numSteps):
    # return optimize.optOverLine(poly.Polynomial[1,2,-1,1], k2Min, k2Max, numSteps)
    return optimize.optOverLine(f1(k1), k2Min, k2Max, numSteps)


def anglePlusPropModel(k3, k4):
    T = 0.1
    V = 0.1

    controller = sf.Gain(k3)

    # plant 1 is as before
    plant1 = sf.Cascade(sf.Cascade(sf.R(), sf.Gain(T)), sf.FeedbackAdd(sf.Gain(1), sf.R()))

    # plant2 is as before
    plant2 = sf.Cascade(sf.Cascade(sf.Gain(V*T), sf.R()), sf.FeedbackAdd(sf.Gain(1), sf.R()))

    # The complete system
    # sf.FeedbackSubtract(controller, sf.Gain(k4))

    sys = sf.FeedbackSubtract(sf.Cascade(sf.Cascade(sf.Gain(k3), sf.FeedbackSubtract(plant1,sf.Gain(k4))), plant2))

    return sys


# Given k3, return the value of k4 for which the system converges most
# quickly, within the range k4Min, k4Max.  Should call optimize.optOverLine.

def f2(k3):
    # return x * x - x
    return lambda k4: abs(anglePlusPropModel(k3, k4).dominantPole())


def bestk4(k3, k4Min, k4Max, numSteps):
    return optimize.optOverLine(f2(k3), k4Min, k4Max, numSteps)


# k2 can't bigger than k1
print 'bestk2'
print '= = = = = = = = = = = = = = = = = = = = = = = = = = = = '
print bestk2(10, -10, 10, 200)
print bestk2(30, -30, 30, 600)
print bestk2(100, -100, 100, 2000)
print bestk2(300, -300, 300, 3000)
print '= = = = = = = = = = = = = = = = = = = = = = = = = = = = '
print 'bestk4'
print bestk4(1, -10, 10, 200)
print bestk4(3, -10, 10, 200)
print bestk4(10, -10, 10, 200)
print bestk4(30, -30, 30, 600)

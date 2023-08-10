import lib601.sig  as sig # Signal
import lib601.ts as ts  # TransducedSignal
import lib601.sm as sm  # SM

######################################################################
##  Make a state machine model using primitives and combinators
######################################################################

# class Gain(SM):
# def __init__(self, k):
# self.k = k
# def getNextValues(self, state, inp):
# return (state, self.k*inp)


def plant(T, initD):
    return sm.Cascade(sm.Cascade(sm.R(0), sm.Gain(-T)), sm.FeedbackAdd(sm.Wire(), sm.R(initD)))


def controller(k):
    return sm.Gain(k)


def sensor(initD):
    return sm.R(initD)


def wallFinderSystem(T, initD, k):
    return sm.FeedbackSubtract(sm.Cascade(controller(k), plant(T, initD)), sensor(initD))


# Plots the sequence of distances when the robot starts at distance
# initD from the wall, and desires to be at distance 0.7 m.  Time step
# is 0.1 s.  Parameter k is the gain;  end specifies how many steps to
# plot. 

# first the car's distance to the wall
initD = 1.5


def plotD(k, end=50):
  d = ts.TransducedSignal(sig.ConstantSignal(0.7),
                          wallFinderSystem(0.1, initD, k))
  d.plot(0, end, newWindow='Gain '+str(k))


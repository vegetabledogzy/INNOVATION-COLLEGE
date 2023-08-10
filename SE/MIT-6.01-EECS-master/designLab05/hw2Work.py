# -*- coding=utf-8 -*-
import lib601.sf as sf
import lib601.sig as sig
import lib601.ts as ts

# 6.01 HomeWork 2 Skeleton File

# Constants relating to some properties of the motor
k_m = 250
k_b = 0.48
k_s = 1
r_m = 4.5


def controllerAndSensorModel(k_c):
    return sf.Cascade(sf.Gain(k_s), sf.Gain(k_c))


# pass #your code here

def integrator(T):
    # input Ωh  output Θh
    return sf.Cascade(sf.Cascade(sf.R(), sf.Gain(T)), sf.FeedbackAdd(sf.Gain(1), sf.R()))


# pass #your code here

def motorModel(T):
    # input Vc   output Ωh
    return sf.Gain((k_m * T) / (k_b * k_m * T + r_m))


def plantModel(T):
    return sf.Cascade(motorModel(T), integrator(T))


def lightTrackerModel(T, k_c):
    return sf.FeedbackSubtract(sf.Cascade(controllerAndSensorModel(k_c), plantModel(T)))


def plotOutput(sfModel):
    """Plot the output of the given SF, with a unit-step signal as input"""
    smModel = sfModel.differenceEquation().stateMachine()
    outSig = ts.TransducedSignal(sig.StepSignal(), smModel)
    outSig.plot()

  
plotOutput(lightTrackerModel(0.02, 300.0))

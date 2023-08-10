import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

import os
labPath = os.getcwd()
from sys import path
if not labPath in path:
    path.append(labPath)
    print 'setting labPath to', labPath

from boundaryFollower import boundaryFollowerClass


# class MySMClass(sm.SM):
#
#     def getNextValues(self, state, inp):
#         [neck, left, right] = inp.analogInputs[0:3]
#         sonars = inp.sonars
#         gain = 1
#         if 4.8 < neck < 5.2:
#             return state, io.Action(fvel=1, rvel=0)
#         else:
#             return (state, io.Action(fvel=0, rvel=gain * (neck - 5)))


class MySMClass(sm.SM):

    def getNextValues(self, state, inp):
        # [neck, left, right] = inp.analogInputs[0:3]
        neck = inp.analogInputs[3]
        sonars = inp.sonars
        gain = 1
        if 4.8 < neck < 5.2:
            if inp.sonars[3] >= 0.65 or inp.sonars[4] >= 0.65:
                return state, io.Action(fvel=0.1, rvel=0)
            if 0.35 < inp.sonars[3] < 0.65 or 0.35 < inp.sonars[4] < 0.65:
                return state, io.Action(fvel=0, rvel=0)
            else:
                return state, io.Action(fvel=-0.1, rvel=0)
            # mySM = boundaryFollowerClass()
        else:
            return (state, io.Action(fvel=0, rvel=gain * (neck - 5)))
        # return state, io.Action(fvel=0.1, rvel=gain * (inp.analogInputs[1]-inp.analogInputs[2]))


mySM1 = MySMClass()
class Stop(sm.SM):
    def getNextValues(self, state, inp):
        return (state,io.Action(fvel=0,rvel=0))
# def condition(inp):
#     if inp.analogInputs[3] < 1.5:
#         return True
#     else:
#         return False
# mySM = sm.Switch()
# mySM = sm.Switch(lambda inp: inp.analogInputs[3] < 1.5, boundaryFollowerClass, mySM1)
mySM1.name = 'brainSM'
    

######################################################################
###
###          Brain methods
###
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)

def brainStart():
    robot.behavior = mySM
    robot.behavior.start(robot.gfx.tasks())
    robot.data = []

def step():
    inp = io.SensorInput().analogInputs
    inp = io.SensorInput()
    robot.behavior.step(inp).execute()

def brainStop():
    pass

def shutdown():
    pass

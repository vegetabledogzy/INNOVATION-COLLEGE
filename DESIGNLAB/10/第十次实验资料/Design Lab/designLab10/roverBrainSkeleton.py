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

#from boundaryFollower import boundaryFollowerClass
        
class MySMClass(sm.SM):
    def getNextValues(self, state, inp):
        v1=inp.analogInputs[2]
        v2=inp.analogInputs[3]
        
         pass

mySM = MySMClass()
mySM.name = 'brainSM'
    

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
    inp = io.SensorInput()
    robot.behavior.step(inp).execute()

def brainStop():
    pass

def shutdown():
    pass

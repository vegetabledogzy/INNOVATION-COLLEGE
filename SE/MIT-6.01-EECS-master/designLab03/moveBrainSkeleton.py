# -*- coding: UTF-8 -*-
import os
labPath = os.getcwd()
from sys import path
if not labPath in path:
    path.append(labPath)
print 'setting labPath to', labPath

import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io
import lib601.io as lib601_io
# Remember to change the import in dynamicMoveToPointSkeleton in order
# to use it from inside soar
import dynamicMoveToPointSkeleton
reload(dynamicMoveToPointSkeleton)

import ffSkeleton
reload(ffSkeleton)

from secretMessage import secret

# Set to True for verbose output on every step
verbose = True

# Rotated square points
squarePoints = [util.Point(0.5, 0.5), util.Point(0.0, 1.0),
                util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]

# Put your answer to step 1 here
# mySM = None


class Stop(sm.SM):
    def getNextValues(self, state, inp):
        return (state,io.Action(fvel=0,rvel=0))


goalGenerator = ffSkeleton.FollowFigure(squarePoints)
# goalGenerator = ffSkeleton.FollowFigure(secret)
temp_m = sm.Cascade(sm.Parallel(goalGenerator, sm.Wire()), dynamicMoveToPointSkeleton.DynamicMoveToPoint())
mySM = sm.Switch(lambda x: min(x.sonars[0:8]) < 0.5, Stop(), temp_m)



######################################################################
###
###          Brain methods
###
######################################################################
#
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail = True)
    robot.behavior = mySM

def brainStart():
    robot.behavior.start(traceTasks=robot.gfx.tasks(),
                         verbose=verbose)

def step():
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())

def brainStop():
    pass

def shutdown():
    pass

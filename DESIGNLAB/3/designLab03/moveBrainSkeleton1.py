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

# Remember to change the import in dynamicMoveToPointSkeleton in order
# to use it from inside soar
import dynamicMoveToPointSkeleton
reload(dynamicMoveToPointSkeleton)

import ffSkeleton
reload(ffSkeleton)

from secretMessage import secret

# Set to True for verbose output on every step
verbose = False

# Rotated square points
squarePoints = [util.Point(0.5, 0.5), util.Point(0.0, 1.0),
                util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]


# Put your answer to step 1 here
class DynamicMoveToPoint(sm.SM):#state machine 2
    startState=None
    def getNextValues(self, state, inp):
        k=0.2
        r=0.1
        angle_error=0.01
        position_error=0.05
        print(inp)
        p1 = inp.odometry()  # the instance variables of io.SensorInput
        o1 = util.Point(1.0, 0.5)#point ¿‡
        print('o1', o1)
        inp = (o1, inp)
        print(inp)
        print(p1)
        p0=o1   #refers to the goal point
        distance = p0.distance(p1.point())
        angle1 = p0.angleTo(p1.point())#angle between current position and goal point
        go_speed = k*distance
        rot_speed = r*(angle1-angle1)
        angle2=util.fixAnglePlusMinusPi(p1.theta)#angle of the car's head
        print('iooutput:', io.SensorInput(cheat = True).odometry.point())

        # Replace this definition
        print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        assert isinstance(inp,tuple), 'inp should be a tuple'
        assert len(inp) == 2, 'inp should be of length 2'
        assert isinstance(inp[0],util.Point), 'inp[0] should be a Point'

        if util.nearAngle(angle1, angle2, angle_error):
            return (state, io.Action(fvel=go_speed ,rvel=rot_speed))
        else:
            return (state, io.Action(fvel=go_speed ,rvel=rot_speed))
poseList = [util.Pose(0, 0, 0),
            util.Pose(0, 0, math.pi / 2),
            util.Pose(0, 0, math.atan2(0.5, 1)),
            util.Pose(1.0001, 0.499999, 0)]

mySM=DynamicMoveToPoint()


######################################################################
###
###          Brain methods
###
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail = True)
    robot.behavior = mySM

def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks(),
                         verbose = verbose)

def step():
    robot.behavior.step(io.SensorInput()).execute()
    print('iooutput:',io.SensorInput().odometry.point())
    io.done(robot.behavior.isDone())

def brainStop():
    pass

def shutdown():
    pass

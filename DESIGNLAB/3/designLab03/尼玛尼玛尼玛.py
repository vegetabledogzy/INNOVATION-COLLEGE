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
squarePoints = [util.Point(0.5, 0.5)]
temp = 'False'

# Put your answer to step 1 here
class DynamicMoveToPoint(sm.SM):#state machine 2
    startState='False'
    def getNextValues(self, state, inp):
        global temp
        global squarePoints
        temp = state
        print('dier',state)
        (goal,inpPose)=inp
        inp=inpPose.odometry
        k=0.2
        r=0.1
        angle_error=0.01 #½Ç¶ÈÎó²î
        position_error=0.05 #Î»ÖÃÎó²î
        #print(inp)
        p1 = inp  # the instance variables of io.SensorInput(x,y,thea)
        o1 = goal
        print('o1', o1)
        inp = (o1, inp)
        #print(inp)
        #print(p1)
        p0=o1   #refers to the goal point
        distance = p0.distance(p1.point())
        # angle1 = p0.angleTo(p1.point())#angle between current position and goal point
        angle1 = p1.point().angleTo(p0)
        go_speed = k*distance
        # angle2=util.fixAnglePlusMinusPi(p1.theta) # angle of the car's head  ÓëxÖáµÄ¼Ð½Ç
        angle2 = p1.theta
        rot_speed = r*(angle1-angle2)
        print('iooutput:', io.SensorInput(cheat = True).odometry.point())
        # Replace this definition
        print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        assert isinstance(inp,tuple), 'inp should be a tuple'
        assert len(inp) == 2, 'inp should be of length 2'
        assert isinstance(inp[0],util.Point), 'inp[0] should be a Point'
        if state == 'False':
            if not (util.nearAngle(angle1, angle2, angle_error)) :
                heading = util.fixAnglePlusMinusPi(angle1 - angle2)
                return ('False', io.Action(fvel=0, rvel=heading * 2.0))
            if distance > position_error:
                return ('False', io.Action(fvel=go_speed, rvel=0))
            if util.nearAngle(angle1, angle2, angle_error) and abs(distance - position_error) < 0.002:
                return ('True', io.Action())
        if state == 'True':
            if squarePoints=='':
                state='over'
            else:
                return ('False',io.Action())
    def done(self,state):
        print(state)
        if state == 'over':
            return True  
class GoalGenerator(sm.SM):
    def __init__(self):
        self.startState='False'
    def getNextValues(self,state,inp):
        global temp
        global squarePoints
        state = temp
        print('diyi',state)
        if state=='True':
            if len(squarePoints)>1:
                del squarePoints[0]
                return '',(squarePoints[0],inp)
            else:
                return '',(squarePoints[0],inp)
        if state =='False':
            return '',(squarePoints[0],inp)
     
def statemachine():
    return sm.Cascade(GoalGenerator(),DynamicMoveToPoint())

mySM=statemachine()


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

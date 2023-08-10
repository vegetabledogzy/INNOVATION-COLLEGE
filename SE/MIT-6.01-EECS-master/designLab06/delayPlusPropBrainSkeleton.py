# coding=utf-8
import math
import lib601.sm as sm
from soar.io import io
import lib601.gfx as gfx
import lib601.util as util
import lib601.sonarDist as sonarDist

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.4
forwardVelocity = 0.1


# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        v = sonarDist.getDistanceRight(inp.sonars)
        print 'Dist from robot center to wall on right', v
        return (state, v)


# inp is the distance to the right
class WallFollower(sm.SM):
    T = 0.1
    k1 = 10
    k2 = -9.9
    startState = 0

    # save the last time do(inp)
    def getNextValues(self, state, inp):
        print 'rightDist', inp
        lastState = state
        rvel = self.k1 * (desiredRight - inp) + self.k2 * lastState
        # 把当前 (desiredRight - inp) 当state 传回去 当下一个lastState
        return (desiredRight - inp), io.Action(forwardVelocity, rvel=rvel)



    # output is an instance of the class io.Action
################
# Your code here
################


sensorMachine = Sensor()
sensorMachine.name = 'sensor'
mySM = sm.Cascade(sensorMachine, WallFollower())

######################################################################
#
#            Running the robot
#
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    robot.gfx.addStaticPlotSMProbe(y=('rightDistance', 'sensor',
                                      'output', lambda x:x))
    robot.behavior = mySM
    robot.behavior.start(traceTasks=robot.gfx.tasks())


def step():
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())


def brainStop():
    pass

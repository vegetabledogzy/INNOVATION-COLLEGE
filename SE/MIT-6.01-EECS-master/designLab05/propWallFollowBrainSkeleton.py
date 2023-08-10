import math
import lib601.sm as sm
from soar.io import io
import lib601.gfx as gfx
import lib601.util as util
import lib601.sonarDist as sonarDist

reload(gfx)

import designLab05Work
reload(designLab05Work)
######################################################################
#
#            Brain SM
#
######################################################################

# Template brain with a place for you to write the proportional controller

desiredRight = 0.5
forwardVelocity = 0.2


# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        return state, sonarDist.getDistanceRight(inp.sonars)

# getDistanceRightAndAngle(sonarValues)

# inp is the distance to the right

# implements a proportional controller.


class WallFollower(sm.SM):
    k = - 30
    T = 0.1

    def getNextValues(self, state, inp):
        print 'rightDist', inp
        print 'angle', self.k * (inp - desiredRight) * self.T
        if inp < 0.5:
            return state, io.Action(fvel=forwardVelocity, rvel=self.k * (inp - desiredRight))
        else:
            if -0.1 < self.k * (inp - desiredRight) * self.T < 0.1:
                return state, io.Action(fvel=forwardVelocity, rvel=0)
            else:
                return state, io.Action(fvel=forwardVelocity, rvel=self.k * (inp - desiredRight))


mySM = sm.Cascade(Sensor(), WallFollower())


######################################################################
#
#            Running the robot
#
######################################################################

def plotDist():
    func = lambda: sonarDist.getDistanceRight(io.SensorInput().sonars)
    robot.gfx.addStaticPlotFunction(y=('d_o', func))


def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    plotDist()
    # designLab05Work.plotD(-20)
    robot.behavior = mySM
    robot.behavior.start(traceTasks=robot.gfx.tasks())


def step():
    robot.behavior.step(io.SensorInput()).execute()


def brainStart():
    # Do this to be sure that the plots are cleared whenever you restart
    robot.gfx.clearPlotData()


def brainStop():
    pass


def shutdown():
    pass

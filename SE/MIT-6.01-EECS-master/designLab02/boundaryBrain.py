# -*- coding: UTF-8 -*-
import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io


class MySMClass(sm.SM):

    def getNextValues(self, state, inp):

        if inp.sonars[3] >= 0.65 or inp.sonars[4] >= 0.65:
            return state, io.Action(fvel=0.1, rvel=0)

        elif 0.35 < inp.sonars[3] < 0.65 or 0.35 < inp.sonars[4] < 0.65:
            return state, io.Action(fvel=0, rvel=0)
        else:
            return state, io.Action(fvel=-0.1, rvel=0)

        # if 0.3 < inp.sonars[3] < 0.5 or 0.3 < inp.sonars[2] < 0.5 or 0.3 < inp.sonars[1] < 0.5:
        #     return state, io.Action(fvel=0.1, rvel=-0.1)
        #
        # if 0.3 < inp.sonars[4] < 0.5 or 0.3 < inp.sonars[5] < 0.5 or 0.3 < inp.sonars[6] < 0.5:
        #     return state, io.Action(fvel=0.1, rvel=0.1)
        #
        # if inp.sonars[0] < 0.2 or inp.sonars[7] < 0.2:
        #     return state, io.Action(fvel=0, rvel=0.1)
        #
        # if inp.sonars[3] >= 0.5 and inp.sonars[4] >= 0.5:
        #     return state, io.Action(fvel=0.2, rvel=0.0)
        # else:
        #     if inp.sonars[0] >= inp.sonars[7]:
        #         return state, io.Action(fvel=0, rvel=0.2)
        #     else:
        #         return state, io.Action(fvel=0, rvel=-0.2)

        #
        # if state == 'start':
        #     next_state = 'Forward'
        #     return next_state, io.Action(fvel=0.3, rvel=0)
        #
        # if state == 'Forward':
        #     if inp.sonars[3] >= 0.5 and inp.sonars[4] >= 0.5:
        #         next_state = 'Forward'
        #         return next_state, io.Action(fvel=0.3, rvel=0)
        #     else:
        #         if inp.sonars[0] >= inp.sonars[7]:
        #             next_state = 'turnLeft'
        #         else:
        #             next_state = 'turnRight'
        #         return next_state, io.Action(fvel=0.0, rvel=0.0)
        #
        # if state == 'turnLeft':
        #     if 0.3 < inp.sonars[3] < 0.5:
        #         next_state = 'turnLeft'
        #         return next_state, io.Action(fvel=0.3, rvel=0.3)
        #     elif inp.sonars[3] > 0.5:
        #         if 0.3 < inp.sonars[7] < 0.5:
        #             next_state = 'turnRight'
        #             return next_state, io.Action(fvel=0, rvel=0.2)
        #         elif inp.sonars[7] > 0.5:
        #             next_state = 'turnLeft'
        #             return next_state, io.Action(fvel=0.1, rvel=0.3)
        #         else:
        #             next_state = 'turnLeft'
        #             return next_state, io.Action(fvel=0.1, rvel=0.3)
        #
        # if state == 'turnRight':
        #     if 0.3 < inp.sonars[4] < 0.5:
        #         next_state = 'turnRight'
        #         return next_state, io.Action(fvel=0.3, rvel=-0.3)
        #     elif inp.sonars[4] > 0.5:
        #         if inp.sonars[0] > 0.5:
        #             next_state = 'turnRight'
        #             return next_state, io.Action(fvel=0.1, rvel=0.1)
        #         elif 0.5 > inp.sonars[0] > 0.3:
        #             next_state = 'turnRight'
        #             return next_state, io.Action(fvel=0.1, rvel=0.0)
        #         else:
        #             next_state = 'turnRight'
        #             return next_state, io.Action(fvel=-0.1, rvel=-0.1)


# mySM = MySMClass()
# mySM.name = 'brainSM'


######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar' + str(sonarNum),
                                        lambda:
                                        io.SensorInput().sonars[sonarNum]))


# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True,  # slime trails
                                  sonarMonitor=True)  # sonar monitor widget

    # set robot's behavior
    robot.behavior = mySM


# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks=robot.gfx.tasks())


# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    print('sonars-3', inp.sonars[3])
    print('sonars-6', inp.sonars[6])
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())


# called when the stop button is pushed
def brainStop():
    pass


# called when brain or world is reloaded (before setup)
def shutdown():
    pass


mySM = MySMClass()
# mySM.getNextValues('start', io.SensorInput())
mySM.name = 'brainSM'

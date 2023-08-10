# -*- coding: UTF-8 -*-
import lib601.sm as sm
import lib601.util as util
import math
import lib601.gfx as gfx
# Use this line for running in idle
# import lib601.io as io
# Use this line for testing in soar
from soar.io import io

points = [util.Point(0.5, 0.5), util.Point(0.0, 1.0),
          util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]


# class DynamicMoveToPoint(sm.SM):
#     def getNextValues(self, state, inp):
#         # Replace this definition
#
#         goalPoint = util.Point(1.0, 0.5)
#         print('goalPoint', goalPoint)
#
#         # 得到当前的x, y
#         currentPoint = inp.odometry.point()
#         print('currentPoint', currentPoint)
#
#         # 得到两个点的距离
#         distance = goalPoint.distance(currentPoint)
#         print('distance', distance)
#
#         angle = goalPoint.angleTo(currentPoint)
#         print('angle', angle)
#
#         if state == 'stop':
#             return (state, io.Action(fvel=0, rvel=0))
#
#         if -2.0 < angle < -1.48:
#             if 0.1 < distance < 1.2:
#                 return (state, io.Action(fvel=0.05, rvel=0.2))
#             elif distance <= 0.1:
#                 state = 'stop'
#                 return (state, io.Action(fvel=0, rvel=0))
#             else:
#                 return (state, io.Action(fvel=0.2, rvel=0))
#
#         else:
#             if distance <= 0.1:
#                 state = 'stop'
#                 return (state, io.Action(fvel=0, rvel=0))
#             else:
#                 return (state, io.Action(fvel=0.2, rvel=0))

        # inp = (goalPoint, inp)
        #
        # print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        # assert isinstance(inp, tuple), 'inp should be a tuple'
        # assert len(inp) == 2, 'inp should be of length 2'
        # assert isinstance(inp[0], util.Point), 'inp[0] should be a Point'

class DynamicMoveToPoint(sm.SM):
    def __init__(self):
        self.rotationGain = 1.0
        # 距离
        self.distEps = 0.02
        # 角度
        self.angleEps = 0.05

    def getNextValues(self, state, inp):
        goalPoint, sensors = inp
        # 获得小车当前的坐标
        robotCurrentPoint = sensors.odometry.point()
        # 获取小车当前的角度
        robotCurrentTheta = sensors.odometry.theta
        # 目标角度 target
        goalTheta = robotCurrentPoint.angleTo(goalPoint)
        # 检查角度 有一个角度的误差范围之内 util.nearAngle
        if util.nearAngle(robotCurrentTheta, goalTheta, self.angleEps):
            r = robotCurrentPoint.distance(goalPoint)
            # 检查两点之间的距离
            if r > self.distEps:
                return False, io.Action(fvel=0.08, rvel=0)
            else:
                return True, io.Action(fvel=0, rvel=0)
        else:
            # 不在同一直线上 就需要原地调整位置
            target = util.fixAnglePlusMinusPi(goalTheta - robotCurrentTheta)
            return False, io.Action(fvel=0, rvel=target * self.rotationGain)

        # inp = (goalPoint, inp)
        # print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        # assert isinstance(inp, tuple), 'inp should be a tuple'
        # assert len(inp) == 2, 'inp should be of length 2'
        # assert isinstance(inp[0], util.Point), 'inp[0] should be a Point'


def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar' + str(sonarNum),
                                        lambda:
                                        io.SensorInput().sonars[sonarNum]))


# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True,  # slime trails
                                  sonarMonitor=False)  # sonar monitor widget

    # set robot's behavior
    robot.behavior = mySM


# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks=robot.gfx.tasks())


# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())


# called when the stop button is pushed
def brainStop():
    pass


# called when brain or world is reloaded (before setup)
def shutdown():
    pass


mySM = DynamicMoveToPoint()


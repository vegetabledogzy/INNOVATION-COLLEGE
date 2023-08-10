# -*- coding: UTF-8 -*-
import lib601.sm as sm
import lib601.util as util


class FollowFigure(sm.SM):
    distEps = 0.02
    index = 0

    def __init__(self, points):
        self.points = points
        self.startState = None

    def getNextValues(self, state, inp):
        nextPoint = state
        robotCurrentPoint = inp.odometry.point()
        if nextPoint is None:
            nextPoint = self.points[0]
        # 判断小车是否靠近目标点
        if robotCurrentPoint.isNear(nextPoint, self.distEps):
            index = search(self.points, nextPoint)
            self.index = index
            if index == len(self.points) - 1:
                nextPoint = self.points[-1]
            else:
                # if self.points[index] == nextPoint:
                nextPoint = self.points[index + 1]

            # index = findPoint(self.points, nextPoint)
            # nextPoint = self.points[index]
            # if index != len(self.points) - 1:
            #     nextPoint = self.points[index + 1]
            # else:
            #     nextPoint = self.points[-1]
        print('NextPoint', nextPoint, self.index)
        return nextPoint, nextPoint


def search(points, point):
    index = 0
    while index < len(points):
        if points[index] == point:
            return index
        index += 1
    return -1

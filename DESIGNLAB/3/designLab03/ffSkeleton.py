import lib601.sm as sm
import os
import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io
import dynamicMoveToPointSkeleton

class FollowFigure(sm.SM):
    def __init__(self):
        self.startState='False'
        self.squarePoints = [util.Point(0.5, 0.5), util.Point(0.0, 1.0),
                util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]
    def getNextValues(self,state,inp):
        state = dynamicMoveToPointSkeleton.DynamicMoveToPoint().temp
        print('diyi',state)
        if state=='True':
            if len(squarePoints)>1:
                del self.squarePoints[0]
                return '',(self.squarePoints[0],inp)
            else:
                return '',(self.squarePoints[0],inp)
        if state =='False':
            return '',(self.squarePoints[0],inp)

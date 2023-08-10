import lib601.sm as sm

# from dynamicMoveToPointSkeleton import DynamicMoveToPoint
# reload(DynamicMoveToPoint)
squarePoints = [util.Point(0.5, 0.5), util.Point(0.0, 1.0),
                util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]
temp = 'False'
import dynamicMoveToPointSkeleton
class FollowFigure(sm.SM):
    def __init__(self):
        self.startState = 'False'
    def getNextValues(self, state, inp):
        global temp
        global squarePoints
        state = dynamicMoveToPointSkeleton.temp
        # print('diyi',state)
        if state == 'True':
            if len(squarePoints) > 1:
                del squarePoints[0]
                return '', (squarePoints[0], inp)
            else:
                return '', (squarePoints[0], inp)
        if state == 'False':
            return '', (squarePoints[0], inp)

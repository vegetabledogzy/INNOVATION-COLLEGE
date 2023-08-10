import lib601.sm as sm

from secretMessage import secret
squarePoints = secret
import dynamicMoveToPointSkeleton
class FollowFigure(sm.SM):
    def __init__(self):
        self.startState = 'False'
    def getNextValues(self, state, inp):
        global temp
        global squarePoints
        print('secret',secret)
        print('ssssss', squarePoints)
        state = dynamicMoveToPointSkeleton.temp
        # print('diyi',state)
        if state == 'True':
            if len(squarePoints) > 1:
                del squarePoints[0]
                return ('', (squarePoints[0], inp))
            else:
                return '', (squarePoints[0], inp)
        if state == 'False':
            return '', (squarePoints[0], inp)

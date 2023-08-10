import lib601.sm as sm
import lib601.util as util
import lib601.io as io
from secretMessage import secret
#squarePoints = secret
#squarePoints = [util.Point(1.0, 0.5), util.Point(0.0, 1.0),
               #util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]
import dynamicMoveToPointSkeleton
class FollowFigure(sm.SM):
    def __init__(self,new_list):
        self.startState = 'None'
        self.new_list = new_list
        self.index=0
    def getNextValues(self, state, inp):
        distance = self.new_list[self.index].distance(inp.odometry.point())
        if distance >0.05:
            state = 'False'
        else:
            state ='True'      
        if state == 'True':
            if self.index<len(self.new_list)-1:
                self.index+=1
                return ('False', (self.new_list[self.index],inp))
            else:
                return 'True', (self.new_list[self.index],inp)
        if state == 'False':
            return 'False', (self.new_list[self.index],inp)

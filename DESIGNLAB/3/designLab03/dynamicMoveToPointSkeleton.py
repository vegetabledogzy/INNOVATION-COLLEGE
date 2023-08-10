import lib601.sm as sm
import lib601.util as util
import math

# Use this line for running in idle
import lib601.io as io
# Use this line for testing in soar
from soar.io import io

class DynamicMoveToPoint(sm.SM):
    def __init__(self):
        self.temp='False'
        self.startState='Flase'
    def getNextValues(self, state, inp):
        # Replace this definition
        self.temp = state
        print('dier',state)
        (goal,inpPose)=inp
        inp=inpPose.odometry
        k=0.2
        r=0.1
        angle_error=0.01 
        position_error=0.05 
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
        # angle2=util.fixAnglePlusMinusPi(p1.theta) 
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
                return ('False',io.Action())
    

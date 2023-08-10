import lib601.sm as sm
import lib601.util as util
import math

# Use this line for running in idle
import lib601.io as io
# Use this line for testing in soar
from soar.io import io
squarePoints = [util.Point(0.5, 0.5), util.Point(0.0, 1.0),
                 util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]
temp = 'False'
class DynamicMoveToPoint(sm.SM):
    startState='False'
    def getNextValues(self, state, inp):
        global temp
        global squarePoints
        temp = state
        # print('dier',state)
        (goal,inpPose)=inp
        inp=inpPose.odometry
        k=1.5
        r = 2.0
        angle_error=0.001
        position_error=0.005
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
        # angle2=util.fixAnglePlusMinusPi(p1.theta) # angle of the car's head
        angle2 = p1.theta
        heading = util.fixAnglePlusMinusPi(angle1 - angle2)
        rot_speed = r*heading
        print('iooutput:', io.SensorInput(cheat = True).odometry.point())
        # Replace this definition
        print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        assert isinstance(inp,tuple), 'inp should be a tuple'
        assert len(inp) == 2, 'inp should be of length 2'
        assert isinstance(inp[0],util.Point), 'inp[0] should be a Point'
        if state == 'False':
            if min(io.SensorInput().sonars) < 0.3:
                return ('False',io.Action())
            if not (util.nearAngle(angle1, angle2, angle_error)) :
                return ('False', io.Action(fvel=0, rvel=rot_speed))
            if distance > position_error:
                return ('False', io.Action(fvel=go_speed, rvel=0))
            if util.nearAngle(angle1, angle2, angle_error) and abs(distance - position_error) < 0.002:
                return ('True', io.Action())
        if state == 'True':
            if squarePoints=='':
                return ('over',io.Action())
            else:
                return ('False',io.Action())

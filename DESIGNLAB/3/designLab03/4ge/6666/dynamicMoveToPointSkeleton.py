import lib601.sm as sm
import lib601.util as util
import math

# Use this line for running in idle
import lib601.io as io
# Use this line for testing in soar
from soar.io import io
class DynamicMoveToPoint(sm.SM):
    def getNextValues(self, state, inp):
        (goal,Sensorinput)=inp
        p1=Sensorinput.odometry #Pose
        k=1.5
        r = 2.0
        angle_error=0.001
        position_error=0.005
        inp = (goal, p1)
        p0=goal   #po is goal
        distance = p0.distance(p1.point())
        angle1 = p1.point().angleTo(p0)
        angle2 = p1.theta
        heading = util.fixAnglePlusMinusPi(angle1 - angle2)
        go_speed = k*distance
        rot_speed = r*heading
        if distance > position_error:
            if not (util.nearAngle(angle1, angle2, angle_error)) :
                return (state,io.Action(fvel=0, rvel=rot_speed))
            else:
                return (state,io.Action(fvel=go_speed, rvel=0))
        if distance < position_error:
            return (state, io.Action())
        #print('iooutput:', io.SensorInput(cheat = True).odometry.point())
        # Replace this definition
        print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        assert isinstance(inp,tuple), 'inp should be a tuple'
        assert len(inp) == 2, 'inp should be of length 2'
        assert isinstance(inp[0],util.Point), 'inp[0] should be a Point'
       

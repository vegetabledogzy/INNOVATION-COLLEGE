import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    def __init__(self):
        self.StartState= None
        self.a=5
        self.b=5
    def getNextValues(self, state, inp):   
        if state == 'go':
            if inp.sonars[3]+inp.sonars[4]+inp.sonars[2]+inp.sonars[5]<0.9 or inp.sonars[2]<0.2 or inp.sonars[5]<0.2: #判断是否在墙角
                state = 'back'        
            else:
                if inp.sonars[0]<=0.3 or inp.sonars[1]<=0.33:
                    state = 'right'
                if (abs(inp.sonars[7]-self.a)>0.5 and self.a<0.5):
                    state = 'keepright'
                if (abs(inp.sonars[0]-self.b)>0.5 and self.b<0.5):
                    state = 'keepleft'
                if inp.sonars[6]<=0.33 or inp.sonars[7]<=0.3:
                    state = 'left'
                if inp.sonars[3]<=0.5 or inp.sonars[4]<=0.5:
                    if inp.sonars[0]+inp.sonars[1]<=inp.sonars[6]+inp.sonars[7]:
                        state = 'right'
                    else:
                        state = 'left'
        print (state)        
        self.a=inp.sonars[7]
        self.b=inp.sonars[0]
        if state == 'go':
            return ('go', io.Action(fvel=0.3, rvel=0))
        elif state == 'right':
            return ('go',io.Action(fvel=0.05, rvel=-0.3))
        elif state == 'left':
            return ('go',io.Action(fvel=0.05, rvel=0.3))
        elif state =='keepright':
            if self.a+inp.sonars[6]<1.2:
                return ('go',io.Action(fvel=0.2, rvel=-0.3))
            else:
                return ('keepright',io.Action(fvel=0.2, rvel=-0.3))
        elif state =='keepleft':
            if self.b<0.8:
                return ('go',io.Action(fvel=0.2, rvel=0.3))
            else:
                return ('keepleft',io.Action(fvel=0.2, rvel=0.3))
        else:
            if  inp.sonars[2]<0.2 and inp.sonars[5]>0.2:
                return ('go',io.Action(fvel=-0.1, rvel=-0.3))
            elif  inp.sonars[5]<0.2 and inp.sonars[2]>0.2:
                return ('go',io.Action(fvel=-0.1, rvel=0.3))
            else:
                return ('go',io.Action(fvel=-0.1, rvel=0))
        

mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=True) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    print inp.sonars[0] , inp.sonars[3] ,inp.sonars[7]     #打印三号声呐距离障碍物的距离,最远是1.5，大于1.5则一直显示5  
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass

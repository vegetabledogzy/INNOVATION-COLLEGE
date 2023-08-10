import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    def getNextValues(self, state, inp):
        near=0
        if (inp.sonars[2]<0.5 or inp.sonars[3]<0.5 or inp.sonars[4]<0.5 or inp.sonars[5]<0.5):
                near=1
        elif (inp.sonars[3]+inp.sonars[4])/2>0.5 and inp.sonars[0]>0.5 and inp.sonars[7]>0.5:
                near=0
        if((inp.sonars[2]<0.25 and inp.sonars[5]<0.25)or(inp.sonars[3]<0.25 and inp.sonars[4]<0.25)or inp.sonars[2]+inp.sonars[3]+inp.sonars[4]+inp.sonars[6]<0.75 ):
            return (state,io.Action(fvel = -0.3,rvel = 0.4))
        if near ==1:
            if inp.sonars[0]+inp.sonars[1]+inp.sonars[2]+inp.sonars[3]<inp.sonars[4]+inp.sonars[5]+inp.sonars[6]+inp.sonars[7]:#ÔÚ×óÇ½±ß
                if inp.sonars[0]<0.35:
                    if(inp.sonars[1]<0.3):
                      return (state,io.Action(fvel = -0.08,rvel = -0.4))   
                    return (state,io.Action(fvel = 0.08,rvel = -0.4)) 
                elif inp.sonars[0]>=0.35:
                    return (state,io.Action(fvel = 0.08,rvel = -0.3))
            if inp.sonars[0]+inp.sonars[1]+inp.sonars[2]+inp.sonars[3]>inp.sonars[4]+inp.sonars[5]+inp.sonars[6]+inp.sonars[7]:
                if inp.sonars[7]<0.35:
                    if(inp.sonars[6]<0.3):
                      return (state,io.Action(fvel = -0.08,rvel = 0.4))   
                    return (state,io.Action(fvel = 0.08,rvel = 0.4)) 
                elif inp.sonars[7]>=0.35:
                    return (state,io.Action(fvel = 0.08,rvel = 0.3))
        elif near==0:#²»ÔÚÇ½±ß
            return (state,io.Action(fvel = 0.1,rvel = 0))

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
    ipt = [1,1,1,1,1,1,1,1]
    inp = io.SensorInput()
    #print(inp.sonars[0])
    for i in range(8):
        ipt[i]=inp.sonars[i]
    print(ipt)
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass

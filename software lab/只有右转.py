import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    def getNextValues(self, state, inp):
        near=0
        # if (( inp.sonars[0]<0.4 or inp.sonars[2]<0.5 or inp.sonars[3]<0.5 or inp.sonars[4]<0.5 )):
        if  inp.sonars[0]<0.4 or min(inp.sonars[2:5])< 0.5:  
            near=1
        elif max(inp.sonars[0:7]) < 0.3:
            near = 3
        elif (inp.sonars[3]+inp.sonars[4])/2>0.7 and inp.sonars[0]>0.5 and inp.sonars[7]>0.5:
        #else:
            near=0
        if near ==1:#æ‡¿Î«ΩΩ¸
            if inp.sonars[0]<0.3:
                return (state,io.Action(fvel = -0.08,rvel = -0.2))
            elif inp.sonars[0]>0.3:
                return (state,io.Action(fvel = 0,rvel = -0.2))
            #elif min(inp.soars[4:7]) < 0.3:
                #return (state,io.Action(fvel = -0.08,rvel = 0.2))
        elif near==0:#¿Î«Ω‘∂
            return (state,io.Action(fvel = 0.3 ,rvel = 0))
        elif near == 3:#«ΩΩ«
            return (state,io.Action(fvel = -0.2 ,rvel = 0))

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
                                  sonarMonitor=False) # sonar monitor widget
    
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

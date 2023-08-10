from lib601 import util

sonarMax = 1.5
numObservations = 10
sonarPose0 = util.Pose(0.08, 0.134, 1.570796)


def wall((x1, y1), (x2, y2)):
    return util.LineSeg(util.Point(x1, y1), util.Point(x2, y2))


wallSegs = [wall((0, 2), (8, 2)),
            wall((1, 1.25), (1.5, 1.25)),
            wall((2, 1.75), (2.8, 1.75))]

robotPoses = [util.Pose(0.5, 0.5, 0), util.Pose(1.25, 0.5, 0),
              util.Pose(1.75, 1.0, 0), util.Pose(2.5, 1.0, 0)]


def discreteSonar(sonarReading):
    if sonarReading < sonarMax:
        return int(sonarReading / (sonarMax / numObservations))
    else:
        return numObservations - 1


print "discreteSonar"
print discreteSonar(0.1)
print discreteSonar(0.3)
print discreteSonar(0.55)
print "= = = = = = = = = = = = = "

from lib601 import util
import math


def sonarHit(distance, sonarPose, robotPose):
    (x_S, y_S, theta_S) = sonarPose
    (x_R, y_R, theta_R) = robotPose
    x_Sonar = distance
    y_Sonar = 0
    x_Robot = x_S + math.cos(theta_S)*x_Sonar - math.sin(theta_S)*y_Sonar
    y_Robot = y_S + math.sin(theta_S)*x_Sonar + math.cos(theta_S)*y_Sonar
    x = x_R + math.cos(theta_R)*x_Robot - math.sin(theta_R)*y_Robot
    y = y_R + math.sin(theta_R) * x_Robot + math.cos(theta_R) * y_Robot
    return util.Point(x, y)


def ideaReadings(wallSegs, robotPoses):
    sonarReadings = []
    for pose in robotPoses:
        # lineStart = sonarHit(0, sonarPose0, pose)
        # lineEnd = sonarHit(sonarMax, sonarPose0, pose)
        lineStart = sonarHit(0, (sonarPose0.x, sonarPose0.y, sonarPose0.theta), (pose.x, pose.y, pose.theta))
        lineEnd = sonarHit(sonarMax, (sonarPose0.x, sonarPose0.y, sonarPose0.theta), (pose.x, pose.y, pose.theta))
        line = util.LineSeg(lineStart, lineEnd)
        sonarReading = []
        for seg in wallSegs:
            interPoint = line.intersection(seg)
            # false
            if interPoint is False:
                sonarReading.append(sonarMax)
            else:
                sonarReading.append(pose.point().distance(interPoint))
        sonarReadings.append(min(sonarReading))
    return sonarReadings


test = ideaReadings(wallSegs, robotPoses)
print test
for i in test:
    print discreteSonar(i)

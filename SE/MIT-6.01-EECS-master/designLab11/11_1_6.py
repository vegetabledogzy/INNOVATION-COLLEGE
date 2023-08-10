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


print sonarHit(3, (1, 1, 0), (0, 0, 0))

print sonarHit(3, (1, 1, math.pi/2), (0, 0, 0))

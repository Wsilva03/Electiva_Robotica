import numpy
import math
from sympy import *
from roboticstoolbox import *
from spatialmath.base import *

def plot_1(l1,l2,theta1,theta2):
    q1 = theta1
    q2 = theta2
    R = []
    R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
    Robot = DHRobot(R, name='Wall-e')
    Robot.plot([q1, q2], backend='pyplot', block=False, limits=[-19, 19, -19, 19, -19, 19])  # Plot en 3D
    MTH = Robot.fkine([q1, q2])
    return MTH
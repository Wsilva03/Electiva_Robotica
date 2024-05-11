import numpy
import numpy as np
import math
from sympy import *
from roboticstoolbox import *
from spatialmath.base import *

def inversa_2R(l1, l2, Px, Py):
    b = math.sqrt(Px**2+Py**2)
    # Theta 2
    cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
    try:
        sen_theta2 = math.sqrt(1-(cos_theta2)**2)  # (-)codo arriba
    except ValueError:
        sen_theta2 = math.sqrt(1+(cos_theta2)**2)  # (+)codo abajo

    theta2 = math.atan2(sen_theta2, cos_theta2)
    # Theta 1
    alpha = math.atan2(Py, Px)
    phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
    theta1 = alpha - phi
    return abs(theta1), abs(theta2)
# Ruta 1 (espacio articulacional (MoveJ) - interpolando ángulos)
import math
import numpy
from sympy import *
from InverseKinematics3R import *
from ForwardKinematics3R import *
import matplotlib.pyplot as plt
import time

l1 = 10
l2 = 10
l3 = 10

# Cinemática inversa
# Punto 1
P1x = 2.456
P1y = 0.31
P1z = 26.933

[theta1_P1, theta2_P1, theta3_P1] = InverseKinematics3R(l1,l2,l3,P1x,P1y,P1z)

# Punto 2
P2x = -9.804
P2y = 11.851
P2z = 20.723

[theta1_P2, theta2_P2, theta3_P2] = InverseKinematics3R(l1,l2,l3,P2x,P2y,P2z)

n = 10
x = numpy.arange(1,n+1,1)

theta1_P1toP2 = numpy.linspace(theta1_P1, theta1_P2, n)
theta2_P1toP2 = numpy.linspace(theta2_P1, theta2_P2, n)
theta3_P1toP2 = numpy.linspace(theta3_P1, theta3_P2, n)

d = numpy.zeros((3,n))

fig1 = plt.figure().add_subplot(projection='3d')
fig1.set_xlabel('X')
fig1.set_ylabel('Y')
fig1.set_zlabel('Z')
fig1.set_xlim(-30, 30)
fig1.set_ylim(-30, 30)
fig1.set_zlim(-30, 30)

for i in range (0,n):
    MTH = ForwardKinematics3R(l1,l2,l3,theta1_P1toP2[i],theta2_P1toP2[i],theta3_P1toP2[i])
    d[:,i] =  MTH.t    
    fig1.plot(d[0,i],d[1,i],d[2,i],'.b')

plt.show(block=True)

fig2 = plt.figure(2)
ax1, ax2 = fig2.subplots(2,1)
ax1.plot(x, numpy.rad2deg(theta1_P1toP2),'tab:red')
ax1.set_title('Espacio articulacional')
ax1.set_xlabel('Waypoint')
ax1.set_ylabel('Ángulo (°)')
plt.grid()
ax1.plot(x, numpy.rad2deg(theta2_P1toP2),'tab:green')
ax1.plot(x, numpy.rad2deg(theta3_P1toP2),'tab:blue')
ax1.legend(['q1','q2','q3'],loc="upper left")

ax2.plot(x, d[0,:],'tab:red')
ax2.set_title('Espacio operacional')
ax2.set_xlabel('Waypoint')
ax2.set_ylabel('Posición (m)')
plt.grid()
ax2.plot(x, d[1,:],'tab:green')
ax2.plot(x, d[2,:],'tab:blue')
ax2.legend(['X','Y','Z'],loc="upper left")
plt.show(block=True)
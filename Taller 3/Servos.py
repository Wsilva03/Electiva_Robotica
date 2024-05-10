import RPi.GPIO as GPIO
import numpy as np

def Servos(theta1,theta2):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    servo1 = GPIO.PWM(19, 50)  # GPIO 19 para Servo 1 con frecuencia de 50Hz
    servo2 = GPIO.PWM(16, 50)
    ang1 = np.rad2deg(theta1)
    print (ang1)
    ang2 = np.rad2deg(theta2)
    print (ang2)
    print ("Servo inicio")
    if 0 <= abs(int(ang1)) <=180 and 0 <= abs(int(ang2)) <= 180:
        duty1 = ang1 / 18.0 + 2.5  # Calculate duty cycle for angle 1
        duty2 = ang2 / 18.0 + 2.5  # Calculate duty cycle for angle 2
        servo1.start(duty1)
        servo2.start(duty2)
        # Mueve los servos y apágalos inmediatamente
    else:
        print("Limite exedido")
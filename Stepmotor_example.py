# import required libs
import time
from motors.motor import *

 # Initialize (run once)----------------------------------------------------
my_motor = Motor("Stepper") #create an object from type Motor with name "Stepper"

'''Example change the default used output pins (GPIO BCM numbering)
my_motor.used_pins = [20, 21, 22, 23]'''

my_motor.init() #initialize GPIO ports, in this case the default ports
my_motor.helo() #test to see if the motor object is alive!
my_motor.debug = True

'''Example change default sequence (less power per steps)
my_motor.f_seq = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]
my_motor.b_sec = [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]]
            '''
while True:
    for step in range(20):
        my_motor.move(1, False)
    time.sleep(2)
    for step in range(20):
        my_motor.move(1, True)
    

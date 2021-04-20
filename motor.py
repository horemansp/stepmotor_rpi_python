#####################################################################
#   module to initialize and steer motors                            #
#####################################################################
# import dependencies
import time
import RPi.GPIO as GPIO

# run once
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


# define classes
class Motor():
    used_pins = [22, 23, 24, 25]
    f_seq = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 0, 0, 0]]
    b_sec = [
            [1, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
    loop_steps = 8
    loop_wait = 0.002
    debug=False

    def __init__(self, name):
        self.name = name

    def init(self):
        for pin in self.used_pins:
            GPIO.setup(pin, GPIO.OUT)

    def move(self, steps, direction):
        if direction:
            sequence_list = self.f_seq
        else:
            sequence_list = self.b_sec
        for step in range(steps):
            for loop in range(self.loop_steps):
                for sequences in range(len(sequence_list)):
                    for pins in range(len(self.used_pins)):
                        if sequence_list[sequences][pins] == 1:
                            GPIO.output(self.used_pins[pins], True)
                        else:
                            GPIO.output(self.used_pins[pins], False)
                    time.sleep(self.loop_wait)
            if self.debug: print("step, direction",direction)

    def hello(self):
        print("Hello from",self.name,"motor!")

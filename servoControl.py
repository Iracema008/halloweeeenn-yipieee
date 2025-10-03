from gpiozero import Servo
from time import sleep
from smbus2 import SMBus, ic2_msg



def servoControl():
    """ function to control the servo movement
        tba pwm once i get servo
    """
    servo = Servo(16, min_pulse_width=500/1_000_000, max_pulse_width=2500/1_000_000)

def acct():
    """ """
    pass
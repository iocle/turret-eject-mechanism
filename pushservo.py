from machine import Pin, PWM
import utime
from machine import Pin
import time

MID = 1500000
MIN = 1000000
MAX = 2000000


led = Pin(25,Pin.OUT)
pwm = PWM(Pin(15))
button = Pin(14, Pin.IN, Pin.PULL_UP)

pwm.freq(50)
pwm.duty_ns(MIN)

while True:
    if button.value() == 0:
        pwm.duty_ns(MID)
    else:
        pwm.duty_ns(MIN)
    time.sleep(0.1)
    

    
#Yay, working 10/2/2024


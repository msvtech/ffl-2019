#!/usr/bin/env micropython

from ev3dev2.motor import MediumMotor, OUTPUT_D, SpeedPercent
from ev3dev2.led import Leds
import time

top_motor = MediumMotor(OUTPUT_D)
leds = Leds()

leds.all_off()

for i in range(0, 100, 2):
    top_motor.on(SpeedPercent(i))
    leds.set_color('LEFT', (1 - i/100.0, i/100.0))
    leds.set_color('RIGHT', (1 - i/100.0, i/100.0))
    time.sleep(.1)

top_motor.on(SpeedPercent(100))
time.sleep(1)

for i in range(100, 0, -2):
    top_motor.on(SpeedPercent(i))
    leds.set_color('LEFT', (1 - i/100.0, i/100.0))
    leds.set_color('RIGHT', (1 - i/100.0, i/100.0))
    time.sleep(.1)

m.off()

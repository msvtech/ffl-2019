#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
# from ev3dev2.sensor.lego import GyroSensor, ColorSensor, TouchSensor
from ev3dev2.led import Leds
import time
# from math import cos, radians, degrees
# import os
# import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
# front_motor = MediumMotor(OUTPUT_C)
top_motor = MediumMotor(OUTPUT_D)
# gs = GyroSensor()
leds = Leds()

ratio_degrees_to_inches = 360 / 8.44
rotate90 = 137 / 90.0

# Main Program

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

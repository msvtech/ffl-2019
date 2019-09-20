#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C # , OUTPUT_D
# from ev3dev2.sensor.lego import GyroSensor, ColorSensor, TouchSensor
# from ev3dev2.led import Leds
import time
# from math import cos, radians, degrees
# import os
# import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
front_motor = MediumMotor(OUTPUT_C)
# top_motor = MediumMotor(OUTPUT_D)
# gs = GyroSensor()
# leds = Leds()

ratio_degrees_to_inches = 360 / 8.44
rotate90 = 137 / 90.0

# Main Program

# front_motor.on_for_degrees(speed=SpeedPercent(5), degrees=3)

# for i in range(6):
#     front_motor.on_for_degrees(speed=SpeedPercent(1), degrees=15)
#     time.sleep(0.5)

front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=90)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(10), degrees=90)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=45)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=45)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(10), degrees=90)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=-2)


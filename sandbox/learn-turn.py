#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B # , OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor, ColorSensor # , TouchSensor
from ev3dev2.led import Leds
import time
# from math import cos, radians, degrees
# import os
# import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
# front_motor = MediumMotor(OUTPUT_C)
# top_motor = MediumMotor(OUTPUT_D)
gs = GyroSensor()
leds = Leds()

ratio_degrees_to_inches = 360 / 8.44
rotate90 = 137 / 90.0

# Main Program

rotate90 = 188
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

# Right turn 90 degree
tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(-100), rotate90)
time.sleep(0.5)

# Left turn 360 degree
tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate90 * 4)
time.sleep(0.5)

# Right turn 180 degree then 90 degree
tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate90 * 2)
time.sleep(0.5)
tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate90 * 1)

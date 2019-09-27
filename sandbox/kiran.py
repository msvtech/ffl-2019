#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B # , OUTPUT_C, OUTPUT_D
# from ev3dev2.sensor.lego import GyroSensor, ColorSensor, TouchSensor
# from ev3dev2.led import Leds
import time
# from math import cos, radians, degrees
# import os
# import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
# front_motor = MediumMotor(OUTPUT_C)
# top_motor = MediumMotor(OUTPUT_D)
# gs = GyroSensor()
# leds = Leds()

ratio_degrees_to_inches = 360 / 8.44
rotate90 = 137 / 90.0

# Main Program


# Drive Backwards
tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(-30), ratio_degrees_to_inches * 55, brake=True)


# Turn left 45 degrees0
tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 250)


# Drive backwards
tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(-30), ratio_degrees_to_inches 30 * , brake=True)

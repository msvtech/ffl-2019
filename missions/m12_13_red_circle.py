#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C # , OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor #,  GyroSensor, ColorSensor
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
ts = TouchSensor()

ratio_degrees_to_inches = 360 / 8.44
rotate = 135.0 / 90.0

def m12_RedCircle():
    # ####################################
    # Mission 12 - Red Circle
    # ####################################

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 13, brake=True)
    time.sleep(1)
    tank_drive.on_for_degrees(SpeedPercent(10), SpeedPercent(-10), rotate * 22)
    time.sleep(1)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 16.5, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-100), SpeedPercent(-100), ratio_degrees_to_inches * 50, brake=True)
    time.sleep(1)

    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(-100), rotate * 45)

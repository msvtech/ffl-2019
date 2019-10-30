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

def m01_ElevatedPlaces():
    # ####################################
    # Mission 1 - Elevated Places
    # ####################################

    tank_drive.on_for_degrees(SpeedPercent(45), SpeedPercent(45), ratio_degrees_to_inches * 47, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate * 74, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(-50), ratio_degrees_to_inches * 39.5, brake=True)

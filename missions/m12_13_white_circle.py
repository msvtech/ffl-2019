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

def m12_WhiteCircle():
    # ####################################
    # Mission 12 - White Circle
    # ####################################

    tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(-40), rotate * 52, brake=True)

    # Drive Forward
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 17.6, brake=True)

    time.sleep(1)

    # Drive Backwards
    tank_drive.on_for_degrees(SpeedPercent(-40), SpeedPercent(-40), ratio_degrees_to_inches * 18, brake=True)

    # Turn Right 45 degrees
    tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate * 45, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-100), SpeedPercent(-100), ratio_degrees_to_inches * 17, brake=True)

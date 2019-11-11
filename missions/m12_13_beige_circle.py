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

def m12_BeigeCircle():
    # ####################################
    # Mission 12 - Beige Circle
    # ####################################

    tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(40), ratio_degrees_to_inches * 27, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(10), SpeedPercent(-10), rotate * 51, brake=True)
    time.sleep(0.25)
    tank_drive.on_for_degrees(SpeedPercent(45), SpeedPercent(45), ratio_degrees_to_inches * 22.3, brake=True)
    time.sleep(0.25)
    tank_drive.on_for_degrees(SpeedPercent(-100), SpeedPercent(-100), ratio_degrees_to_inches * 18, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(-100), rotate * -70, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-100), SpeedPercent(-100), ratio_degrees_to_inches * 50, brake=True)

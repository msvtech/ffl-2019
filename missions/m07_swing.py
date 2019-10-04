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

def m07_Swing():
    # ####################################
    # Mission 7 - Swing
    # ####################################

    tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 58)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 40, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate90 * 18)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 11, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * -50, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate90 * 20)


    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -10000, brake=True)

    # Drive forward
    # tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 16, brake=True)

    #! Turn left 45 degrees
    # tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 45)

    # front_motor.on_for_degrees(SpeedPercent(100), 5 * 360)

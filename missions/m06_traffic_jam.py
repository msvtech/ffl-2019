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

def m06_TrafficJam():
    # ####################################
    # Mission 6 - Traffic Jam
    # ####################################

    # front_motor.on_for_degrees(speed=SpeedPercent(-50), degrees=10, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 12, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 45)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 3, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(-30), rotate * 15)

    front_motor.on(speed=SpeedPercent(-5))
    time.sleep(0.25)
    tank_drive.on_for_degrees(SpeedPercent(75), SpeedPercent(75), ratio_degrees_to_inches * 18, brake=True)
    time.sleep(0.25)
    front_motor.on(speed=SpeedPercent(75))
    time.sleep(0.75)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 8, brake=True)
    front_motor.off()
    #tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 4, brake=True)
    time.sleep(0.5)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -50, brake=True)

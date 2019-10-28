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

def m02_Crane_Part1():
    # ####################################
    # Mission 02 - Crane Part 1
    # ####################################

    # Drive to Crane
    #front_motor.on_for_degrees(speed=SpeedPercent(50), degrees=90, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 11, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(-30), rotate * 80)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 22, brake=True)

    # Drop attachment to lower crane lever
    #front_motor.on_for_degrees(speed=SpeedPercent(-10), degrees=45, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(10), SpeedPercent(10), ratio_degrees_to_inches * -5, brake=True)

    # Drive backwards to get in position for Traffic Jam
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * -30, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 100)

def m02_Crane_Part2():
    # ####################################
    # Mission 02 - Crane Part 2
    # ####################################

    # Drive to Crane
    # front_motor.off(brake=True)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 9.5, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(-50), rotate * 83)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 19.5, brake=True)
    # front_motor.on_for_degrees(speed=SpeedPercent(40), degrees=90, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -10.0, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(-100), rotate * -100)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -25, brake=True)
    # front_motor.off(brake=False)

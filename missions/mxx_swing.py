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

def mxx_Swing():
    # ####################################
    # Mission 7 - Swing
    # ####################################

    #front_motor.on_for_degrees(speed=SpeedPercent(-10), degrees=85)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 50, brake=True)
    #tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate * 2)
    #tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 22, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate * 20)


    tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(40), ratio_degrees_to_inches * 8, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -12, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate * -20)

    #front_motor.on_for_degrees(speed=SpeedPercent(-100), degrees=-100)

    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -50, brake=True)

    #front_motor.off(brake=False)
    return


    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate * 18)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 11, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * -50, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate * 20)


    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -10000, brake=True)

    # Drive forward
    # tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 16, brake=True)

    #! Turn left 45 degrees
    # tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate * 45)

    # front_motor.on_for_degrees(SpeedPercent(100), 5 * 360)

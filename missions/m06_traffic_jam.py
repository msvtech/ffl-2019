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

    # tank_drive.on_for_degrees(SpeedPercent(75), SpeedPercent(75), ratio_degrees_to_inches * 10, brake=True)
    # tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate*-45)
    # tank_drive.on_for_degrees(SpeedPercent(75), SpeedPercent(75), ratio_degrees_to_inches * 8, brake=True)
    # tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate*45)
    # tank_drive.on_for_degrees(SpeedPercent(75), SpeedPercent(75), ratio_degrees_to_inches * 10, brake=True)
    # tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate*75)


    tank_drive.on_for_degrees(SpeedPercent(75), SpeedPercent(75), ratio_degrees_to_inches * 12, brake=True)
    front_motor.on(speed=SpeedPercent(-100))
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 6, brake=True)
    time.sleep(1.00)
    front_motor.off(brake=True)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -10, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate*-75)
    tank_drive.on_for_degrees(SpeedPercent(75), SpeedPercent(75), ratio_degrees_to_inches * -40, brake=True)


if __name__ == '__main__':
    m06_TrafficJam()

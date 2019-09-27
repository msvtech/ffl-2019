#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C # , OUTPUT_D
# from ev3dev2.sensor.lego import GyroSensor, ColorSensor, TouchSensor
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

ratio_degrees_to_inches = 360 / 8.44
rotate = 188.0 / 90.0

# Mission 10 - Steel Construction
tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 3.0000001, brake=True)
time.sleep(0.5)
front_motor.on(speed=SpeedPercent(40))
time.sleep(1)
tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 9, brake=True)
time.sleep(0.5)
front_motor.off()
#tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(-30), ratio_degrees_to_inches * 11, brake=True)
#tank_drive.on_for_degrees(SpeedPercent(10), SpeedPercent(100), ratio_degrees_to_inches * 7, brake=True)
#tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 20, brake=True)
#tank_drive.on_for_degrees(SpeedPercent(-100), SpeedPercent(100), rotate * 80)
#tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 100, brake=True)

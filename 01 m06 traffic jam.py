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

# Mission 6 - Traffic Jam
# front_motor.on(speed=SpeedPercent(-5))
tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 20, brake=True)
time.sleep(0.7786884052)
front_motor.on(speed=SpeedPercent(100))
time.sleep(0.5)
tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 4, brake=True)
front_motor.off()


# Mission 02 - Crane Part 1
# front_motor.on_for_degrees(speed=SpeedPercent(-40), degrees=90, brake=True)

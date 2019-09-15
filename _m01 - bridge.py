#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
import time

ratio_degrees_to_inches = 360 * 1.6 / 12
rotate90 = 137 / 90.0
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 40)
tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 20)
time.sleep(2)
tank_drive.on_for_degrees(SpeedPercent(-100), SpeedPercent(-100), ratio_degrees_to_inches * 1000000)

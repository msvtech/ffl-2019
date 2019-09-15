#!/usr/bin/env micropython

from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import time

rotate90 = 188
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

# Right turn 90 degree
tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(-100), rotate90)
time.sleep(0.5)

# Left turn 360 degree
tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate90 * 4)
time.sleep(0.5)

# Right turn 180 degree then 90 degree
tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate90 * 2)
time.sleep(0.5)
tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate90 * 1)

# tank_drive.on_for_rotations(SpeedPercent(25), SpeedPercent(100), 6)

# l1 = LargeMotor(OUTPUT_A)
# l2 = LargeMotor(OUTPUT_B)
# l1.on_for_rotations(SpeedPercent(75), 5)
# l2.on_for_rotations(SpeedPercent(-75), 5)

# tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)
# tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)

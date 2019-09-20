#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
# from ev3dev2.sensor.lego import GyroSensor, ColorSensor
import time
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
front_motor = MediumMotor(OUTPUT_C)
# top_motor = MediumMotor(OUTPUT_D)

ratio_degrees_to_inches = 360 / 8.44
rotate90 = 137 / 90.0

# Drive forward
tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 36, brake=True)

# Turn left 45 degrees
tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 45)

# Drive Forward
tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 10.5, brake=True)

time.sleep(1)

# Drive Backwards
tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(-30), ratio_degrees_to_inches * 10.5, brake=True)

# Turn Right 45 degrees
tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate90 * 45)
tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(-30), ratio_degrees_to_inches * 16, brake=True)

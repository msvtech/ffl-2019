#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
# from ev3dev2.sensor.lego import GyroSensor, ColorSensor
import time
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
front_motor = MediumMotor(OUTPUT_C)
# top_motor = MediumMotor(OUTPUT_D)

ratio_degrees_to_inches = 360 / 8.44
rotate90 = 137 / 90.0

tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 58)

tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 40, brake=True)

tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate90 * 18)

tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 11, brake=True)

tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 50, brake=True)

tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), rotate90 * 20)


tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 10000, brake=True)

# Drive forward
# tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 16, brake=True)

<<<<<<< HEAD
#! Turn left 45 degrees
# tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 45)
=======
# Turn left 45 degrees
tank_drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), rotate90 * 45)

# front_motor.on_for_degrees(SpeedPercent(100), 5 * 360)
>>>>>>> master

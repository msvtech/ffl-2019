#!/usr/bin/env micropython

from ev3dev2.motor import MediumMotor, OUTPUT_C, SpeedPercent
import time

front_motor = MediumMotor(OUTPUT_C)

# front_motor.on_for_degrees(speed=SpeedPercent(5), degrees=3)

# for i in range(6):
#     front_motor.on_for_degrees(speed=SpeedPercent(1), degrees=15)
#     time.sleep(0.5)

front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=90)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(10), degrees=90)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=45)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=45)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(10), degrees=90)

time.sleep(1)
front_motor.on_for_degrees(speed=SpeedPercent(-5), degrees=-2)


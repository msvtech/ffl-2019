#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor,OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from math import cos, radians, degrees
import time
import os
import sys

def main():
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    gs = GyroSensor()
    # cl = ColorSensor()
    # light = cl.reflected_light_intensity

    while True:
        # angle = gs.angle
        # rate = gs.rate
        angleAndRate = gs.angle_and_rate
        deg = angleAndRate[0]

        msg = str(deg) + ' degrees' # + '   ' + str(angleAndRate[1]) + ' rate'
        print(deg)
        debug_print(deg)

        time.sleep(1)


# state constants
ON = True
OFF = False

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)

if __name__ == '__main__':
    main()

import os
import sys
import time
from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C # , OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor

# state constants
ON = True
OFF = False

ts = TouchSensor()

def wait_for_button_with_message(msg):
    print_message(msg + '...')
    wait_for_button()
    print_message(msg + ' running')

def wait_for_button():
    while not ts.value():
        time.sleep(0.1)

def print_message(msg):
    reset_console()
    print('')
    print(msg)
    debug_print('')
    debug_print(msg)

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

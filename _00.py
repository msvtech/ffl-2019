#!/usr/bin/env micropython
import time
from utility import wait_for_button_with_message, reset_console, set_cursor, set_font, OFF

from missions.m01_elevated_places           import m01_ElevatedPlaces
from missions.m02_crane                     import m02_Crane_Part1, m02_Crane_Part2
from missions.m06_traffic_jam               import m06_TrafficJam
from missions.m07_swing                     import m07_Swing
from missions.m08_elevator                  import m08_Elevator
from missions.m09_safetyfactor              import m09_SafetyFactor
from missions.m10_steel_construction        import m10_SteelConstruction
from missions.m11_innovative_architecture   import m11_InnovativeArchitecture
from missions.m12_13_white_circle           import m12_WhiteCircle
from missions.m12_13_beige_circle           import m12_BeigeCircle, m12_BeigeCircleStacked
from missions.m12_13_red_circle             import m12_RedCircle
from missions.mxx_swing                     import mxx_Swing

def main(startAt):
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-TerminusBold32x16')

    #if startAt <=  1 : wait_for_button_with_message('Crane 1');         m02_Crane_Part1()
    #if startAt <=  1 : wait_for_button_with_message('Traffic');         m06_TrafficJam()
    #if startAt <=  1 : wait_for_button_with_message('White Circle');    m12_WhiteCircle()

    if startAt <=  1 : wait_for_button_with_message('Swing');            mxx_Swing()
    if startAt <=  2 : wait_for_button_with_message('Crane 2');         m02_Crane_Part2()
    if startAt <=  3 : wait_for_button_with_message('Elevator');         m08_Elevator()
    if startAt <=  4 : wait_for_button_with_message('SafetyFactor');     m09_SafetyFactor()
    if startAt <=  5 : wait_for_button_with_message('Beige Circle');    m12_BeigeCircleStacked()
    if startAt <=  6 : wait_for_button_with_message('Red Circle');      m12_RedCircle()
    if startAt <=  7 : wait_for_button_with_message('Architecture');    m11_InnovativeArchitecture()
    if startAt <=  8 : wait_for_button_with_message('Elevated Places'); m01_ElevatedPlaces()

if __name__ == '__main__':
    main(8)

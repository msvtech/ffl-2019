#!/usr/bin/env micropython
import time
from utility import wait_for_button_with_message

from m01_elevated_places            import m01_ElevatedPlaces
from m02_crane                      import m02_Crane_Part1, m02_Crane_Part2
from m06_traffic_jam                import m06_TrafficJam
from m07_swing                      import m07_Swing
from m10_steel_construction         import m10_SteelConstruction
from m11_innovative_architecture    import m11_InnovativeArchitecture
from m12_13_white_circle            import m12_WhiteCircle
from m12_13_beige_circle            import m12_BeigeCircle
from m12_13_red_circle              import m12_RedCircle

def main():

    wait_for_button_with_message('Crane 1')
    m02_Crane_Part1()

    wait_for_button_with_message('Traffic')
    m06_TrafficJam()

    wait_for_button_with_message('Swing')
    m07_Swing()

    wait_for_button_with_message('Crane 2')
    m02_Crane_Part2()

    wait_for_button_with_message('White Circle')
    m12_WhiteCircle()

    wait_for_button_with_message('Beige Circle')
    m12_BeigeCircle()

    wait_for_button_with_message('Red Circle')
    m12_RedCircle()

    wait_for_button_with_message('Architecture')
    m11_InnovativeArchitecture()

    wait_for_button_with_message('Elevated Places')
    m01_ElevatedPlaces()

if __name__ == '__main__':
    main()

#!/usr/bin/env micropython
import time
from _01_m06_traffic_jam import Crane, Traffic
from utility import wait_for_button_with_message

def main():

    wait_for_button_with_message('Crane')
    Crane()

    wait_for_button_with_message('Traffic')
    Traffic()

if __name__ == '__main__':
    main()

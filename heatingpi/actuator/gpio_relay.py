#!/usr/bin/env python
#
# A simple GPIO controlled relay.
#

import RPi.GPIO as GPIO

class GPIORelay(object):
    """
    A GPIORelay is a relay controlled by one of the GPIO pins on the Pi.
    """

    def __init__(self, name, gpio):
        self.name = name
        self.gpio = gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.OUT)

    def set(self, state=False):
        GPIO.output(self.gpio, state)

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="GPIO Relay options")
    parser.add_argument("--gpio", help="GPIO Pin Number (BCM ID)", default=17)
    parser.add_argument("--state", help="Switch state", type=bool, default=False)

    args = parser.parse_args()
    relay = GPIORelay("gpio_relay", args.gpio)
    relay.set(args.state)











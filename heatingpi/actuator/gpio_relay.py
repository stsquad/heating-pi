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
        self.gpio = int(gpio)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup(self.gpio)

    def set(self, state=False):
        GPIO.output(self.gpio, state)

if __name__ == "__main__":
    from argparse import ArgumentParser
    from time import sleep

    parser = ArgumentParser(description="GPIO Relay options")
    parser.add_argument("--gpio", help="GPIO Pin Number (BCM ID)", default=17)
    parser.add_argument("--on", help="Switch on", dest="state", action="store_true")
    parser.add_argument("--off", help="Switch off", dest="state", action="store_false")

    args = parser.parse_args()
    relay = GPIORelay("gpio_relay", args.gpio)
    relay.set(args.state)
    print "Set GPIO %s to %s" % (args.gpio, args.state)
    sleep(10)
    print "Done now..."










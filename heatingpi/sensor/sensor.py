#!/usr/bin/env python
#
#
"""
Base sensor classes and helper functions
"""
from argparse import ArgumentParser
from time import sleep, asctime


class Sensor(object):
    """
    A sensor is anything that returns a sensed state
    """

    def __init__(self, stype="sensor", name="sensor", num=1):
        self.stype = stype
        self.name = name
        self.num = int(num)

    def __str__(self):
        return "Sensor %s (%s)" % (self.name, self.stype)

    def log_data(self, array_of_data):
        """
        Log the sensor data
        """
        print "%s: %s %s" % (asctime(), str(self), array_of_data)
    
        

def common_args():
    """Return an argument parser with common sensor arguments"""
    parser = ArgumentParser(description="Sensor arguments")
    parser.add_argument("--name", help="Unique name of the sensor")
    return parser

def poll_sensor(period, sensor):
    """Poll a sensor every couple of seconds and report the result"""
    while True:
        sensor.poll()
        sleep(period)




















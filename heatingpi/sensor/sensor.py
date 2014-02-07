#!/usr/bin/env python
#
#
"""
Base sensor classes and helper functions
"""
from argparse import ArgumentParser


class Sensor(object):
    """
    A sensor is anything that returns a sensed state
    """

    def __init__(self, type="sensor", name):
        self.type = type
        self.name = name

    def __str__(self):
        return "%s sensor called %s" % (self.type, self.name)
    
        

def common_args():
    """Return an argument parser with common sensor arguments"""
    parser = ArgumentParser(description="Sensor arguments")
    parser.add_argument("--name", description="Unique name of the sensor")
    return parser

def poll_sensor(period, sensor):
    """Poll a sensor every couple of seconds and report the result"""
    while True:
        sensor.poll()
        sleep(period)




















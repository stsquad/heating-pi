#!/usr/bin/env python
#

from sensor import Sensor

class TempSensor(Sensor):
    """A TempSensor is a basic sensor the returns a temperature"""

    def __init__(self, name):
        super(TempSensor, self).__init__("temperature", name)

        




















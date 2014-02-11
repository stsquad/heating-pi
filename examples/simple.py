#!/usr/bin/env python
#
# A very simple example of usage
#


#
# This is just a workaround for using the library direct out of the
# source tree. It isn't required if the Heating Pi modules are
# correctly installed on the system.
#
import os,sys
from os.path import realpath,dirname
base_dir = os.path.dirname(os.path.abspath("%s/.." % (__file__)))
if os.path.exists("%s/heatingpi" % (base_dir)):
    print("Adding "+base_dir+" to path")
    sys.path.insert(0, base_dir)

#from heatingpi.sensor import SerialTempSensor
from heatingpi.controller.simple_thermostat import SimpleThermostat
from heatingpi.sensor.test_temp_sensor import TestTempSensor
from heatingpi.actuator.gpio_relay import GPIORelay

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Example options")
    parser.add_argument("--period", help="Polling period", type=float)
    parser.add_argument("--target", help="Target temp", type=float)

    args = parser.parse_args()
    sensor = TestTempSensor("test", 1, 10, 20)
    actuator = GPIORelay("relay1", 17)
    controller = SimpleThermostat(sensor, actuator, args.target, args.period)

    controller.run()
    

    



















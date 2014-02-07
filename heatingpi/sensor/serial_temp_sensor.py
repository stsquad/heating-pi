#!/usr/bin/env python
#
# A simple temperature sensor that is plugged into the serial port of
# the Pi and reports a temperature every now and again.
#

from temp_sensor import TempSensor
from serial import Serial

class SerialTempSensor(TempSensor):
    """
    A SerialTempSensor expects to read a temperture from a serial port
    (by default ttyAMA0)
    """

    def __init__(self, name="ttyAMA0", dev="/dev/ttyAMA0", baud=9600):
        super(SerialTempSensor, self).__init__(name)
        self.port = Serial(dev, baud)

    def poll(self):
        line = self.port.readline()
        print "got %s" % (line)


if __name__ == "__main__":
    from sensor import common_args, poll_sensor
    parser = common_args()
    serial_args = parser.add_argument_group("Serial Temp Sensor options")
    serial_args.add_argument("--dev", help="Serial device", default="/dev/ttyAMA0")
    serial_args.add_argument("--baud", help="Baud Rate", default=9600)

    args = parser.parse_args()
    sensor = SerialTempSensor(name=args.name, dev=args.dev, baud=args.baud)
    poll_sensor(20, sensor)





















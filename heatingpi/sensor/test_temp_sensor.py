#!/usr/bin/env python
#
# A test test sensor for generating random temp data
#

from temp_sensor import TempSensor
from random import uniform

class TestTempSensor(TempSensor):

    def __init__(self, name, number, min, max):
        super(TestTempSensor, self).__init__(name=name, num=number)
        self.min = min
        self.max = max

    def poll(self):
        data = []
        for x in range(0, self.num):
            data.append(uniform(self.min, self.max))
        self.log_data(data)

if __name__ == "__main__":
    from sensor import common_args, poll_sensor
    parser = common_args()
    test_args = parser.add_argument_group("Test Temp Sensor options")
    test_args.add_argument("--min", help="Minimum temp", default=0.0)
    test_args.add_argument("--max", help="Maximum temp", default=30.0)
    test_args.add_argument("--num", help="Number of values", default=1)
    

    args = parser.parse_args()
    sensor = TestTempSensor(args.name, args.num, args.min, args.max)
    poll_sensor(10, sensor)

                      





















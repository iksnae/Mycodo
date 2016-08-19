# coding=utf-8


import time
from tentacle_pi.TSL2561 import TSL2561


class TSL2561_read(object):
    def __init__(self, address, bus):
        self._lux = None
        self.i2c_address = i2c_address
        self.i2c_bus = bus
        self.running = True

    def read(self):
        try:
            tsl = TSL2561(self.i2c_address, "/dev/i2c-"+str(self.i2c_bus))
            tsl.enable_autogain()
            # tsl.set_gain(16)
            tsl.set_time(0x00)
            self._lux = tsl.lux()
        except:
            return 1

    @property
    def lux(self):
        return self._lux


    def __iter__(self):
        """
        Support the iterator protocol.
        """
        return self

    def next(self):
        """
        Call the read method and return lux information.
        """
        if self.read():
            return None
        response = {
            'lux': self.lux
        }
        return response

    def stopSensor(self):
        self.running = False


if __name__ == "__main__":
    tsl2561 = TSL2561_read('0x39')

    for measurement in tsl2561:
        print("Lumenosity: {} lux".format(measurement['lux']))
        time.sleep(3)

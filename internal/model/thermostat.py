import random
from internal.model.device_interface import DeviceBaseClass
from internal.constants.enums import DeviceType


class Thermostat(DeviceBaseClass):
    """Class representing a Thermostat iot device"""

    def __init__(self, device_id, device_name, device_metadata):
        super().__init__(device_id, device_name, DeviceType.THERMOSTAT, device_metadata)
        self.curr_timestamp = 0
        random.seed(1)

    def send(self, command):
        self.curr_timestamp += 1
        print("Got command %s on device with id: %s" % (command, self.id))
        return (self.curr_timestamp, True)

    def get(self, options):
        self.curr_timestamp += 1
        print("Got options %s on device with id: %s" % (options, self.id))
        return (self.curr_timestamp, random.randint(1, 5))

    def update(self, options):
        pass

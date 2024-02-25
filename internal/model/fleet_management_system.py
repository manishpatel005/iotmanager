from internal.model.fleet_management_system_interface import (
    FleetManagementSystemInterface,
)
from internal.model.device_interface import DeviceBaseClass
from typing import List
import collections


class FMS(FleetManagementSystemInterface):
    """FMS enables management of iot devices"""

    def __init__(self):
        super().__init__()
        # devices map stores device_id to device
        self.devices = collections.defaultdict(DeviceBaseClass)
        # device_data map stores device_id to list of (timestamp, value)
        self.device_data = collections.defaultdict(list)

    def registerDevices(self, devices: List[DeviceBaseClass]):
        for device in devices:
            print("Registerd device %s with id %s" % (device.name, device.id))
            self.devices[device.id] = device
            self.device_data[device.id] = []

    def deregisterDevices(self, devices: List[DeviceBaseClass]):
        for device in devices:
            if device in self.devices:
                print("De-registerd device %s with id %s" % (device.name, device.id))
                del self.devices[device.id]
                del self.device_data[device.id]
            else:
                print("Device %s with id %s not found" % (device.name, device.id))

    def sendCommand(self, device_ids: List[str], command):
        output = []
        for device_id in device_ids:
            if device_id in self.devices:
                print("Sending command to the device with id %s" % (device_id))
                out = self.devices[device_id].send(command)
                output.append({device_id: out})
            else:
                print("Device with id %s not found" % (device_id))
                output.append({device_id: "Device not found"})
        return output

    def fetchData(self, device_ids: List[str], options):
        output = []
        for device_id in device_ids:
            if device_id in self.devices:
                print("Fetching data from device with id %s" % (device_id))
                out = self.devices[device_id].get(options)
                output.append({device_id: out})
            else:
                print("Device with id %s not found" % (device_id))
                output.append({device_id: "Device not found"})
        return output

    def pushData(self, device_id, values: List):
        if device_id in self.device_data:
            self.device_data[device_id] += values
        else:
            print("Device with id %s not found" % (device_id))

    def updateDevices(self, devices, options):
        pass

    def queryData(self, device_options):
        output = {}
        for device_id, option in device_options.items(): # option is (startTS, endTS)
            startTS, endTS = option[0], option[1]
            out_val = []
            # Naive approach is to scan the list and pick all values which satisfy TS criterion
            for val in self.device_data[device_id]:
                print(val)
                if val[0] >= startTS and val[0] <= endTS:
                    out_val.append(val)
            output[device_id] = out_val
        return output

from internal.model.fleet_management_system_interface import FleetManagementSystemInterface
from internal.model.device_interface import DeviceBaseClass
from typing import List
import collections


class FMS(FleetManagementSystemInterface):
    def __init__(self):
        super().__init__()
        self.devices = collections.defaultdict(DeviceBaseClass)

    def registerDevices(self, devices: List[DeviceBaseClass]):
        for device in devices:
            print("Registerd device %s with id %s" % (device.name, device.id))
            self.devices[device.id] = device

    def deregisterDevices(self, devices: List[DeviceBaseClass]):
        for device in devices:
            if device in self.devices:
                print("De-registerd device %s with id %s" % (device.name, device.id))
                del self.devices[device.id]
            else:
                print("Device %s with id %s not found" % (device.name, device.id))

    def sendCommand(self, devices: List[DeviceBaseClass], command):
        output = []
        for device in devices:
            if device.id in self.devices:
                print(
                    "Sending command to the device %s with id %s"
                    % (device.name, device.id)
                )
                out = device.send(command)
                output.append({device.id: out})
            else:
                print("Device %s with id %s not found" % (device.name, device.id))
                output.append({device.id: "Device not found"})
        return output

    def getData(self, devices: List[DeviceBaseClass], options):
        output = []
        for device in devices:
            if device.id in self.devices:
                print(
                    "Fetching data from devices %s with id %s"
                    % (device.name, device.id)
                )
                out = device.get(options)
                output.append({device.id: out})
            else:
                print("Device %s with id %s not found" % (device.name, device.id))
                output.append({device.id: "Device not found"})
        return output

    def updateDevices(self, devices, options):
        pass

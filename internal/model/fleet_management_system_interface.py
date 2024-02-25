from abc import ABC, abstractmethod
from internal.model.device_interface import DeviceBaseClass
from typing import List


class FleetManagementSystemInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def registerDevices(self, devices: List[DeviceBaseClass]):
        raise NotImplementedError("Implement registerDevice method")

    @abstractmethod
    def deregisterDevices(self, devices: List[DeviceBaseClass]):
        raise NotImplementedError()

    @abstractmethod
    def sendCommand(self, devices: List[DeviceBaseClass], command):
        raise NotImplementedError()

    @abstractmethod
    def getData(self, devices: List[DeviceBaseClass], options):
        raise NotImplementedError()

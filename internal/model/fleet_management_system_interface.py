from abc import ABC, abstractmethod
from internal.model.device_interface import DeviceBaseClass
from typing import List


class FleetManagementSystemInterface(ABC):
    """Interface for iot device fleet management system"""

    def __init__(self):
        pass

    @abstractmethod
    def registerDevices(self, devices: List[DeviceBaseClass]):
        raise NotImplementedError("Implement registerDevice method")

    @abstractmethod
    def deregisterDevices(self, devices: List[DeviceBaseClass]):
        raise NotImplementedError()

    @abstractmethod
    def sendCommand(self, device_ids: List[str], command):
        raise NotImplementedError()

    @abstractmethod
    def fetchData(self, device_ids: List[str], options):
        raise NotImplementedError()

    @abstractmethod
    def queryData(self, device_options):
        raise NotImplementedError()
    
    @abstractmethod
    def pushData(self, device_id, values):
        raise NotImplementedError()
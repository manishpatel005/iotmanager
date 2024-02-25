from abc import ABC, abstractmethod
from internal.constants.enums import DeviceStatus


class DeviceBaseClass(ABC):
    def __init__(self, device_id, device_name, device_type, device_metadata):
        self.id = device_id
        self.name = device_name
        self.type = device_type
        self.metadata = device_metadata
        self.status = None
        self.values = []
        self.status = DeviceStatus.OFFLINE

    @abstractmethod
    def send(self, command):
        raise NotImplementedError()

    @abstractmethod
    def get(self, options):
        raise NotImplementedError()

    @abstractmethod
    def update(self, options):
        raise NotImplementedError()

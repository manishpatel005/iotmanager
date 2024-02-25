from enum import Enum


class DeviceStatus(Enum):
    OFFLINE = 10
    ONLINE = 20
    MAINTENANCE = 30


class DeviceType(Enum):
    CAMERA = 10
    SPEAKER = 20
    THERMOSTAT = 30
    BULB = 4

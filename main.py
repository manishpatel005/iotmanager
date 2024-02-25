from internal.model.fleet_management_system import FMS
from internal.model.camera import Camera


def main():
    # Initialize FLeet Management Sytem
    iotManager = FMS()
    # Create devices
    camera1 = Camera("X1", "Camera-NorthSide", {"model": "ABC"})
    camera2 = Camera("X2", "Camera-EastSide", {"model": "DEF"})
    devices = [camera1, camera2]
    iotManager.registerDevices(devices)
    iotManager.getData(devices, "")


if __name__ == "__main__":
    main()

from internal.model.fleet_management_system import FMS
from internal.model.camera import Camera
from internal.model.thermostat import Thermostat


def main():
    # Initialize FLeet Management Sytem
    iotManager = FMS()
    while True:
        # Create devices
        camera1 = Camera("X1", "Camera-NorthSide", {"model": "ABC"})
        camera2 = Camera("X2", "Camera-EastSide", {"model": "DEF"})
        thermostat1 = Thermostat("T1", "Nest-1", {"model": "Google Nest"})
        devices = [camera1, camera2, thermostat1]
        iotManager.registerDevices(devices)
        out_data = iotManager.fetchData([camera1.id, camera2.id, thermostat1.id], "")
        print(out_data)
        # let's push some data from devices
        iotManager.pushData(camera1.id, [camera1.get("")])
        iotManager.pushData(camera1.id, [camera1.get("")])
        iotManager.pushData(camera2.id, [camera2.get("")])
        output = iotManager.queryData({camera1.id: (1,3), camera2.id: (1,2)})
        print(output)
        break


if __name__ == "__main__":
    main()

from djitellopy import Tello

drone = Tello()
drone.connect()
print('Dronun Batareyası: ',drone.get_battery())
drone.takeoff()
if drone.get_barometer()>300:
    drone.land()
    drone.emergency()



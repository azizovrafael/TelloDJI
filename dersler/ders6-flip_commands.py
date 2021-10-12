from djitellopy import Tello

drone = Tello()
drone.connect()
print('Dronun Batareyası: ',drone.get_battery())
drone.takeoff()

drone.flip_left()
drone.flip_right()
drone.flip_back()
drone.flip_forward()


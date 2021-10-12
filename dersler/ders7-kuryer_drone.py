from djitellopy import Tello

drone = Tello()
drone.connect()
print('Dronun Batareyası: ',drone.get_battery())
drone.takeoff()

drone.move_forward(300)
drone.move_left(600)
drone.move_forward(1000)
drone.move_right(1000)


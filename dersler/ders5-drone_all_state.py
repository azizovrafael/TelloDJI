from djitellopy import Tello

drone = Tello()
drone.connect()
print('Dronun Hündürlüyü: ',drone.get_height())
print('Dronun Hündürlüyü: ',drone.get_distance_tof())
print('Dronun Batareyası: ',drone.get_battery())
print('Dronun Tempraturu: ',drone.get_temperature())
print('Dronun Ən Aşağı Tempraturu: ', drone.get_lowest_temperature())
print('Dronun Ən Aşağı Tempraturu: ',drone.get_highest_temperature())
print('Dronun X Istiqamıtində Sürəti: ',drone.get_speed_x())
print('Dronun Y Istiqamıtində Sürəti: ',drone.get_speed_y())
print('Dronun Z Istiqamıtində Sürəti: ',drone.get_speed_z())

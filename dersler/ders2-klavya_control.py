from djitellopy import Tello
import KeyboardPressModule as kp
import time

kp.init()
drone = Tello()
drone.connect()
print('Battery: ',drone.get_battery())
drone.takeoff()

def get_Key_Board_Input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 40

    if kp.get_key("LEFT"):
        lr = -speed
    if kp.get_key("RIGHT"):
        lr = speed

    if kp.get_key("UP"):
        fb = speed
    if kp.get_key("DOWN"):
        fb = -speed

    if kp.get_key("s"):
        ud = -speed
    if kp.get_key("w"):
        ud = speed

    if kp.get_key("a"):
        yv = -speed
    if kp.get_key("d"):
        yv = speed

    if kp.get_key("q"):
        yv = drone.land()

    if kp.get_key("t"):
        yv = drone.takeoff()

    if kp.get_key("f"):
        drone.flip_forward()

    print(lr,' ', fb,' ', ud, ' ',yv)

    return [lr, fb, ud, yv]

while True:
    dir = get_Key_Board_Input()
    print('Battery: ',drone.get_battery())
    drone.send_rc_control(dir[0],dir[1],dir[2],dir[3])
    if drone.get_mission_pad_id() > 0:
        print('Battery: ', drone.get_battery())
        print('Drone High: ',drone.get_distance_tof())
        print('Drone PAD ID: ', drone.get_mission_pad_id())
        drone.land()
        drone.emergency()
    time.sleep(0.05)

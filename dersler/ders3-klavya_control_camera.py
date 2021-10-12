from djitellopy import Tello
import KeyboardPressModule as kp  # -kimi

import cv2
import time

def get_Key_Board_Input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

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
        yv = speed

    if kp.get_key("d"):
        yv = -speed

    if kp.get_key("q"):
        drone.land()

    if kp.get_key("t"):
        drone.takeoff()

    if kp.get_key('i'):
        cv2.imwrite(f'Frame-{time.time()}.jpg',frame)
        print('Şəkil Çəkildi')

    if kp.get_key("f"):
        drone.flip_forward()


    return [lr, fb, ud, yv]

if __name__ == "__main__":
    kp.init()
    drone = Tello()
    drone.connect()
    drone.takeoff()
    drone.streamon()

    while True:
        dir = get_Key_Board_Input()
        drone.send_rc_control(dir[0],dir[1],dir[2],dir[3])
        frame = drone.get_frame_read().frame
        camera = cv2.resize(frame,(360,240))
        cv2.imshow('Camera Window',camera)
        cv2.waitKey(1)


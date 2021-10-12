from djitellopy import Tello
import cv2

drone = Tello()
drone.connect()
drone.streamon()

while True:
    frame = drone.get_frame_read().frame
    camera = cv2.resize(frame, (360, 240))
    cv2.imshow('Kamera Window',camera)
    cv2.waitKey(1)
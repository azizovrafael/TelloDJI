from djitellopy import Tello
import KeyboardPressModule as kp
import time
import csv

namafile = 'droneData3D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"

x_value = 0
y_value = 0
z_value = 0

fieldnames = [header1, header2, header3]

with open(namafile, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

kp.init()
drone = Tello()
drone.connect()
drone.takeoff()

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
        yv = -speed
    if kp.get_key("d"):
        yv = speed

    if kp.get_key("q"):
        yv = drone.land()

    if kp.get_key("t"):
        yv = drone.takeoff()

    if kp.get_key("k"):
        drone.flip_forward()


    return [lr, fb, ud, yv]


while True:
    print('Drone Battery: ' ,drone.get_battery())
    dir = get_Key_Board_Input()
    drone.send_rc_control(dir[0],dir[1],dir[2],dir[3])
    with open(namafile, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            header1: x_value,
            header2: y_value,
            header3: z_value
        }
        csv_writer.writerow(info)
        print(x_value, y_value, z_value)

        x_value += int(dir[0])
        y_value += int(dir[1])
        z_value += int(dir[2])

    time.sleep(0.05)


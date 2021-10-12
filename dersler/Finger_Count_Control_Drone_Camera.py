import cv2
import time
import os
import HandTrackingModule as htm
from djitellopy import Tello

drone = Tello()
drone.connect()
drone.takeoff()
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
def get_Hand_Finger_Input(x):
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 40

    if int(x) == 1:
        fb = speed
    if int(x) == 2:
        fb = -speed
    if int(x) == 3:
        lr = speed
    if int(x) == 4:
        lr = -speed
    if int(x) == 5:
        ud = speed
    if int(x) == 0:
        ud = -speed

    print(lr,' ', fb,' ',ud)

    return [lr, fb, ud]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        print(totalFingers)
        dir = get_Hand_Finger_Input(totalFingers)
        print('Battery: ', drone.get_battery())
        drone.send_rc_control(dir[0], dir[1], dir[2], 0)
        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 25)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

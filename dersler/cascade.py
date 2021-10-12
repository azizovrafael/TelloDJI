from djitellopy import tello
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
me = tello.Tello()
me.connect()
print('Connection Okay')
print('Battery : ',me.get_battery())
#me.takeoff()
me.streamon()
#me.send_rc_control(0,10,0,0)
#me.send_rc_control(0,0,0,40)
#me.send_rc_control(0,10,0,0)
#me.send_rc_control(0,0,0,30)
while True:
    img  = me.get_frame_read().frame
    img  = cv2.resize(img,(360,240))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Kamera',img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        me.streamoff()
        break
#print('Sleep Time Start')
#sleep(60)
#time.sleep(60)
#print('1')
#print('1')
#print('1')
#me.land()
#print('1')
#------------------Teke Off--------
#me.takeoff()

#me.send_rc_control(20,0,0,0)
#print('Rc Control 1')
#sleep(2)
#me.send_rc_control(0,20,0,0)
#print('Rc Control 2')
#sleep(2)
#me.send_rc_control(0,0,20,0)
#print('Rc Control 3')
#sleep(2)
#me.send_rc_control(0,0,0,20)
#print('Rc Control 4')
#sleep(2)


#me.send_re_contro( sag , qabaqa , hundrluk , etrafinda Donme )

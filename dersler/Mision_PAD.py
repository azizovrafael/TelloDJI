from djitellopy import Tello

drone = Tello()
drone.connect()
print('Battery: ',drone.get_battery())
drone.takeoff()
PAD_List = []
distance = 0
move_list = ['forward','right','back','left',]
for i in range(4):
    for i in range(10): # 2 metr en- uzunluq kavadrat erazi
        print('--------------------------------------------------')
        print('Pad List: ',PAD_List)
        drone.move(move_list[i],20)
        print(drone.get_mission_pad_id())
        distance+=20
        if drone.get_mission_pad_id() > 0:
            if PAD_List.count(drone.get_mission_pad_id()) > 0:
                print(drone.get_mission_pad_id(), ' Idli Mina Askar Olunub')
            else:
                PAD_List.append(drone.get_mission_pad_id())
                print('Detected: ',distance,' mm')
drone.land()
drone.emergency()

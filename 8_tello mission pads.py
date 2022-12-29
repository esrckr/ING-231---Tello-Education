from djitellopy import Tello

# create and connect
tello = Tello()
tello.connect()
print(tello.get_battery())

# configure drone

tello.set_video_direction(Tello.CAMERA_DOWNWARD)

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)  # forward detection only  
#tello.takeoff()

pad = tello.get_mission_pad_id()
print("padi gördüm",pad,"x:",tello.get_mission_pad_distance_x(),"y:",tello.get_mission_pad_distance_y(),"z:",tello.get_mission_pad_distance_z())
# detect and react to pads until we see pad #1
n=0
while pad!=1:
    print("padi gördüm",pad,"x:",tello.get_mission_pad_distance_x(),"y:",tello.get_mission_pad_distance_y(),"z:",tello.get_mission_pad_distance_z())
    if pad!=-1:
       # tello.move_back(30)
       # tello.rotate_clockwise(90)
       pass
    n+=1
    print("dönüyorum",n)
    pad = tello.get_mission_pad_id()
"""
while pad != 1:
    if pad == 2:
        print("padi gördüm",pad,"x:",tello.get_mission_pad_distance_x(),"y:",tello.get_mission_pad_distance_y(),"z:",tello.get_mission_pad_distance_z())
        tello.move_back(30)
        tello.rotate_clockwise(90)
        print("burdayım", pad)

    n+=1
    print("dönüyorum",n)
    pad = tello.get_mission_pad_id()
    print("padi gördüm",pad,"x:",tello.get_mission_pad_distance_x(),"y:",tello.get_mission_pad_distance_y(),"z:",tello.get_mission_pad_distance_z())
"""
"""
    if pad == 4:
        tello.move_up(30)
        tello.flip_forward()
        print("burdayım 2")
"""


# graceful termination
tello.disable_mission_pads()
#tello.land()
print("tamam 1 i gördüm")
tello.end()

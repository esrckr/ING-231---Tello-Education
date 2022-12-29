from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

#tello.move_left(100)
tello.rotate_clockwise(100)
tello.move_forward(100)
"""
tello.move_back(30)
tello.flip_back()
tello.flip_right()
"""

tello.land()

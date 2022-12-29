# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()
#tello.set_video_direction(Tello.CAMERA_FORWARD)
tello.streamon()
frame_read = tello.get_frame_read()

#tello.takeoff()
print("Komutlar: l : yere in ve kapat \n \
      w: ileri \n \
      s: geri \n \
      a: sola \n \
      d: sağa \n \
      e: döndür \n \
      q: ters yöne döndür \n \
      r: yukarı \n \
      f: aşağı \n \
      t: takla \n \ ")

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    # 在实际开发里请在另一个线程中显示摄像头画面，否则画面会在无人机移动时静止
    img = frame_read.frame
    cv2.imshow("drone", img)
    key=input("Komut girin ve enter'a basın 'l,w,s,a,d,e,q,r,f':  ")
#    key = cv2.waitKey(1) and 0xff
    if key == "l": # land
        print("l ile yere in ve kapan")
        break
    elif key == 'w':
        print("w ile 30 cm ileri")
        tello.move_forward(30)
    elif key == 's':
        print("s ile 30 cm geri")
        tello.move_back(30)
    elif key == 'a':
        print("a ile 30 cm sola")
        tello.move_left(30)
    elif key == 'd':
        print("d ile 30 cm sağa")
        tello.move_right(30)
    elif key == 'e':
        print("e ile 30  cm rotate")
        tello.rotate_clockwise(30)
    elif key == 'q':
        print("q ile 30  cm rotate")
        tello.rotate_counter_clockwise(30)
    elif key == 'r':
        print("r ile 30 cm yukarı")
        tello.move_up(30)
    elif key == 'f':
        print("f ile 30 cm aşağı")
        tello.move_down(30)
    elif key == 't':
        print("t ile takla")
        tello.flip("b")

#tello.land()

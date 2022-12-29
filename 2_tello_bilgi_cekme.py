import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()
#kaldırmadan motor çalışsın
tello.turn_motor_on()

#barometre bilgisini al
print("Barometre bilgisi", tello.get_barometer())

#5 sn motor çalışsın
time.sleep(5)
print("Speed bilgisi", tello.get_speed_x())
print("Battery bilgisi", tello.get_battery())
print("Flight time bilgisi", tello.get_flight_time())
print("Snr signal noise ratio bilgisi", tello.query_wifi_signal_noise_ratio())
print("TOF time of flight distance in cm uzaklık bilgisi", tello.get_distance_tof())




#kaldırmadan motor kapatsın
tello.turn_motor_off()

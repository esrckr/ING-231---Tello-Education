import threading
import socket
import sys
import time
import platform

host=""
port=9000
locaddr=(host,port)

#create UDP socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(locaddr)

tello_address=("192.168.10.1","8889")

sock.sendto(b'command',locaddr)
sock.sendto(b"takeoff", locaddr)
sock.sendto(b"left 25", locaddr)
sock.sendto(b"backward 25", locaddr)
sock.sendto(b"right 25", locaddr)
sock.sendto(b"forward 25", locaddr)

sock.sendto(b"battery?", locaddr)

response,ip=socket.recvform(1024)
print(response)

sock.sendto(b"land", locaddr)
sock.close()



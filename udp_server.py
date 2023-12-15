import socket
from sense_hat import SenseHat 

# Binding to 0.0.0.0 allows UDP connections to any address
# that the device is using
UDP_IP = "0.0.0.0"
UDP_PORT = 5000
red = (255, 0, 0)
blue= (0,0,255)

sock = socket.socket(socket.AF_INET, # Use Internet socket family
                     socket.SOCK_DGRAM) # Use UDP packets
addr = (UDP_IP, UDP_PORT)
sock.bind(addr)

sense = SenseHat()

while True:
    data, addr = sock.recvfrom(1024)
    print(data)
    sense.show_message(data.decode(), text_colour=red, back_colour=blue, scroll_speed=0.3)
    sense.clear()


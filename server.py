import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

s = socket.socket()
host = get_ip_address('wlan0')
port = 7600
s.bind((host, port))

s.listen(5)

while True:
    c, address = s.accept()
    print 'recieved connection request from device: ', address
    c.send('Awesome!')
    c.close()

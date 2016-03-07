import socket

s = socket.socket()
host = socket.gethostname()
port = 7600
s.bind((host, port))

s.listen(5)

while True:
    c, address = s.accept()
    print 'recieved connection request from device: ', address
    c.send('Awesome!')
    c.close()

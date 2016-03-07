import socket

s = socket.socket()
host = socket.gethostname()
port = 7600

s.connect((host, port))
print s.recv(1234)
s.close

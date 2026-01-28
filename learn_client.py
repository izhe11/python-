import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))     #连接到指定网络地址
print(s.recv(1024))
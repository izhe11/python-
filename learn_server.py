import socket

s = socket.socket()          #创建socket对象
host = socket.gethostname()  #获取host，主机名
port = 12345                 #端口
s.bind((host, port))         #绑定host与端口，组成网络地址

s.listen(5)                  #开启监听
while True:
    conn, addr = s.accept()  #等待连接
    print('Connection address:', addr)
    conn.send(b'thank you for connecting')
    conn.close()

from socketserver import TCPServer,StreamRequestHandler

class MyHandler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()    #获取客户端地址
        print('get connection from',addr)
        self.wfile.write(b'connect seccessful')     #写入数据

server = TCPServer(('',12345), MyHandler)
server.serve_forever()

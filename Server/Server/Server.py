__author__ = 'Yuheng Chen'
from tornado.tcpserver import TCPServer

class BaseServer(TCPServer):
    def handle_stream(self, stream, address):
        print "New request :", address, stream
        
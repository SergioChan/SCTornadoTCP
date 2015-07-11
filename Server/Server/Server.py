__author__ = 'Yuheng Chen'
from tornado.tcpserver import TCPServer
from Connection.Connection import Connection

class BaseServer(TCPServer):
    def handle_stream(self, stream, address):
        print "New request :", address, stream
        Connection(address=address,stream=stream)
        
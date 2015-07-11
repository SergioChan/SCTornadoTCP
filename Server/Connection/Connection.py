__author__ = 'Yuheng Chen'

class Connection(object):
    clients = set()
    def __init__(self, stream, address):
        Connection.clients.add(self)
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.on_close)
        self.read_message()
        print "New Connection from server: ", address

    def read_message(self):
        self._stream.read_until('\n', self.handle_request)

    def handle_request(self,data):
        print 'Request is ', data[:-1]
        self.read_message()

    def on_close(self):
        print "Server connection has been closed: ", self._address
        Connection.clients.remove(self)
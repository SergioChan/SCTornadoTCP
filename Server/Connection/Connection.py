# coding=utf-8
__author__ = 'Yuheng Chen'

from Request.Request import Request
import Handler.Handler
from Handler.Handler import BaseHandler
import urls
from tornado.iostream import StreamClosedError


class Connection(object):
    clients = set()

    def __init__(self, stream, address):
        Connection.clients.add(self)
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.on_close)
        self.read_request()
        print "New Connection from server: ", address

    def read_request(self):
        try:
            self._stream.read_until('\n', self.handle_request)
        except StreamClosedError:
            pass

    def handle_request(self, data):
        tmp_body = data[:-1]

        request = Request(address=self._address, Body=tmp_body)
        handler = urls.Handler_mapping.get(request.cmdid)

        handler_instance = handler()

        if isinstance(handler_instance,BaseHandler):
            try:
                handler_instance.process(request=request)
                self._stream.write(handler_instance.res)
            except Exception as e:
                print e.message

        self.read_request()

    def on_close(self):
        print "Server connection has been closed: ", self._address
        Connection.clients.remove(self)
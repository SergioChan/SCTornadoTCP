# coding=utf-8
__author__ = 'Yuheng Chen'

from Request.Request import Request
import Handler.Handler
from Logger.Logger import baseLogger
from Handler.Handler import BaseHandler
import urls
from tornado.iostream import StreamClosedError


class Connection(object):
    '''
    Connection is the base Class for server and client communication.
    Each connection between Server and client-server will be
    maintained by a `Connection` instance.
    Connection will read the request from IOStream and handle
    the requests.
    When a request handling is over, the Connection will automatically
    read the stream to get the next request.
    '''

    clients = set()

    def __init__(self, stream, address):
        Connection.clients.add(self)
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.on_close)
        self.read_request()
        baseLogger.info(msg=("New Connection from server: ",address))

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
                baseLogger.error(e.message)

        self.read_request()

    def on_close(self):
        baseLogger.info(msg=("Server connection has been closed: ", self._address))
        Connection.clients.remove(self)
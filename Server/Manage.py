# coding=utf-8
__author__ = 'Yuheng Chen'

from Logger.Logger import baseLogger
from tornado.ioloop import IOLoop
from Server.Server import BaseServer
from Settings import Settings
from tornado.netutil import bind_sockets
from tornado import process
import tornado


if __name__ == '__main__':
    baseLogger.info('Server is running...')
    server = BaseServer()

    if Settings.MULTI_PROCESS:
        server.bind(Settings.SERVER_PORT)
        server.start(0)
        for advanced_port in Settings.ADVANCED_SERVER_PORT:
            # bind more port if set
            tornado.process.fork_processes(0)
            sockets = bind_sockets(advanced_port)
            server.add_sockets(sockets)
    else:
        server.listen(Settings.SERVER_PORT)

    IOLoop.instance().start()
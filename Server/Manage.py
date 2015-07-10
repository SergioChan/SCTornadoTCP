__author__ = 'Yuheng Chen'

from tornado.ioloop  import IOLoop
from Server.Server import BaseServer
from Settings import Settings

if __name__ == '__main__':
    print "Server start ......"
    server = BaseServer()

    if Settings.MULTI_PROCESS:
        server.bind(Settings.SERVER_PORT)
        server.start(Settings.MULTI_PROCESS_NUMBER)
    else:
        server.listen(Settings.SERVER_PORT)

    IOLoop.instance().start()
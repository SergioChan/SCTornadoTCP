# coding=utf-8
__author__ = 'Yuheng Chen'

from Request import Request
import socket,errno

HOST = '127.0.0.1'
# The remote host
TEST_CMDID = 10000

PORT = 8889
# The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# If use Django or Tornado, you can keep this connection alive
# when the client-side server starts.

requestData = {"content":"Hello world!"}
request = Request(cmdid=TEST_CMDID,data=requestData)

# remember to catch IOError here in order to avoid or solve situations
# like server rebooting or internal network breakdown.
try:
    s.send(request.serialization())
except IOError as e:
        if e.errno == errno.EPIPE:
            # you should try to reconnect your socket connection here
            pass

result = s.recv(1024)
print 'result is', repr(result)
# You can choose wait for reply or not

# s.close()
# close() will be called when the client-side server closes.
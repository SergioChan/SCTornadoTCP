# tornado-TCP
A TCP Server and Client based on tornado

Written specifically for the server-to-server internal request.

## Connection

Any other server that was connected to this `tornado-TCP` server will be represented as a `client-server`. Each `client-server` will maintain a TCP connection with `tornado-TCP` server. If the connection will be used very frequently, it's better not to close it. Keeping an IOStream for the connection will make the communication in the server-side Local Area Network faster than typical HTTP request.

## Handler

Handler is the class type for processing the request object. You can sub-class your own Handler from BaseHandler to implement custom processing method. This is the sample of TestHandler:

```Python
@urls.handler(constant.TEST_CMDID)
class TestHandler(BaseHandler):

	def process(self,request):
        if isinstance(request, Request):
            print request.params
        else:
            raise TypeError
```
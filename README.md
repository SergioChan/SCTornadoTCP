# tornado-TCP
A TCP Server and Client based on `tornado`.

Written specifically for the server-to-server internal request.

## Current Version

Alpha Version 0.1.1

## License

MIT License

## Structure

The server can be represented by the Architecture diagram below:

![](https://raw.githubusercontent.com/SergioChan/tornado-TCP/master/tornado-TCP%20framework.png)  
## Connection

Any other server that was connected to this `tornado-TCP` server will be represented as a `client-server`. Each `client-server` will maintain a TCP connection with `tornado-TCP` server. If the connection will be used very frequently, it's better not to close it. Keeping an `IOStream` for the connection will make the communication in the server-side Local Area Network faster than typical HTTP request.

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

Notice the decorator `@urls.handler` which is used to add mapping between cmdId and Handler. The definition of this decorator is in the `urls.py`. Each custom Handler should decorated by this decorator.


## Request

`Request` is the basic object type in the `IOStream`. Each `Request` is delimited by a delimiter '\n'.`Request` is transported in a serialization mode, using normal json type.

To extend `Request`, define a subclass and there is no need to override anything.

`Request` has following parameters:

*  1.`address`: simple ip address combined with port number representing                 the request origin server.

*  2.`rawBody`: raw content of the request body

*  3.`cmdid`: command id defines in Command

*  4.`timestamp`: the date when request was sent

*  5.`params`: a dict that storage all the data it takes

## Server

You can start the server by command `Python Manage.py`. 

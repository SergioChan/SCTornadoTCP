# coding=utf-8
__author__ = 'Yuheng Chen'

import urls
import constant
from Request.Request import Request

class BaseHandler(object):
    pass

@urls.handler(constant.TEST_CMDID)
class TestHandler(BaseHandler):

    def process(self,request):
        if isinstance(request, Request):
            print request.params
        else:
            raise TypeError
# coding=utf-8
__author__ = 'Yuheng Chen'

import urls
import constant
from Request.Request import Request


@urls.handler(constant.TEST_CMDID)
class TestHandler(object):
    @staticmethod
    def process(request):
        if isinstance(request, Request):
            print request.params
        else:
            raise TypeError
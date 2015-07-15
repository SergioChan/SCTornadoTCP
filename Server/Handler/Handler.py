# coding=utf-8
__author__ = 'Yuheng Chen'

import urls
import constant
from Request.Request import Request
from Logger.Logger import testLogger

class BaseHandler(object):
    '''
    Base Class for Handler.
    You can custom your db connections or logger here.
    '''
    res = None
    logger = None

    def process(self,request):
        '''
        This method needs to be overridden.
        If not, raise `NotImplementedError`
        '''
        raise NotImplementedError

@urls.handler(constant.TEST_CMDID)
class TestHandler(BaseHandler):

    TAG = 'TestHandler'

    def process(self,request):
        if isinstance(request, Request):
            testLogger.info(request.params)
            self.res = "{'code':0}"
        else:
            raise TypeError
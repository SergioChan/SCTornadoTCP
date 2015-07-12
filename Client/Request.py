# coding=utf-8
__author__ = 'Yuheng Chen'

import time
import json

class Request(object):
    '''
    Client Request class.
    Init with command id and params data.
    '''

    cmdid = 0
    timestamp = 0
    params = dict()

    def __init__(self, cmdid, data):
        '''
        Ensure data is a dict type object.
        :param cmdid: Command id.
        :param data: data dict.
        :return: Request instance.
        '''
        if isinstance(data,dict):
            self.params = data
            self.cmdid = cmdid
            self.timestamp = int(time.time())

        else:
            raise TypeError

    def serialization(self):
        '''
        Serialized request object in order to send through IOStream.
        '''
        serialized_request = {}
        serialized_request['cmdid'] = self.cmdid
        serialized_request['timestamp'] = self.timestamp
        serialized_request['params'] = self.params

        result = json.dumps(serialized_request)+'\n'
        return result
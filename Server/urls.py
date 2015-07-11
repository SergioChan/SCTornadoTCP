# coding=utf-8
__author__ = 'Yuheng Chen'

Handler_mapping = {}


def handler(cmdid):
    '''
    decorator for custom Handler
    used to add mapping between cmdId and Handler
    '''

    def _module_dec(cls):
        Handler_mapping[cmdid] = cls
        return cls

    return _module_dec
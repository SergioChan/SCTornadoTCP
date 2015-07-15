#coding=utf-8
__author__ = 'Yuheng Chen'
import logging

class BaseLogger(object):
    '''
    Base Class for Logger.
    If you sub-class the BaseLogger, you can custom your logger_name,
    logger_level, logger_format_file, logger_format_console and logger_path.
    This provides developers ability to custom different loggers for
    different handlers.
    '''

    logger_name = 'BaseLogger'
    logger_level = logging.DEBUG
    logger_format_file = '%(asctime)s%(name)-12s%(levelname)-7s%(message)s'
    logger_format_console = '%(asctime)s %(name)-12s:%(levelname)-7s%(message)s'
    logger_path = 'debug.log'

    def __init__(self):
        '''
        Set file and console output logger
        '''

        logging.basicConfig(
                    level=self.logger_level,
                    format=self.logger_format_file,
                    datefmt='%m-%d %H:%M:%S',
                    filename=self.logger_path,
                    filemode='a+'
        )

        console = logging.StreamHandler()
        console.setLevel(self.logger_level)

        # set logger output formatter
        formatter = logging.Formatter(fmt=self.logger_format_console,datefmt='%m-%d %H:%M:%S')
        console.setFormatter(formatter)

        logging.getLogger(self.logger_name).addHandler(console)

        self.logger = logging.getLogger(self.logger_name)

    def info(self, msg):
        '''
        info
        '''

        self.logger.info(msg)

    def debug(self, msg):
        '''
        debug
        '''

        self.logger.debug(msg)

    def error(self, msg):
        '''
        error
        '''

        self.logger.error(msg)

    def warn(self, msg):
        '''
        warn
        '''

        self.logger.warn(msg)

    def exception(self, e):
        '''
        exception stack
        '''

        self.logger.exception(e)


class TestLogger(BaseLogger):
    '''
    Test Class for Logger.
    '''

    logger_name = 'TestLogger'
    logger_level = logging.DEBUG
    logger_format_file = '%(asctime)s%(name)-12s%(levelname)-7s%(message)s'
    logger_format_console = '%(asctime)s %(name)-12s:%(levelname)-7s%(message)s'
    logger_path = 'debug.log'

baseLogger = BaseLogger()
testLogger = TestLogger()
# -*- coding:utf-8 -*-

import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler

LOG_LEVEL = logging.DEBUG
file_logger_handler={}
stream_logger_handle={}

def get_file_logger(logger_name='root', log_path='mylog.log.', level=None):
    logger = logging.getLogger(logger_name)
    log_level = level if level else LOG_LEVEL
    logger.setLevel(log_level)
    handler = file_logger_handler.get(logger_name, None)
    if handler is None:
        handler = TimedRotatingFileHandler(log_path, when='midnight' ,interval=1, backupCount=30)
        file_logger_handler[logger_name] = handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(process)d -  %(thread)d - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_stream_logger(logger_name, level=None):
    logger = logging.getLogger(logger_name)
    log_level = level if level else LOG_LEVEL
    logger.setLevel(log_level)
    handler = stream_logger_handle.get(logger_name, None)
    if handler is None:
        handler = StreamHandler(sys.stdout)
        stream_logger_handle[logger_name] = handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(process)d -  %(thread)d - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


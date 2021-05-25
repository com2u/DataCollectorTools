import requests
from requests.api import request

BASE = 'http://127.0.0.1:3000'


class SVLog:
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    def getLogger(self, name):
        method = 'getLogger'
        requests.post(BASE, json={'method': method,
                                  'arguments': name}, verify=True)
        return logger()

    def Handler(self, level=NOTSET):
        method = 'Handler'
        requests.post(BASE, json={'method': method,
                                  'arguments': level}, verify=True)
        return Handler()

    def Logger(self, name, level=NOTSET):
        method = 'Logger'
        requests.post(BASE, json={'method': method,
                                  'arguments': [name, level]}, verify=True)
        return logger()

    def FileHandler(self, filename, mode='a', encoding=None, delay=False):
        method = 'FileHandler'
        requests.post(BASE, json={'method': method, 'arguments': [
                      filename, mode, encoding, delay]}, verify=True)
        return FileHandler()

    def StreamHandler(self, stream=None):
        method = 'StreamHandler'
        requests.post(BASE, json={'method': method,
                                  'arguments': stream}, verify=True)
        return StreamHandler()

    def Formatter(self, fmt=None, datefmt=None, style='%', validate=True):
        method = 'Formatter'
        requests.post(BASE, json={'method': method, 'arguments': [
                      fmt, datefmt, style, validate]}, verify=True)
        return Formatter()

    def Filter(self, name):
        method = 'Filter'
        requests.post(BASE, json={'method': method,
                                  'arguments': name}, verify=True)
        return Filter()

    def Filterer(self):
        method = 'Filterer'
        requests.post(BASE, json={'method': method}, verify=True)
        return Filterer()

    def Template(self, template: str):
        method = 'Template'
        requests.post(BASE, json={'method': method,
                                  'arguments': template}, verify=True)

    def addLevelName(self, level, levelname):
        method = 'addLevelName'
        args = [level, levelname]
        requests.post(BASE, json={'method': method,
                                  'arguments': args}, verify=True)

    def basicConfig(self, *args, **kwargs):
        method = 'basicConfig'
        requests.post(BASE, json={'method': method,
                                  'arguments': [args, kwargs]}, verify=True)

    def disable(self, level):
        method = 'disable'
        request.post(BASE, json={'method': method,
                                 'arguments': level}, verify=True)

    def debug(self, message, *args, **kwargs):
        method = 'debug'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def DEBUG(self):
        method = 'DEBUG'
        print("Hello")
        requests.post(BASE, json={'method': method}, verify=True)
        int = 10
        return int

    def CRITICAL(self):
        method = 'CRITICAL'
        int = 50
        return int

    def FATAL(self):
        method = 'FATAL'
        int = 50
        return int

    def ERROR(self):
        method = 'ERROR'
        int = 40
        return int

    def WARNING(self):
        method = 'WARNING'
        int = 30
        return 30

    def INFO(self):
        method = 'INFO'
        int = 20
        return int

    def info(self, message, *args, **kwargs):
        method = 'info'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def warning(self, message, *args, **kwargs):
        method = 'warning'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def error(self, message, *args, **kwargs):
        method = 'error'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def critical(self, message, *args, **kwargs):
        method = 'critical'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def log(self, level, message, *args, **kwargs):
        method = 'log'
        requests.post(BASE, json={'method': method, 'arguments': [
                      level, message, args, kwargs]}, verify=True)

    def exception(self, message, *args, exc_info=True, **kwargs):
        method = 'exception'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, exc_info, kwargs]}, verify=True)

    def shutdown(self):
        method = 'shutdown'
        requests.post(BASE, json={'method': method}, verify=True)

    def captureWarnings(self, capture: bool):
        method = 'captureWarnings'
        requests.post(BASE, json={'method': method,
                                  'arguments': capture}, verify=True)

    def lastResort(self):
        method = 'lastResort'
        requests.post(BASE, json={'method': method}, verify=True)

    def setLogRecordFactory(self, factory):
        #factory:(*args:Any, **kwargs:Any)
        method = 'setLogRecordFactory'
        requests.post(BASE, json={'method': method,
                                  'arguments': factory}, verify=True)

    def setLoggerClass(self):
        method = 'setLoggerClass'
        requests.post(BASE, json={'method': method}, verify=True)

    def makeLogRecord(self, dict):
        method = 'makeLogRecord'
        requests.post(BASE, json={'method': method,
                                  'arguments': dict}, verify=True)

    def getLogRecordFactory(self, *args, **kwargs):
        method = 'getLogRecordFactory'
        arguments = [args, kwargs]
        requests.post(BASE, json={'method': method,
                                  'arguments': arguments}, verify=True)

    def getLoggerClass(self):
        method = 'getLoggerClass'
        requests.post(BASE, json={'method': method}, verify=True)

    def LoggerAdapter(self, logger, dict):
        method = 'LoggerAdapter'
        requests.post(BASE, json={'method': method,
                                  'arguments': [logger, dict]}, verify=True)
        return LoggerAdapter()

    def LogRecord(self, name: str, level: int, pathname, lineno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
        method = 'LogRecord'
        requests.post(BASE, json={'method': method, 'arguments': [
                      name, level, pathname, lineno, msg, args, exc_info, func, sinfo, kwargs]}, verify=True)

    def warn(self, message, *args):
        method = 'warn'
        requests.post(BASE, json={'method': method,
                                  'arguments': [message, args]}, verify=True)

    def BASIC_FORMAT():
        method = 'BASIC_FORMAT'
        requests.post(BASE, json={'method': method}, verify=True)

    def raiseExceptions(self):
        pass

    class config:
        def fileConfig(fname, *args, **kwargs):
            method = 'config.fileConfig'
            requests.post(BASE, json={'method': method,
                                      'arguments': [fname, args, kwargs]}, verify=True)


class Filterer(object):
    def addFilter(self, filter):
        method = 'Filterer.addFilter'
        requests.post(BASE, json={'method': method,
                                  'arguments': filter}, verify=True)

    def removeFilter(self, filter):
        method = 'Filterer.removeFilter'
        requests.post(BASE, json={'method': method,
                                  'arguments': filter}, verify=True)

    def filter(self, record):
        method = 'Filterer.filter'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)


class Handler(object):
    def get_name(self):
        method = 'handler.get_name'
        requests.post(BASE, json={'method': method}, verify=True)

    def set_name(self, name):
        method = 'Handler.set_name'
        requests.post(BASE, json={'method': method}, verify=True)

    def createLock(self):
        method = 'Handler.createLock'
        requests.post(BASE, json={'method': method}, verify=True)

    def acquire(self):
        method = 'Handler.acquire'
        requests.post(BASE, json={'method': method}, verify=True)

    def release(self):
        method = 'Handler.release'
        requests.post(BASE, json={'method': method}, verify=True)

    def setLevel(self, level):
        print("Test1")
        method = 'Handler.setLevel'
        requests.post(BASE, json={'method': method,
                                  'arguments': level}, verify=True)

    def format(self, record):
        method = 'Handler.format'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def emit(self, record):
        method = 'Handler.emit'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def handle(self, record):
        method = 'Handler.handle'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def setFormatter(self, fmt):
        if isinstance(fmt, Handler):
            method = 'Handler.setFormatter'
            fmt = 'Formatter'
            requests.post(BASE, json={'method': method,
                                      'arguments': fmt}, verify=True)

        else:
            print("wrong input variable")
            method = 'Handler.removeHandler'
            requests.post(
                BASE, json={'method': method, 'arguments': 'Wrong input variable'}, verify=True)

    def flush(self):
        method = 'Handler.flush'
        requests.post(BASE, json={'method': method}, verify=True)

    def close(self):
        method = 'Handler.close'
        requests.post(BASE, json={'method': method}, verify=True)

    def handleError(self, record):
        method = 'Handler.handleError'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def addFilter(self, filter):
        method = 'Handler.addFilter'
        requests.post(BASE, json={'method': method,
                                  'arguments': filter}, verify=True)

    def removeFilter(self, filter):
        method = 'Handler.removeFilter'
        requests.post(BASE, json={'method': method,
                                  'arguments': filter}, verify=True)

    def filter(self, record):
        method = 'Handler.filter'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)


class logger(object):
    def warning(self, message, *args, **kwargs):
        method = 'logger.warning'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def debug(self, message, *args, **kwargs):
        method = 'logger.debug'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def info(self, message, *args, **kwargs):
        method = 'logger.info'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def error(self, message, *args, **kwargs):
        method = 'logger.error'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def critical(self, message, *args, **kwargs):
        method = 'logger.critical'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, kwargs]}, verify=True)

    def log(self, level, message, *args, **kwargs):
        method = 'logger.log'
        requests.post(BASE, json={'method': method, 'arguments': [
                      level, message, args, kwargs]}, verify=True)

    def setLevel(self, level):
        method = 'logger.setLevel'
        requests.post(BASE, json={'method': method,
                                  'arguments': level}, verify=True)

    def warn(self, msg, *args, **kwargs):
        method = 'logger.warn'
        requests.post(BASE, json={'method': method, 'arguments': [
                      msg, args, kwargs]}, verify=True)

    def propagate(self):
        method = 'propagate'
        requests.post(BASE, json={'method': method}, verify=True)

    def isEnabledFor(self, level):
        method = 'logger.isEnabledFor'
        requests.post(BASE, json={'method': method}, verify=True)

    def getEffectiveLevel(self):
        method = 'logger.getEffectiveLevel'
        requests.post(BASE, json={'method': method}, verify=True)

    def getChild(self, suffix):
        method = 'logger.getChild'
        requests.post(BASE, json={'method': method}, verify=True)

    def exception(message, *args, exc_info=True, **kwargs):
        method = 'logger.exception'
        requests.post(BASE, json={'method': method, 'arguments': [
                      message, args, exc_info, kwargs]}, verify=True)

    def callHandlers(self, record):
        method = 'logger.callHandlers'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def addHandler(self, hdlr):

        if isinstance(hdlr, FileHandler):
            method = 'logger.addHandler'
            hdlr = 'FileHandler'
            requests.post(BASE, json={'method': method,
                                      'arguments': hdlr}, verify=True)

        elif isinstance(hdlr, StreamHandler):
            method = 'logger.addHandler'
            hdlr = 'StreamHandler'
            requests.post(BASE, json={'method': method,
                                      'arguments': hdlr}, verify=True)

        elif isinstance(hdlr, Formatter):
            method = 'logger.addHandler'
            hdlr = 'Formatter'
            requests.post(BASE, json={'method': method,
                                      'arguments': hdlr}, verify=True)

        else:
            print("wrong input variable")
            method = 'logger.addHandler'
            requests.post(
                BASE, json={'method': method, 'arguments': 'Wrong input variable'}, verify=True)

    def removeHandler(self, hdlr):

        if isinstance(hdlr, FileHandler):
            method = 'logger.removeHandler'
            hdlr = 'FileHandler'
            requests.post(BASE, json={'method': method,
                                      'arguments': hdlr}, verify=True)

        elif isinstance(hdlr, StreamHandler):
            method = 'logger.removeHandler'
            hdlr = 'StreamHandler'
            requests.post(BASE, json={'method': method,
                                      'arguments': hdlr}, verify=True)

        elif isinstance(hdlr, Handler):
            method = 'logger.removeHandler'
            hdlr = 'Handler'
            requests.post(BASE, json={'method': method,
                                      'arguments': hdlr}, verify=True)

        elif isinstance(hdlr, Formatter):
            method = 'logger.removeHandler'
            hdlr = 'Formatter'
            requests.post(BASE, json={'method': method,
                                      'arguments': hdlr}, verify=True)

        else:
            print("wrong input variable")
            method = 'logger.removeHandler'
            requests.post(
                BASE, json={'method': method, 'arguments': 'Wrong input variable'}, verify=True)

    def findCaller(self, stack_info=False, stacklevel=1):
        method = 'logger.findCaller'
        requests.post(BASE, json={'method': method, 'arguments': [
                      stack_info, stacklevel]}, verify=True)

    def handle(self, record):
        method = 'logger.handle'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
        method = 'logger.makeRecord'
        requests.post(BASE, json={'method': method, 'arguments': [
                      name, level, fn, lno, msg, args, exc_info, func, extra, sinfo]}, verify=True)

    def hasHandlers(self):
        method = 'logger.hasHandlers'
        requests.post(BASE, json={'method': method}, verify=True)

    def addFilter(self, filter):
        method = 'logger.addFilter'
        requests.post(BASE, json={'method': method}, verify=True)

    def removeFilter(self, filter):
        method = 'logger.removeFilter'
        requests.post(BASE, json={'method': method}, verify=True)

    def filter(self, record):
        method = 'logger.filter'
        requests.post(BASE, json={'method': method}, verify=True)


class StreamHandler(object):

    def flush(self):
        method = 'StreamHandler.flush'
        requests.post(BASE, json={'method': method}, verify=True)

    def emit(self, record):
        method = 'StreamHandler.emit'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def setStream(self, stream):
        method = 'StreamHandler.setStream'
        requests.post(BASE, json={'method': method,
                                  'arguments': stream}, verify=True)

    def get_name(self):
        method = 'StreamHandler.get_name'
        requests.post(BASE, json={'method': method}, verify=True)

    def set_name(self, name):
        method = 'StreamHandler.set_name'
        requests.post(BASE, json={'method': method}, verify=True)

    def createLock(self):
        method = 'StreamHandler.createLock'
        requests.post(BASE, json={'method': method}, verify=True)

    def acquire(self):
        method = 'StreamHandler.acquire'
        requests.post(BASE, json={'method': method}, verify=True)

    def release(self):
        method = 'StreamHandler.release'
        requests.post(BASE, json={'method': method}, verify=True)

    def setLevel(self, level):
        method = 'StreamHandler.setLevel'
        requests.post(BASE, json={'method': method,
                                  'arguments': level}, verify=True)

    def format(self, record):
        method = 'StreamHandler.format'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def emit(self, record):
        method = 'StreamHandler.emit'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def handle(self, record):
        method = 'StreamHandler.handle'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def setFormatter(self, fmt):
        if isinstance(fmt, Formatter):
            method = 'StreamHandler.setFormatter'
            fmt = 'Formatter'
            requests.post(BASE, json={'method': method,
                                      'arguments': fmt}, verify=True)

        else:
            print("wrong input variable")
            method = 'StreamHandler.setFormatter'
            requests.post(
                BASE, json={'method': method, 'arguments': 'Wrong input variable'}, verify=True)

    def flush(self):
        method = 'StreamHandler.flush'
        requests.post(BASE, json={'method': method}, verify=True)

    def close(self):
        method = 'StreamHandler.close'
        requests.post(BASE, json={'method': method}, verify=True)

    def handleError(self, record):
        method = 'StreamHandler.handleError'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def addFilter(self, filter):
        method = 'StreamHandler.addFilter'
        requests.post(BASE, json={'method': method}, verify=True)

    def removeFilter(self, filter):
        method = 'StreamHandler.removeFilter'
        requests.post(BASE, json={'method': method}, verify=True)

    def filter(self, record):
        method = 'StreamHandler.filter'
        requests.post(BASE, json={'method': method}, verify=True)


class FileHandler(object):

    def close(self):
        method = 'FileHandler.close'
        requests.post(BASE, json={'method': method}, verify=True)

    def emit(self, record):
        method = 'FileHandler.emit'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def flush(self):
        method = 'FileHandler.flush'
        requests.post(BASE, json={'method': method}, verify=True)

    def emit(self, record):
        method = 'FileHandler.emit'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def setStream(self, stream):
        method = 'FileHandler.setStream'
        requests.post(BASE, json={'method': method,
                                  'arguments': stream}, verify=True)

    def get_name(self):
        method = 'FileHandler.get_name'
        requests.post(BASE, json={'method': method}, verify=True)

    def set_name(self, name):
        method = 'FileHandler.set_name'
        requests.post(BASE, json={'method': method}, verify=True)

    def createLock(self):
        method = 'FileHandler.createLock'
        requests.post(BASE, json={'method': method}, verify=True)

    def acquire(self):
        method = 'FileHandler.acquire'
        requests.post(BASE, json={'method': method}, verify=True)

    def release(self):
        method = 'FileHandler.release'
        requests.post(BASE, json={'method': method}, verify=True)

    def setLevel(self, level):
        method = 'FileHandler.setLevel'
        requests.post(BASE, json={'method': method,
                                  'arguments': level}, verify=True)

    def format(self, record):
        method = 'FileHandler.format'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def emit(self, record):
        method = 'FileHandler.emit'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def handle(self, record):
        method = 'FileHandler.handle'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def setFormatter(self, fmt):
        if isinstance(fmt, FileHandler):
            method = 'FileHandler.setFormatter'
            fmt = 'Formatter'
            requests.post(BASE, json={'method': method,
                                      'arguments': fmt}, verify=True)

        else:
            print("wrong input variable")
            method = 'FileHandler.setFormatter'
            requests.post(
                BASE, json={'method': method, 'arguments': 'Wrong input variable'}, verify=True)

    def flush(self):
        method = 'FileHandler.flush'
        requests.post(BASE, json={'method': method}, verify=True)

    def close(self):
        method = 'FileHandler.close'
        requests.post(BASE, json={'method': method}, verify=True)

    def handleError(self, record):
        method = 'FileHandler.handleError'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def addFilter(self, filter):
        method = 'FileHandler.addFilter'
        requests.post(BASE, json={'method': method}, verify=True)

    def removeFilter(self, filter):
        method = 'FileHandler.removeFilter'
        requests.post(BASE, json={'method': method}, verify=True)

    def filter(self, record):
        method = 'FileHandler.filter'
        requests.post(BASE, json={'method': method}, verify=True)


class Filter(object):
    def filter(self, record):
        method = 'Filter.filter'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)


class LogRecord(object):
    def getMessage(self):
        method = 'LogRecord.getMessage'
        requests.post(BASE, json={'method': method}, verify=True)


class LoggerAdapter(object):
    def process(self, msg, **kwargs):
        method = 'LoggerAdapter.process'
        requests.post(BASE, json={'method': method,
                                  'arguments': [msg, kwargs]}, verify=True)


class Formatter(object):
    def formatTime(self, record, datefmt=None):
        method = 'Formatter.formatTime'
        requests.post(BASE, json={'method': method, 'arguments': [
                      record, datefmt]}, verify=True)

    def formatException(self, exc_info):
        method = 'Formatter.formatException'
        requests.post(BASE, json={'method': method,
                                  'arguments': exc_info}, verify=True)

    def usesTime(self):
        method = 'Formatter.usesTime'
        requests.post(BASE, json={'method': method}, verify=True)

    def formatMessage(self, record):
        method = 'Formatter.formatMessage'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)

    def formatStack(self, stack_info):
        method = 'Formatter.formatStack'
        requests.post(BASE, json={'method': method,
                                  'arguments': stack_info}, verify=True)

    def format(self, record):
        method = 'Formatter.format'
        requests.post(BASE, json={'method': method,
                                  'arguments': record}, verify=True)


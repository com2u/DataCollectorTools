import logging
from flask_restful import Api, Resource
from flask import Flask, request
from importlib import reload
import logging.config

class LoggingServer(Resource):

    logger = []

    @classmethod
    def post(self):

        values = request.json
        method = values['method']

        if method == 'getLogger':
            arguments = values['arguments']
            LoggingServer.getLogger(self, arguments)

        elif method == 'Handler':
            arguments = values['arguments']
            LoggingServer.Handler(self, arguments)

        elif method == 'Logger':
            arguments = values['arguments']
            LoggingServer.Logger(self, arguments)

        elif method == 'FileHandler':
            arguments = values['arguments']
            LoggingServer.FileHandler(self, arguments)

        elif method == 'StreamHandler':
            arguments = values['arguments']
            LoggingServer.StreamHandler(self, arguments)

        elif method == 'Formatter':
            arguments = values['arguments']
            LoggingServer.Formatter(self, arguments)

        elif method == 'Filter':
            arguments = values['arguments']
            LoggingServer.Filter(self, arguments)

        elif method == 'Filterer':
            LoggingServer.Filterer(self)

        elif method == 'Template':
            arguments = values['arguments']
            LoggingServer.Template(self, arguments)

        elif method == 'warning':
            arguments = values['arguments']
            LoggingServer.warning(self, arguments)

        elif method == 'debug':
            arguments = values['arguments']
            LoggingServer.debug(self, arguments)

        elif method == 'error':
            arguments = values['arguments']
            LoggingServer.error(self, arguments)

        elif method == 'critical':
            arguments = values['arguments']
            LoggingServer.critical(self, arguments)

        elif method == 'info':
            arguments = values['arguments']
            LoggingServer.info(self, arguments)

        elif method == 'log':
            arguments = values['arguments']
            LoggingServer.log(self, arguments)

        elif method == 'getLevelName':
            arguments = values['arguments']
            LoggingServer.getLevelName(self, arguments)

        elif method == 'addLevelName':
            arguments = values['arguments']
            LoggingServer.addLevelName(self, arguments)

        elif method == 'exception':
            arguments = values['arguments']
            LoggingServer.exception(self, arguments)

        elif method == 'disable':
            arguments = values['arguments']
            LoggingServer.disable(self, arguments)

        elif method == 'shutdown':
            LoggingServer.shutdown(self)

        elif method == 'captureWarnings':
            arguments = values['arguments']
            LoggingServer.captureWarnings(self, arguments)

        elif method == 'lastResort':
            LoggingServer.lastResort(self)

        elif method == 'setLogRecordFactory':
            arguments = values['arguments']
            LoggingServer.setLogRecordFactory(self, arguments)

        elif method == 'setLoggerClass':
            LoggingServer.setLoggerClass(self)

        elif method == 'basicConfig':
            arguments = values['arguments']
            LoggingServer.basicConfig(self, arguments)

        elif method == 'config.fileConfig':
            arguments = values['arguments']
            LoggingServer.configfileConfig(self, arguments)

        elif method == 'makeLogRecord':
            arguments = values['arguments']
            LoggingServer.makeLogRecord(self, arguments)

        elif method == 'getLogRecordFactory':
            arguments = values['arguments']
            LoggingServer.getLogRecordFactory(self, arguments)

        elif method == 'getLoggerClass':
            LoggingServer.getLoggerClass(self)

        elif method == 'LoggerAdapter':
            arguments = values['arguments']
            LoggingServer.LoggerAdapter(self, arguments)

        elif method == 'warn':
            arguments = values['arguments']
            LoggingServer.warn(self, arguments)

        elif method == 'DEBUG':
            LoggingServer.DEBUG(self)

        elif method == 'CRITICAL':
            pass

        elif method == 'FATAL':
            pass

        elif method == 'ERROR':
            pass

        elif method == 'WARNING':
            pass

        elif method == 'INFO':
            pass

        elif method == 'BASIC_FORMAT':
            LoggingServer.BASIC_FORMAT(self)

        elif method == 'LogRecord':
            arguments = values['arguments']
            LoggingServer.LogRecord(self, arguments)

        ###############################################################

        elif method == 'Filterer.addFilter':
            arguments = values['arguments']
            LoggingServer.FiltereraddFilter(self, arguments)

        elif method == 'Filterer.removeFilter':
            arguments = values['arguments']
            LoggingServer.FiltererremoveFilter(self, arguments)

        elif method == 'Filterer.filter':
            arguments = values['arguments']
            LoggingServer.Filtererfilter(self, arguments)

        ##############################################################

        elif method == 'handler.get_name':
            LoggingServer.Handlerget_name(self)

        elif method == 'Handler.set_name':
            arguments = values['arguments']
            LoggingServer.Handlerset_name(self, arguments)

        elif method == 'Handler.createLock':
            LoggingServer.HandlercreateLock(self)

        elif method == 'Handler.acquire':
            LoggingServer.Handleracquire(self)

        elif method == 'Handler.release':
            LoggingServer.Handlerrelease(self)

        elif method == 'Handler.setLevel':
            arguments = values['arguments']
            LoggingServer.HandlersetLevel(self, arguments)

        elif method == 'Handler.format':
            arguments = values['arguments']
            LoggingServer.Handlerformat(self, arguments)

        elif method == 'Handler.emit':
            arguments = values['arguments']
            LoggingServer.Handleremit(self, arguments)

        elif method == 'Handler.handle':
            arguments = values['arguments']
            LoggingServer.Handlerhandle(self, arguments)

        elif method == 'Handler.setFormatter':
            arguments = values['arguments']
            LoggingServer.HandlersetFormatter(self, arguments)

        elif method == 'Handler.flush':
            LoggingServer.Handlerflush(self)

        elif method == 'Handler.close':
            LoggingServer.Handlerclose(self)

        elif method == 'Handler.handleError':
            arguments = values['arguments']
            LoggingServer.HandlerhandleError(self, arguments)

        elif method == 'Handler.addFilter':
            arguments = values['arguments']
            LoggingServer.HandleraddFilter(self, arguments)

        elif method == 'Handler.removeFilter':
            arguments = values['arguments']
            LoggingServer.HandlerremoveFilter(self, arguments)

        elif method == 'Handler.filter':
            arguments = values['arguments']
            LoggingServer.Handlerfilter(self, arguments)

        ######################################################

        elif method == 'logger.warning':
            arguments = values['arguments']
            LoggingServer.loggerwarning(self, arguments)

        elif method == 'logger.debug':
            arguments = values['arguments']
            LoggingServer.loggerdebug(self, arguments)

        elif method == 'logger.info':
            arguments = values['arguments']
            LoggingServer.loggerinfo(self, arguments)

        elif method == 'logger.error':
            arguments = values['arguments']
            LoggingServer.loggererror(self, arguments)

        elif method == 'logger.critical':
            arguments = values['arguments']
            LoggingServer.loggercritical(self, arguments)

        elif method == 'logger.log':
            arguments = values['arguments']
            LoggingServer.loggerlog(self, arguments)

        elif method == 'logger.setLevel':
            arguments = values['arguments']
            LoggingServer.loggersetLevel(self, arguments)

        elif method == 'logger.warn':
            arguments = values['arguments']
            LoggingServer.loggerwarn(self, arguments)

        elif method == 'logger.propagate':
            LoggingServer.loggerpropagate(self)

        elif method == 'logger.isEnabledFor':
            arguments = values['arguments']
            LoggingServer.loggerlevel(self, arguments)

        elif method == 'logger.getEffectiveLevel':
            LoggingServer.loggergetEffectiveLevel(self)

        elif method == 'logger.getChild':
            arguments = values['arguments']
            LoggingServer.loggergetChild(self, arguments)

        elif method == 'logger.exception':
            arguments = values['arguments']
            LoggingServer.loggerexception(self, arguments)

        elif method == 'logger.callHandlers':
            arguments = values['arguments']
            LoggingServer.loggercallHandlers(self, arguments)

        elif method == 'logger.addHandler':
            arguments = values['arguments']
            LoggingServer.loggeraddHandler(self, arguments)

        elif method == 'logger.removeHandler':
            arguments = values['arguments']
            LoggingServer.loggerremoveHandler(self, arguments)

        elif method == 'logger.findCaller':
            arguments = values['arguments']
            LoggingServer.loggerfindCaller(self, arguments)

        elif method == 'logger.handle':
            arguments = values['arguments']
            LoggingServer.loggerhandle(self, arguments)

        elif method == 'logger.makeRecord':
            arguments = values['arguments']
            LoggingServer.loggermakeRecord(self, arguments)

        elif method == 'logger.hasHandlers':
            LoggingServer.loggerhasHandlers(self)

        elif method == 'logger.addFilter':
            arguments = values['arguments']
            LoggingServer.loggeraddFilter(self, arguments)

        elif method == 'logger.removeFilter':
            arguments = values['arguments']
            LoggingServer.loggerremoveFilter(self, arguments)

        elif method == 'logger.filter':
            arguments = values['arguments']
            LoggingServer.loggerfilter(self, arguments)

        ######################################################

        elif method == 'StreamHandler.flush':
            LoggingServer.StreamHandlerflush(self)

        elif method == 'StreamHandler.emit':
            arguments = values['arguments']
            LoggingServer.StreamHandleremit(self, arguments)

        elif method == 'StreamHandler.setStream':
            arguments = values['arguments']
            LoggingServer.StreamHandlersetStream(self, arguments)

        elif method == 'StreamHandler.get_name':
            LoggingServer.StreamHandlerget_name(self)

        elif method == 'StreamHandler.set_name':
            arguments = values['arguments']
            LoggingServer.StreamHandlerset_name(self, arguments)

        elif method == 'StreamHandler.createLock':
            LoggingServer.StreamHandlercreateLock(self)

        elif method == 'StreamHandler.acquire':
            LoggingServer.StreamHandleracquire(self)

        elif method == 'StreamHandler.release':
            LoggingServer.StreamHandlerrelease(self)

        elif method == 'StreamHandler.setLevel':
            arguments = values['arguments']
            LoggingServer.StreamHandlerset_name(self, arguments)

        elif method == 'StreamHandler.format':
            arguments = values['arguments']
            LoggingServer.StreamHandlerformat(self, arguments)

        elif method == 'StreamHandler.handle':
            arguments = values['arguments']
            LoggingServer.StreamHandlerhandle(self, arguments)

        elif method == 'StreamHandler.setFormatter':
            arguments = values['arguments']
            LoggingServer.StreamHandlersetFormatter(self, arguments)

        elif method == 'StreamHandler.close':
            LoggingServer.StreamHandlerclose(self)

        elif method == 'StreamHandler.handleError':
            arguments = values['arguments']
            LoggingServer.StreamHandlerhandleError(self, arguments)

        elif method == 'StreamHandler.addFilter':
            arguments = values['arguments']
            LoggingServer.StreamHandleraddFilter(self, arguments)

        elif method == 'StreamHandler.removeFilter':
            arguments = values['arguments']
            LoggingServer.StreamHandlerremoveFilter(self, arguments)

        elif method == 'StreamHandler.filter':
            arguments = values['arguments']
            LoggingServer.StreamHandlerfilter(self, arguments)

        ######################################################

        elif method == 'FileHandler.close':
            LoggingServer.FileHandlerclose(self)

        elif method == 'FileHandler.emit':
            arguments = values['arguments']
            LoggingServer.FileHandleremit(self, arguments)

        elif method == 'FileHandler.flush':
            LoggingServer.FileHandlerflush(self)

        elif method == 'FileHandler.setStream':
            arguments = values['arguments']
            LoggingServer.FileHandlersetStream(self, arguments)

        elif method == 'FileHandler.get_name':
            LoggingServer.FileHandlerget_name(self)

        elif method == 'FileHandler.set_name':
            arguments = values['arguments']
            LoggingServer.FileHandlerset_name(self, arguments)

        elif method == 'FileHandler.createLock':
            LoggingServer.FileHandlercreateLock(self)

        elif method == 'FileHandler.acquire':
            LoggingServer.FileHandleracquire(self)

        elif method == 'FileHandler.release':
            LoggingServer.FileHandlerrelease(self)

        elif method == 'FileHandler.setLevel':
            arguments = values['arguments']
            LoggingServer.FileHandlersetLevel(self, arguments)

        elif method == 'FileHandler.format':
            arguments = values['arguments']
            LoggingServer.FileHandlerformat(self, arguments)

        elif method == 'FileHandler.handle':
            arguments = values['arguments']
            LoggingServer.FileHandlerhandle(self, arguments)

        elif method == 'FileHandler.setFormatter':
            arguments = values['arguments']
            LoggingServer.FileHandlersetFormatter(self, arguments)

        elif method == 'FileHandler.handleError':
            arguments = values['arguments']
            LoggingServer.FileHandlerhandleError(self, arguments)

        elif method == 'FileHandler.addFilter':
            arguments = values['arguments']
            LoggingServer.FileHandleraddFilter(self, arguments)

        elif method == 'FileHandler.removeFilter':
            arguments = values['arguments']
            LoggingServer.FileHandlerremoveFilter(self, arguments)

        elif method == 'FileHandler.filter':
            arguments = values['arguments']
            LoggingServer.FileHandlerfilter(self, arguments)

        #####################################################

        elif method == 'LogRecord.getMessage':
            pass

        #####################################################

        elif method == 'LoggerAdapter.process':
            arguments = values['arguments']
            LoggingServer.LoggerAdapterprocess(self, arguments)
            
        #####################################################

        elif method == 'Formatter.formatTime':
            arguments = values['arguments']
            LoggingServer.FormatterformatTime(self, arguments)

        elif method == 'Formatter.formatException':
            arguments = values['arguments']
            LoggingServer.FormatterformatException(self, arguments)

        elif method == 'Formatter.usesTime':
            LoggingServer.FormatterusesTime(self)

        elif method == 'Formatter.formatMessage':
            arguments = values['arguments']
            LoggingServer.FormatterformatMessage(self, arguments)

        elif method == 'Formatter.formatStack':
            arguments = values['arguments']
            LoggingServer.FormatterformatStack(self, arguments)

        elif method == 'Formatter.format':
            arguments = values['arguments']
            LoggingServer.Formatterformat(self, arguments)

    ################################################################

    def getLogger(self, arguments):
        name = arguments
        self.h1_getLogger = logging.getLogger(name)
        print(self.h1_getLogger)
        #self.h1_getLogger.handlers.clear()
        return self.h1_getLogger

    def Handler(self, arguments):
        level = arguments
        self.h2_handler = logging.Handler(level)
        return self.h2_handler

    def Logger(self, arguments):
        name = arguments[0]
        level = arguments[1]
        self.h1_getLogger = logging.Logger(name, level)
        return self.h1_getLogger

    def FileHandler(self, arguments):
        filename = arguments[0]
        mode = arguments[1]
        encoding = arguments[2]
        delay = arguments[3]
        self.h4_FileHandler = logging.FileHandler(filename, mode, encoding, delay)
        return self.h4_FileHandler

    def StreamHandler(self, arguments):
        stream = arguments
        self.h5_StreamHandler = logging.StreamHandler(stream)
        return self.h5_StreamHandler

    def Formatter(self, arguments):
        fmt = arguments[0]
        datefmt = arguments[1]
        style = arguments[2]
        validate = arguments[3]
        self.h6_Formatter = logging.Formatter(fmt, datefmt, style, validate)
        return self.h6_Formatter

    def Filter(self, arguments):
        name = arguments
        self.h7_Filter = logging.Filter(name)
        return self.h7_Filter

    def Filterer(self):
        self.h8_Filterer = logging.Filterer()
        return self.h8_Filterer

    def Template(self, arguments):
        template = arguments
        logging.Template(template)

    def addLevelName(self, arguments):
        level = arguments[0]
        levelname = arguments[1]
        logging.addLevelName(level, levelname)

    def basicConfig(self, arguments):
        args = arguments[0]
        kwargs = arguments[1]
        logging.shutdown()
        reload(logging)
        logging.basicConfig(*args,**kwargs)

    def configfileConfig(self, arguments):
        logging.shutdown()
        reload(logging)
        fname = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.config.fileConfig(fname, *args, **kwargs)


    def disable(self, arguments):
        level = arguments
        logging.disable(level)

    def debug(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.debug(message, *args, **kwargs)

    def info(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.info(message, *args, **kwargs)

    def warning(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.warning(message, *args, **kwargs)

    def error(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.error(message, *args, **kwargs)

    def critical(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.critical(message, *args, **kwargs)

    def log(self, arguments):
        level = arguments[0]
        message = arguments[1]
        args = arguments[2]
        kwargs = arguments[3]
        logging.log(level, message, *args, **kwargs)

    def exception(self, arguments):
        message = arguments[0]
        args = arguments[1]
        exc_info = arguments[2]
        kwargs = arguments[3]
        logging.exception(message, *args, exc_info, **kwargs)

    def DEBUG(self):
        logging.DEBUG

    def WARNING(self):
        logging.WARNING

    def ERROR(self):
        logging.ERROR

    def INFO(self):
        logging.INFO

    def CRITICAL(self):
        logging.CRITICAL

    def FATAL(self):
        logging.FATAL

    def shutdown(self):
        logging.shutdown

    def getLevelName(self, arguments):
        level = arguments
        logging.getLevelName(level)

    def captureWarnings(self, arguments):
        capture = arguments
        logging.captureWarnings(capture=capture)

    def lastResort(self):
        logging.lastResort

    def setLogRecordFactory(self, arguments):
        factory = arguments
        logging.setLogRecordFactory(factory)

    def setLoggerClass(self):
        logging.setLoggerClass

    def makeLogRecord(self, arguments):
        dict = arguments
        logging.makeLogRecord(dict)

    def getLogRecordFactory(self, arguments):
        args = arguments[0]
        kwargs = arguments[1]
        logging.getLogRecordFactory(*args, **kwargs)

    def getLoggerClass(self):
        logging.getLoggerClass()

    def LoggerAdapter(self, arguments):
        logger = arguments[0]
        dict = arguments[1]
        h9_LoggerAdapter = None
        h9_LoggerAdapter = logging.LoggerAdapter(logger, dict)
        return h9_LoggerAdapter

    def LogRecord(self, arguments):
        logging.LogRecord(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4],
                          arguments[5], arguments[6], arguments[7], arguments[8], **(arguments[9]))

    def warn(self, arguments):
        message = arguments[0]
        args = arguments[0]
        logging.warn(msg=message, *args)

    def BASIC_FORMAT(self):
        print("hello")
        logging.BASIC_FORMAT

    def raiseExceptions(self):
        pass

##############################################################

    def loggerwarning(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warning(message, *args, **kwargs)

    def loggerdebug(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.debug(message, *args, **kwargs)

    def loggerinfo(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.info(message, *args, **kwargs)

    def loggererror(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.error(message, *args, **kwargs)

    def loggercritical(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.critical(message, *args, **kwargs)

    def log(self, arguments):
        level = arguments[0]
        message = arguments[1]
        args = arguments[2]
        kwargs = arguments[3]
        self.h1_getLogger.log(level, message, *args, **kwargs)

    def loggersetLevel(self, arguments):
        level = arguments
        self.h1_getLogger.setLevel(level)

    def loggerwarn(self, arguments):
        msg = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warn(msg, *args, **kwargs)

    def loggerpropagate(self):
        self.h1_getLogger.propagate()

    def loggerisEnabledFor(self, arguments):
        level = arguments
        self.h1_getLogger.level(level)

    def loggergetEffectiveLevel(self):
        self.h1_getLogger.getEffectiveLevel()

    def loggergetChild(self, arguments):
        suffix = arguments
        self.h1_getLogger.getChild(suffix)

    def loggerexception(self, arguments):
        message = arguments[0]
        args = arguments[1]
        exc_info = arguments[2]
        kwargs = arguments[3]
        self.h1_getLogger.log(message, *args, exc_info, **kwargs)

    def loggercallHandlers(self, arguments):
        record = arguments
        self.h1_getLogger.callHandlers(record)

    def loggeraddHandler(self, arguments):

        hdlr = arguments
        if hdlr == 'FileHandler':
            hdlr = self.h4_FileHandler
            self.h1_getLogger.addHandler(hdlr)

            '''
            for h in list(self.h1_getLogger.handlers):
                if type(self.hdlr) == type(h):
                    print("hit")
                    self.h1_getLogger.removeHandler(hdlr)
                    print(self.h1_getLogger.handlers)
                else:
                    print("no hit")

            print(self.h1_getLogger.handlers)
            '''

        elif hdlr == 'StreamHandler':
            hdlr = self.h5_StreamHandler
            self.h1_getLogger.addHandler(hdlr)

        elif hdlr == 'Handler':
            hdlr = self.h2_handler
            self.h1_getLogger.addHandler(hdlr)

        elif hdlr == 'Formatter':
            hdlr = self.h6_Formatter
            self.h1_getLogger.addHandler(hdlr)

        else:
            message = hdlr
            print(message)

    def loggerremoveHandler(self, arguments):
        hdlr = arguments

        if hdlr == 'FileHandler':
            hdlr = self.h4_FileHandler
            self.h1_getLogger.removeHandler(hdlr)

        elif hdlr == 'StreamHandler':
            hdlr = self.h5_StreamHandler
            self.h1_getLogger.removeHandler(hdlr)

        elif hdlr == 'Handler':
            hdlr = self.h2_handler
            self.h1_getLogger.removeHandler(hdlr)

        elif hdlr == 'Formatter':
            hdlr = self.h6_Formatter
            self.h1_getLogger.removeHandler(hdlr)

        else:
            message = hdlr
            print(message)

    def loggerfindCaller(self, arguments):
        stack_info = arguments[0]
        stacklevel = arguments[1]
        self.h1_getLogger.findCaller(stack_info, stacklevel)

    def loggerhandle(self, arguments):
        record = arguments
        self.h1_getLogger.handle(record)

    def loggermakeRecord(self, arguments):
        name = arguments[0]
        level = arguments[1]
        fn = arguments[2]
        lno = arguments[3]
        msg = arguments[4]
        args = arguments[5]
        exc_info = arguments[6]
        func = arguments[7]
        extra = arguments[8]
        sinfo = arguments[9]
        self.h1_getLogger.makeRecord(
            name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)

    def loggerhasHandlers(self):
        self.h1_getLogger.hasHandlers()

    def loggeraddFilter(self, arguments):
        filter = arguments
        self.h1_getLogger.addfilter(filter)

    def loggerremoveFilter(self, arguments):
        filter = arguments
        self.h1_getLogger.removeFilter(filter)

    def loggerfilter(self, arguments):
        record = arguments
        self.h1_getLogger.filter(record)

##############################################################

    def FiltereraddFilter(self, arguments):
        filter = arguments
        self.h8_Filterer.addFilter(filter)

    def FiltererremoveFilter(self, arguments):
        filter = arguments
        self.h8_Filterer.removeFilter(filter)

    def Filtererfilter(self, arguments):
        record = arguments
        self.h8_Filterer.filter(record)

##############################################################

    def Handlerget_name(self):
        self.h2_handler.get_name()

    def Handlerset_name(self, arguments):
        name = arguments
        self.h2_handler.set_name(name)

    def HandlercreateLock(self):
        self.h2_handler.createLock()

    def Handleracquire(self):
        self.h2_handler.acquire()

    def Handlerrelease(self):
        self.h2_handler.release()

    def HandlersetLevel(self, arguments):
        level = arguments
        self.h2_handler.setLevel(level)

    def Handlerformat(self, arguments):
        record = arguments
        self.h2_handler.format(record)

    def Handleremit(self, arguments):
        record = arguments
        self.h2_handler.emit(record)

    def Handlerhandle(self, arguments):
        record = arguments
        self.h2_handler.handle(record)

    def HandlersetFormatter(self, arguments):
        fmt = arguments

        if fmt == 'Formatter':
            hdlr = self.h6_Formatter
            self.h1_getLogger.removeHandler(hdlr)

        else:
            message = fmt
            print(message)

    def Handlerflush(self):
        self.h2_handler.flush()

    def Handlerclose(self):
        self.h2_handler.close()

    def HandlerhandleError(self, arguments):
        record = arguments
        self.h2_handler.handleError(record)

    def HandleraddFilter(self, arguments):
        filter = arguments
        self.h2_handler.addfilter(filter)

    def HandlerremoveFilter(self, arguments):
        filter = arguments
        self.h2_handler.removeFilter(filter)

    def Handlerfilter(self, arguments):
        record = arguments
        self.h2_handler.filter(record)

##############################################################

    def StreamHandlerflush(self):
        self.h5_StreamHandler.flush()

    def StreamHandleremit(self, arguments):
        record = arguments
        self.h5_StreamHandler.emit(record)

    def StreamHandlersetStream(self, arguments):
        stream = arguments
        self.h5_StreamHandler.setStream(stream)

    def StreamHandlerget_name(self):
        self.h5_StreamHandler.get_name()

    def StreamHandlerset_name(self, arguments):
        name = arguments
        self.h5_StreamHandler.set_name(name)

    def StreamHandlercreateLock(self):
        self.h5_StreamHandler.createLock()

    def StreamHandleracquire(self):
        self.h5_StreamHandler.acquire()

    def StreamHandlerrelease(self):
        self.h5_StreamHandler.release()

    def StreamHandlersetLevel(self, arguments):
        level = arguments
        self.h5_StreamHandler.setLevel(level)

    def StreamHandlerformat(self, arguments):
        record = arguments
        self.h5_StreamHandler.format(record)

    def StreamHandlerhandle(self, arguments):
        record = arguments
        self.h5_StreamHandler.handle(record)

    def StreamHandlersetFormatter(self, arguments):
        fmt = arguments

        if fmt == 'Formatter':
            fmt = self.h6_Formatter
            self.h5_StreamHandler.setFormatter(fmt)

        else:
            message = fmt
            print(message)

    def StreamHandlerclose(self):
        self.h5_StreamHandler.close()

    def StreamHandlerhandleError(self, arguments):
        record = arguments
        self.h5_StreamHandler.handleError(record)

    def StreamHandleraddFilter(self, arguments):
        filter = arguments
        self.h5_StreamHandler.addfilter(filter)

    def StreamHandlerremoveFilter(self, arguments):
        filter = arguments
        self.h5_StreamHandler.removeFilter(filter)

    def StreamHandlerfilter(self, arguments):
        record = arguments
        self.h5_StreamHandler.filter(record)


##############################################################

    def FileHandlerclose(self):
        self.h4_FileHandler.close()

    def FileHandleremit(self, arguments):
        record = arguments
        self.h4_FileHandler.emit(record)

    def FileHandlerflush(self):
        self.h4_FileHandler.flush()

    def FileHandleremit(self, arguments):
        record = arguments
        self.h4_FileHandler.emit(record)

    def FileHandlersetStream(self, arguments):
        stream = arguments
        self.h4_FileHandler.setStream(stream)

    def FileHandlerget_name(self):
        self.h4_FileHandler.get_name()

    def FileHandlerset_name(self, arguments):
        name = arguments
        self.h4_FileHandler.set_name(name)

    def FileHandlercreateLock(self):
        self.h4_FileHandler.createLock()

    def FileHandleracquire(self):
        self.h4_FileHandler.acquire()

    def FileHandlerrelease(self):
        self.h4_FileHandler.release()

    def FileHandlersetLevel(self, arguments):
        level = arguments
        self.h4_FileHandler.setLevel(level)

    def FileHandlerformat(self, arguments):
        record = arguments
        self.h4_FileHandler.format(record)

    def FileHandlerhandle(self, arguments):
        record = arguments
        self.h4_FileHandler.handle(record)

    def FileHandlersetFormatter(self, arguments):
        fmt = arguments

        if fmt == 'Formatter':
            fmt = self.h6_Formatter
            self.h4_FileHandler.setFormatter(fmt)

        else:
            message = fmt
            print(message)

    def FileHandlerhandleError(self, arguments):
        record = arguments
        self.h4_FileHandler.handleError(record)

    def FileHandleraddFilter(self, arguments):
        filter = arguments
        self.h4_FileHandler.addFilter(filter)

    def FileHandlerremoveFilter(self, arguments):
        filter = arguments
        self.h4_FileHandler.removeFilter(filter)

    def FileHandlerfilter(self, arguments):
        record = arguments
        self.h4_FileHandler.filter(record)


##############################################################

    def Filterfilter(self, arguments):
        record = arguments
        self.h7_Filter.filter(record)

##############################################################

    def LogRecordgetMessage(self):
        pass

##############################################################

    def LoggerAdapterprocess(self, arguments):
        msg = arguments[0]
        kwargs = arguments[1]
        self.h9_LoggerAdapter.process(msg, **kwargs)

##############################################################

    def FormatterformatTime(self, arguments):
        record = arguments[0]
        datefmt = arguments[1]
        self.h6_Formatter.formatTime(record, datefmt)

    def FormatterformatException(self, arguments):
        exc_info = arguments
        self.h6_Formatter.formatException(exc_info)

    def FormatterusesTime(self):
        self.h6_Formatter.usesTime()

    def FormatterformatMessage(self, arguments):
        record = arguments
        self.h6_Formatter.formatMessage(record)

    def FormatterformatStack(self, arguments):
        stack_info = arguments
        self.h6_Formatter.formatStack(stack_info)

    def Formatterformat(self, arguments):
        record = arguments
        self.h6_Formatter.format(record)


from logzero import logger
import logzero
import logging
import os
import uuid


class Mylog():
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\Log\\"

    def __init__(self, name):
        _formater = logging.Formatter('%(asctime)-15s : %(message)s')
        self.logzero = logzero
        self.logzero.logfile(Mylog.path + str(uuid.uuid1()) + "_" + name + ".log", formatter=_formater,
                             maxBytes=10000000, backupCount=6)

    def debug(self, message):
        logger.debug(message)

    def info(self, message):
        logger.info(message)

    def warn(self, message):
        logger.warn(message)

    def error(self, message):
        logger.error(message)


if __name__ == '__main__':
    My = Mylog(__name__)
    My.debug("debug test")

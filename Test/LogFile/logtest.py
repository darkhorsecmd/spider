from logzero import logger
import logzero
import logging
import os

logzero.loglevel(logging.WARN)
logzero.logfile(__name__+".log")
logger.error("this is error")
logger.debug("this is debug")

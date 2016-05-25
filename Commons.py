import logging

class Commons:
    LOGGER_FORMAT = "%(asctime)s %(name)s:%(levelname)s %(pathname)s:%(lineno)s - %(message)s"
    LOGGER_LEVEL = logging.INFO
    LOG_PATH = 'logs/run.log'

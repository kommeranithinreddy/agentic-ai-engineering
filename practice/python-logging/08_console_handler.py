import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler() #For console messages
console_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)

class AllowOnlyDebug(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG

console_handler.addFilter(AllowOnlyDebug())
logger.debug("Application Started")
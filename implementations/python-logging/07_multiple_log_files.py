import logging

class DebugOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_handler = logging.FileHandler("debug.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.addFilter(DebugOnlyFilter())

app_handler = logging.FileHandler("app.log")
app_handler.setLevel(logging.INFO)

logger.addHandler(debug_handler)
logger.addHandler(app_handler)

logger.debug("This is debug message")
logger.info("Application Started")
logger.warning("This is Warning Message")
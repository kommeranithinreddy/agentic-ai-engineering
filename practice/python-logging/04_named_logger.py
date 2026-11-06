import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(name)s -  %(levelname)s - %(message)s",
    filename = "app.log"
)

logger = logging.getLogger(__name__)

logger.warning("This is Warning Message")
logger.error("This is Error Message")
logger.critical("This is Critical Message")
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is Debug Message")
logging.info("This is Info Message")
logging.warning("This is Warning Message")
logging.error("This is Error Message")
logging.critical("This is Critical Message")
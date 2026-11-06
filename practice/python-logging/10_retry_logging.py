import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s :: %(name)s :: %(levelname)s  :: %(message)s",
    filename = "app.log" 
)

logger = logging.getLogger(__name__)


def make_request():
    attempt = 0
    for _ in range(3):
        attempt += 1
        logger.info(f"attempt number : {attempt}")
        try:
            raise Exception("API request Failed")
        except Exception:
            logger.warning(f"API request Failed attempt number {attempt}")
            if attempt == 3:
                logger.error("All attempts exhausted")
            else:
                logger.warning(f"Retrying the request")


try:
    logger.info("Application Started")
    result = make_request()
except Exception:
    logger.exception("An exception occured")

finally:
    logger.info("Application finished")



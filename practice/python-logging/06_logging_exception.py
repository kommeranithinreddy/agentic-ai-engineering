import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename = "app.log"
)

logger = logging.getLogger(__name__)
def divide(a : int, b : int) -> float:
    return a / b

try:
    divide(1, 0)
except Exception:
    logger.exception("An exception occurred")



import logging
from logging.handlers import TimedRotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger():
    logger = logging.getLogger("fastapi_app")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if logger.handlers:
        return logger

    log_file = os.path.join(LOG_DIR, "app.log")

    # Rotate daily + keep last 7 days
    file_handler = TimedRotatingFileHandler(
        log_file,
        when="midnight",
        interval=1,
        backupCount=7
    )
    file_handler.suffix = "%Y-%m-%d"

    # Console handler
    console_handler = logging.StreamHandler()

    # Format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Global logger instance
logger = setup_logger()
from loguru import logger
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger.add("logs/crawler.log", rotation="500 KB", retention="10 days", level="DEBUG")
    return logger

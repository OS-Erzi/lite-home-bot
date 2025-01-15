from loguru import logger

def setup_logger():
    logger.add("logger/logs/file_{time}.log", rotation="250 MB", compression="zip")
    return logger

loguru_log = setup_logger()
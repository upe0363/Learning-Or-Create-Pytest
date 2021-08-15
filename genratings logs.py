import logging


# logging.basicConfig(filename="c:\\learning pytest\\logs\\logfile.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d%Y %I:%M:%S %p',level=logging.INFO)

# log = logging.getLogger()
# log.info("this is our first log")

def log():
    logging.basicConfig(filename="c:\\learning pytest\\logs\\logfile.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d%Y %I:%M:%S %p',
                        level=logging.INFO)

    logger = logging.getLogger()
    return logger


logger = log()
logger.info("this is a new log")
logger.error("this is an error message")

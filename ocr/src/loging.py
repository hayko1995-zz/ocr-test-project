import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET

logging.basicConfig(level=logging.DEBUG)

def logging_levels():
    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")
    logging.critical("This is critical")

def logging_levels_above_than(LevelValue=NOTSET):
    logging.disable(level=LevelValue)

    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")
    logging.critical("This is critical")

if __name__ == "__main__":
    logging_levels()
    print("\n")
    logging_levels_above_than()

import logging
import os
from logging import handlers
import time

BASS_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = ""
EMP_ID = ""



def init_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler(BASS_DIR + "/log/ihrm.log",when="s",
                                                   interval=10,backupCount=10,encoding="utf-8")

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)



if __name__ == '__main__':
    init_logger()
#     logging.info("哈喽")
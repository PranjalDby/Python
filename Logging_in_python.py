from asyncio.log import logger
from cgitb import handler
import logging
from logging.handlers import RotatingFileHandler
# # logging.basicConfig(level=logging.DEBUG,format= '%{asctime}s - %{name} - %{levelname}s - %{message}s',datefmt='%m/%d/%Y %M:%M:%S')
# logging.basicConfig(level=logging.DEBUG,format = '%(levelname)s - %(asctime)s - %(message)s',datefmt='%m/%d/%Y')
# import helperlogger
# # loghandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# roll over after 2kb and keep backups log1,log2
handler = RotatingFileHandler('app.log',maxBytes=2000,backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('hello world')



import logging

log_format = "%(asctime)s%(levelname)s%(message)s"

logging.basicConfig(filename='panda.log',level=logging.DEBUG, format=log_format)

logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")


#另外一种写法
logging.log(logging.DEBUG,"hhhh")
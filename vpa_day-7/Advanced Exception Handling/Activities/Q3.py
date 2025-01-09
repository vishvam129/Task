# Use the logging module to log exceptions to a file instead of 
# printing them to the console.

import logging

try:
    ans = 5/0
except ZeroDivisionError as e:
    logging.basicConfig(filename = 'error.txt',filemode = 'w',format = '%(asctime)s %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    # logger.debug("This is level 10 msg")
    # logger.info("This is level 20 msg")
    # logger.warning("This is level 30 msg")
    # logger.error("This is level 40 msg")
    logger.critical(e)
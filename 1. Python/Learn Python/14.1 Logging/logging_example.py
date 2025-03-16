import logging
# level can be logging.ERROR , INFO etc
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    ## adding formatting to show etc info
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("this is an info msg")
logging.debug('this is an debug msg')
logging.warning('this is a warning msg')
logging.error('this is an error msg')
logging.critical('this is a critical msg')
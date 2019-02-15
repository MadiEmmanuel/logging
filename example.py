import logging
'''import height

#try:
  #height(3) = a
  #a = 0.8799999999999999
#except Exception as e:
  #logging.exception("Exception occurred")'''

logging.basicConfig(filename='msg.log', filemode='w',level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logging.debug('This will get logged')

logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_handler)
f_handler.setFormatter(f_handler)

logger.addHandler(c_handler)
logger.addHandler(c_handler)

logger.warning('This is a warning')
logger.error('This is an error')

from common.logger import *

if __name__ == '__main__':
	logger = Logger('app.log', logging.ERROR,logging.DEBUG)
	logger.debug('===here we start===')
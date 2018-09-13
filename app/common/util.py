import ConfigParser
import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler


class CommonUtil:
	def __init__(self, configDir=os.path.join(os.getcwd(, '../../app.cfg'):
		self.configFile = configFire


	def getParserConfig(self, section, key):
		with open(self.configDir) as fp:
			config = ConfigParser.ConfigParser()
			config.readfp(fp)

		try:
			res = config.get(section, key)
		except Exception as e:
			res = str(e)


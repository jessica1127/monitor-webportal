# -*- coding=utf-8

import ConfigParser
import traceback
from logger import *


class Configger():
	def __init__(self, configFile='../../app.cfg'):
		self.configFile = configFile
		self.logger = Logger('../../app.log', logging.DEBUG,logging.DEBUG)


	def getParserConfig(self, section, key):
		with open(self.configFile) as fp:
			config = ConfigParser.ConfigParser()
			config.readfp(fp)

		try:
			res = config.get(section, key)
		except Exception as e:
			res = str(e)
			self.logger.exception('traceback: {0}'.format(traceback.printexc()))
		return res

	def getParserSection(self, sec):
		sectionCont = dict()
		ret = 0
		try:
			with open(self.configFile) as fp:
				config = ConfigParser.ConfigParser()
				config.readfp(fp)
			for key in config.options(sec):
				sectionCont[key] = config.get(sec, key)
				self.logger.debug('key = {0}, val = {1}'.format(key, config.get(sec, key)))
				self.logger.debug('Internal sectionCont={0}'.format(sectionCont))
			self.logger.debug('sectionCont: {0}'.format(sectionCont))
		except Exception as e:
			res = str(e)
			ret = 1
			sectionCont = {}
			self.logger.exception('traceback: {0}'.format(traceback.print_exc()))

		return sectionCont, ret



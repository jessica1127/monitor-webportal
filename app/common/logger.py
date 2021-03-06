# -*- coding=utf-8

import logging, os


class Logger:
	def __init__(self, path='../../app.cfg', Clevel = logging.DEBUG, Flevel = logging.DEBUG):
		self.logger = logging.getLogger(path)
		self.logger.setLevel(Flevel)
		fmt = logging.Formatter("%(asctime)s %(name)s [line:%(lineno)d] %(levelname)s %(message)s")
		#set CMD logger:
		sh = logging.StreamHandler()
		sh.setFormatter(fmt)
		sh.setLevel(Clevel)

		#set file log:
		fh = logging.FileHandler(path)
		fh.setFormatter(fmt)
		sh.setLevel(Flevel)

		self.logger.addHandler(sh)
		self.logger.addHandler(fh)


	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def error(self, message):
		self.logger.error(message)

	def war(self, message):
		self.logger.warning(message)

	def cri(self, message):
		self.logger.critical(message)

	def exception(self, message):
		self.logger.exception(message)




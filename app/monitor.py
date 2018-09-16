
#-*- coding:utf-8
from os import getcwd
from common.logger import *
from common.configger import *
from common.util import *

import re
import urllib2
import sys
import os
from bs4 import BeautifulSoup

class Monitor():
	def __init__(self, configFile):
		self.configFile = 'app.cfg'
		self.logger = Logger('app.log', logging.DEBUG,logging.DEBUG)
		self.configger = Configger(configFile)
		self.directory = os.getcwd() + '/cache'

	def readUrlandCompare(self):
		sectionCont, ret = self.configger.getParserSection('urllist')

		self.logger.debug('sectionCont: {0}, ret = {1}'.format(sectionCont, ret))
		DB_NAME = self.configger.getParserConfig('db', 'name')
		DB_PATH = getcwd()
		c, con = db_connect(DB_NAME, DB_PATH)
		db_setup_everything(c, con)
		for key, url in sectionCont.items():
			self.logger.debug('key={0}, url={1}'.format(key, url))
			if checkUrl(url):		#check if url is a real url
				try:
					os.stat(self.directory)
				except:
					os.makedirs(self.directory)

				try:
					hdr = {'User-Agent':'Mozilla/5.0'}
					req = urllib2.Request(url, headers = hdr)
					response = urllib2.urlopen(req)
					html_page = response.read()

					#req = urllib2.Request(url)
					self.logger.debug('111111111111 = {0}')
					#html_page = urllib2.urlopen(req)
					self.logger.debug('html_page = {0}'.format(html_page))
					self.logger.debug('key={0}, url = {1}, html_page = {2}'.format(key, url, html_page))
					
				except urllib2.URLError as reason:
					self.logger.error("URLError : {0}".format(reason)) 
					continue
				except ValueError:
					self.logger.error("Invalida URL: {0}".format(url))
					continue
				except keyboardInterrupt:
					self.logger.error("Invalida URL: {0}".format(url));

				source = html_page
				soup = BeautifulSoup(source, features="lxml")
				body = str(soup.body).replace('\n', ' ')
				self.logger.debug('soup.headers = {0}'.format(soup.headers))
				self.logger.debug('soup.body = {0}'.format(body))
				
				diff = ''
			else:
				self.logger.error('The item:{0} in section urllist is not a url,please check!'.format(url))
				break



if __name__ == '__main__':
	monitor = Monitor(configFile='../app.cfg')
	configger = monitor.configger
	monitor.readUrlandCompare()
	
	
	
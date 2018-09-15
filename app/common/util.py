# - * - coding=utf-8

import sqlite3 as lite
from os import getcwd

from logger import *
from configger import *
import re


logger = Logger('../../app.log', logging.DEBUG,logging.DEBUG)
def checkUrl(url) :
    # django regex for url validation
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.search(regex, url) == None :
        return 0
    else :
        return 1

def db_connect(db_name, db_path):
    con = lite.connect(db_path + '/' + db_name)
    c = con.cursor()
    logger.debug('Internal db_connect: c = {0}, con = {1}'.format(c, con))

    return c, con


def db_setup_everything(c, con):
    try:
        c.execute('SELECT * from cache')
    except lite.OperationalError:       
        c.execute("CREATE TABLE cache(item text, url text, content text)")
    con.commit()



     
############### LOGGING VARIABLES DATA ####################

import logging

name = 'Venkat Shyam'

logging.error('%s raised an error', name)
logging.error('{} raised an error'.format(name))
logging.error('{0} raised an error'.format(name))
logging.error('{name1} raised an error'.format(name1=name))

"""
While you can use any of above formatting style, the f-strings introduced in Python 3.6 
are an awesome way to format strings as they can help keep the formatting short 
and easy to read:
"""
#logging.error(f'{name} raised an error')
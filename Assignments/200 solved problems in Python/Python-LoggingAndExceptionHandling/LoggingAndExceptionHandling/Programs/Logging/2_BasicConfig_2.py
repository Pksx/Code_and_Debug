############### LOGGING TO A FILE USING basicConfig() ####################

import logging

logging.basicConfig(level= logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logging.error('This will get logged to a file')


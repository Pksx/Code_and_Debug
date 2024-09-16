############### LOGGING AS PER FORMAT SPECIFIED USING basicConfig() ####################

import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

#logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logging.info('This is an Info')

logging.warning('This is a Warning')
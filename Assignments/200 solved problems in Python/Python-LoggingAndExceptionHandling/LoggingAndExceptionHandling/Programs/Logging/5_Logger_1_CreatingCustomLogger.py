############### CREATING CUSTOM LOGGER####################

"""Logger: This is the class whose objects will be used in the application code directly
to call the functions."""

import logging

logger = logging.getLogger('example_logger')

logger.warning('This is a warning message of custom made example_logger')
logging.warning('This is a warning message of default root logger')

"""Format specifier needs to be added to see which custom logger is actually called unlike default root logger"""
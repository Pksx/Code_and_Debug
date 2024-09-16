############### CAPTURING STACK TRACES USING LOGGING.EXCEPTION####################

import logging

a = 5
b = 0
try:
  #logging.exception("Testing exception but it is not meaningful to add here")
  c = a / b

except Exception as e:
  logging.exception("Exception occurred")
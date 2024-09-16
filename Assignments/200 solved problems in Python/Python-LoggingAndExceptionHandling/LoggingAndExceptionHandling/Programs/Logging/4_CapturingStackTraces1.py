############### CAPTURING STACK TRACES USING exc_info=True####################

import logging

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    #logging.error(e)
    #logging.error("Exception occurred", exc_info=False)

"""
try:
    print("#############********************##################")
    print("I am here even after above exception")
except:
    print ("exception block")

"""
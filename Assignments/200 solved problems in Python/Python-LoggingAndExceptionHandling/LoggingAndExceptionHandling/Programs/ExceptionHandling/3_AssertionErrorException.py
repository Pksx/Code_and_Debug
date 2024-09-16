############ASSERTION ERROR EXCEPTION################

import sys

print("PLATFORM TYPE: ", sys.platform)
assert ('abc' in sys.platform), "This condition code runs on Linux only."

print("i am here after assert")
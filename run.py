from transistate import getTransistate

import time
import math

# fetch realtime data every 10 seconds forever
while True:
    timeName = str(math.floor(time.time()))
    if timeName[-1] == '0':
        getTransistate(timeName)

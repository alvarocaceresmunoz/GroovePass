import grovepi
import time
from constants import *

def getKnockString(knockDetected):
    if knockDetected: return 'Knock!'
    else: return '......'

def getKnocks():
    grovepi.pinMode(PORT_TOUCH,'INPUT')

    userKeepsKnocking = True
    timeSinceLastKnock = 0

    # csv file entries are stored here
    log = []
    knocks = []

    while userKeepsKnocking:
        timestamp = time.time()
        distance = grovepi.ultrasonicRead(PORT_DISTANCE)
        touch = grovepi.digitalRead(PORT_TOUCH)

        if touch == TOUCH_ON and distance < DISTANCE_MIN:
            knockDetected = True
            timeSinceLastKnock = 0
        else:
            knockDetected = False
            timeSinceLastKnock += 1

        log.append([timestamp, distance, touch, knockDetected, timeSinceLastKnock])
        print('%f,%d,%d,%s,%d' % (timestamp, distance, touch, knockDetected, timeSinceLastKnock))
        knocks.append(knockDetected)

        # print('%f,%s,%d' % (timestamp, getKnockString(knockDetected), distance, timeSinceLastKnock))

        if timeSinceLastKnock > TIME_SINCE_LAST_KNOCK_MAX:
            userKeepsKnocking = False

        time.sleep(WAIT_TIME)

    return [knocks, log]

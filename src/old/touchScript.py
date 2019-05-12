import grovepi
import time

# sensor constants
distanceMin = 30

# port constants
portDistance = 4
portTouch = 3
grovepi.pinMode(portTouch,'INPUT')

# other constants
userKeepsKnocking = True
timeSinceLastKnock = 0
timeSinceLastKnockMax = 40
waitTime = 0.001

# csv file entries are stored here
logList = []

print("[info] Start listening in 1...")
time.sleep(1)
print("[info] 2...")
time.sleep(1)
print("[info] 3...")
time.sleep(1)
print("[info] Start knocking!")

while userKeepsKnocking:
    distance = grovepi.ultrasonicRead(portDistance)
    touch = grovepi.digitalRead(portTouch)

    if touch == 1:
        knockDetected = True
        timeSinceLastKnock = 0
    else:
        knockDetected = False
        timeSinceLastKnock += 1

    logList.append([knockDetected, timeSinceLastKnock])

    knockString = ''
    if knockDetected:
        knockString = 'Knock!'
    else:
        knockString = '......'
    print('%s,%d' % (knockString, timeSinceLastKnock))

    # print("%4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %s, %d, %f, %f, %f, %f"%(time.time(),distance,loudness,noise,noiseAvg,loudnessHPF,noiseHPF,knockDetected,timeSinceLastKnock,accelerationX,accelerationY,accelerationZ,accelerationCombined))

    if timeSinceLastKnock > timeSinceLastKnockMax:
        userKeepsKnocking = False

    time.sleep(waitTime)

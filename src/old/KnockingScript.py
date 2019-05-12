import grovepi
import time
import grove6axis

#HIGH PASS VARIABLES
loudnessHPF = 0
loudnessLast = 0
noiseHPF = 0
noiseLast = 0
constant = 0.1

#NOISE/LOUDNESS VARIABLES
zeroSound = True
loudnessStart = 0
noiseStart = 0
noiseAvg = 0
noiseThreshold = 0
i = 0
maxLoops = 500
distanceMin = 30

# port config constants
portLoudness = 2
portNoise = 1
portDistance = 4
portTouch = 3
grovepi.pinMode(portTouch,'INPUT')

# other constants
userKeepsKnocking = True
timeSinceLastKnock = 0
timeSinceLastKnockMax = 40
waitTime = 0.005

grove6axis.init6Axis()

logList = []

print("[info] getting ambient noise...")
while userKeepsKnocking:
    distance = grovepi.ultrasonicRead(portDistance)
    loudness = grovepi.analogRead(portLoudness)
    noise = grovepi.analogRead(portNoise)
    touch = grovepi.digitalRead(portTouch)

    acceleration = grove6axis.getAccel()
    accelerationX = acceleration[0]
    accelerationY = acceleration[1]
    accelerationZ = acceleration[2]
    accelerationCombined = abs(accelerationX) + abs(accelerationY) + abs(accelerationZ)

    if zeroSound == True:
        while True:
            #READ THE VALUES EACH RUN
            #read from an analog sensor on input 1 (loudness sensor)
            loudness = grovepi.analogRead(portLoudness)
            #read from an analog sensor on input 1 (noise sensor)
            noise = grovepi.analogRead(portNoise)

            #Average the first 500 values to zero the input
            loudnessStart = loudness + loudnessStart
            noiseStart = noise + noiseStart
            i += 1

            # print("Loop %d: %4.2f, %4.2f"%(i,loudnessStart,noiseStart))

            #Break out of the loop and calculate the average and threshold (25% above)
            if i == maxLoops:
                noiseAvg = (loudnessStart + noiseStart) / (i * 2)
                noiseThreshold = noiseAvg / 3
                # print("Average Sound: %4.2f, Upper Threshold: %4.2f"%(noiseAvg, noiseThreshold))
                zeroSound = False
                print("[info] ambient sensing done...")
                time.sleep(1)
                print("[info] Start listening in 1...")
                time.sleep(1)
                print("[info] 2...")
                time.sleep(1)
                print("[info] 3...")
                time.sleep(1)
                print("[info] Start knocking!")
                print("time,distance,loudness,noise,noiseAvg,loudnessHPF,noiseHPF,knockDetected,timeSinceLastKnock,accelerationX,accelerationY,accelerationZ,accelerationCombined")
                break

    #Calculate the generic high pass filter for the loudness sensor
    loudnessHPF = constant * (loudnessHPF + loudness - loudnessLast)
    loudnessLast = loudness

    #Calculate the generic high pass filter for the noise sensor
    noiseHPF = constant * (noiseHPF + noise - noiseLast)
    noiseLast = noise

    #If the high pass is above 4 and the sensor readings are above the average threshold, knocking is occuring
    #if loudness > (noiseAvg + noiseThreshold): # and distance < distanceMin:
    if touch == 1:
        knockDetected = True
        timeSinceLastKnock = 0
    else:
        knockDetected = False
        timeSinceLastKnock += 1

    knockString = ''
    if knockDetected:
        knockString = 'Knock!'
    else:
        knockString = '......'
    logList.append([knockDetected, timeSinceLastKnock])
    print('%s,%d' % (knockString, timeSinceLastKnock))
    # print("%4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %4.2f, %s, %d, %f, %f, %f, %f"%(time.time(),distance,loudness,noise,noiseAvg,loudnessHPF,noiseHPF,knockDetected,timeSinceLastKnock,accelerationX,accelerationY,accelerationZ,accelerationCombined))

    if timeSinceLastKnock > timeSinceLastKnockMax:
        userKeepsKnocking = False



import grovepi
import time
import grove6axis

inputPortDistance = 4
inputPortLoudness = 2
grove6axis.init6Axis()

typeTime = '%f'
typeLoudness = '%d'
typeDistance = '%d'
typeOrientation = '%f'
typeAcceleration = '%f'
sensorVariables = [typeTime, typeDistance, typeLoudness, typeOrientation, typeOrientation, typeOrientation, typeAcceleration, typeAcceleration, typeAcceleration]
headerString = 'time, distance, loudness, orientationX, orientationY, orientationZ, accelerationX, accelerationY, accelerationZ'
rowFormatString = ','.join(sensorVariables)

waitTime = 0.001

print(headerString)
while(True):
    timestamp = time.time()
    loudness = grovepi.analogRead(inputPortLoudness)
    distance = grovepi.ultrasonicRead(inputPortDistance)
    orientation = grove6axis.getOrientation()
    orientationX = orientation[0]
    orientationY = orientation[1]
    orientationZ = orientation[2]
    acceleration = grove6axis.getAccel()
    accelerationX = acceleration[0]
    accelerationY = acceleration[1]
    accelerationZ = acceleration[2]

    print(rowFormatString % (timestamp, distance, loudness, orientationX, orientationY, orientationZ, accelerationX, accelerationY, accelerationZ))
    time.sleep(waitTime)
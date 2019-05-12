import grovepi
import time
import grove6axis

inputPortDistance = 4
inputPortTouch = 3
grovepi.pinMode(inputPortTouch,'INPUT')
inputPortLoudness = 2
grove6axis.init6Axis()

# nearDistanceThreshold = 60
typeTime = '%f'
typeLoudness = '%d'
typeDistance = '%d'
typeTouch = '%d'
typeOrientation = '%f'
typeAcceleration = '%f'
sensorVariables = [typeTime, typeDistance, typeLoudness, typeTouch, typeOrientation, typeOrientation, typeOrientation, typeAcceleration, typeAcceleration, typeAcceleration]
header = 'time, distance, loudness, touch, orientationX, orientationY, orientationX, accelerationX, accelerationY, accelerationZ'
rowFormatString = ','.join(sensorVariables)

waitTime = 0.1

print(header)
while(True):
    timestamp = time.time()
    distance = grovepi.ultrasonicRead(inputPortDistance)
    loudness = grovepi.analogRead(inputPortLoudness)
    touch = grovepi.digitalRead(inputPortTouch)

    orientation = grove6axis.getOrientation()
    orientationX = orientation[0]
    orientationY = orientation[1]
    orientationZ = orientation[2]

    acceleration = grove6axis.getAccel()
    accelerationX = acceleration[0]
    accelerationY = acceleration[1]
    accelerationZ = acceleration[2]

    print(rowFormatString % (timestamp, distance, loudness, touch, orientationX, orientationY, orientationX, accelerationX, accelerationY, accelerationZ))

    # print(rowFormatString % (timestamp, distance, loudness, orientationX, orientationY, orientationZ, accelerationX, accelerationY, accelerationZ))
    # if distance < nearDistanceThreshold:
    #     print('%d: near!', distance)
    # else:
    #     print('%d: far...', distance)
    time.sleep(waitTime)

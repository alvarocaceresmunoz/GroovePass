from utils import *
from sensing import getKnocks
from processing import getPassword
from security import password

printCountdown()
results = getKnocks()
knocks = results[0]
logs = results[1]

f = open('alvaro.csv','w+')
for log in logs:
    f.write('%f,%d,%d,%s,%d\n' % (log[0],log[1],log[2],log[3],log[4]))
f.close()

# inputPassword = getPassword(knocks)

# if (inputPassword == password):
#     print('door unlocked!')
# else:
#     print('door locked')

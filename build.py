import os
import time
input1 = input("What version of pip do u use?: ")

os.system(input1 + " install flask")
time.sleep(3)
os.system(input1 + " install sockets")
time.sleep(3)
os.system(input1 + " install requests")


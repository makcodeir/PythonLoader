import time
import sys


animation = [".","..","...","....",".....",":....","::...",":::..","::::.",":::::"]

for i in range(5):
    for i in range(len(animation)):
        time.sleep(0.1)
        str = animation[i]
        sys.stdout.write("\r" + str)
        sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write("\r" + "     ")
    sys.stdout.flush()
print("End!")
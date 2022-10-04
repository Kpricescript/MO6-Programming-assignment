import time
seconds = input("how many seconds? ")
for x in range(seconds, 0, -1):
    print; str(x) + " seconds remain."
    time.sleep(1)
print ("time has stopped")
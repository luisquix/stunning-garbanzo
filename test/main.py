import quixstreams as qx
import os
import time

# Quix injects credentials automatically to the client.
# Alternatively, you can always pass an SDK token manually as an argument.
client = qx.QuixStreamingClient()

while True:
    print(time.ctime())
    # Prints the current time with a five second difference
    time.sleep(5)

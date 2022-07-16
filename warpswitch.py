#!/usr/bin/env python3
import subprocess
import os
import time
import sys
import itertools
import threading
proc = subprocess.Popen(["warp-cli status"],stdout=subprocess.PIPE, shell=True)
(out, err)=proc.communicate()
done = False
def animate():
    for c in itertools.cycle(['|','/','-','\\']):
        if done:
            break
        sys.stdout.write("\b%s" % c)
        sys.stdout.flush()
        time.sleep(0.1)    
if "Disconnected" in str(out):
    print("Current status: Disconnected\n")
    t = threading.Thread(target=animate)
    print("wait a moment...")
    t.start()
    time.sleep(2)
    done = True
    os.system('warp-cli connect')
if "Connected" in str(out):
    print("Current status: Connected\n")
    t = threading.Thread(target=animate)
    print("wait a moment...")
    t.start()
    time.sleep(2)
    done = True
    os.system('warp-cli disconnect')

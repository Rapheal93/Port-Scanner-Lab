#! /usr/bin/env python

import platform
import socket
import subprocess
import sys
from datetime import datetime

# clear the screen
if platform.system() == "Windows":
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)

# ask for input
remoteServer = input("Enter a remote host to scan: ")
target = socket.gethostbyname(remoteServer)

# Print a nice banner
print("-" * 60)
print("Please wait, scanning the remote host", target)
print("-" * 60)

# check what time the scan started
t1 = datetime.now()

# error handling
try:
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port %d is Open" % port)
        sock.close()

except KeyboardInterrupt:
    sys.exit("You pressed Ctrl+C")

except socket.gaierror:
    sys.exit("Hostname could not be resolved. Exiting")

except socket.error:
    sys.exit("Couldn't connect to server")

# checking the time again
t2 = datetime.now()

# calculates how longs program took to run
total = t2 - t1

# Printing the information to screen
print("Scanning Completed in: ", total)


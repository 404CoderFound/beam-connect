import os
import time
import subprocess

packages = ["flask", "sockets", "requests"]

try:
    ver = subprocess.check_output(['pip', '--version']).decode().split()[0]
except (subprocess.CalledProcessError, IndexError):
    print("Failed to retrieve pip version. Please make sure pip is installed correctly.")
    exit(1)

for package in packages:
    os.system(f"{ver} install {package}")
    time.sleep(3)

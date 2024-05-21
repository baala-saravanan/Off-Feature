import os
import vlc
import subprocess
import sys
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from play_audio import GTTSA

# Clear and refresh cache memory with sudo
subprocess.run(["sudo", "sync"])
subprocess.run(["sudo", "sh", "-c", "echo 1 > /proc/sys/vm/drop_caches"])

def cleanup():
    os.system("python3 /home/rock/Desktop/Hearsight/mycroft-precise/test/scripts/cleanup.py")

def Shutdown_Radxa_Zero():
    play_audio = GTTSA()

    play_audio.play_machine_audio("hearsight device off.mp3")

    play_audio.play_machine_audio("Thank You.mp3")

    play_audio.play_machine_audio("now press on off switch to power off.mp3")

    os.system("shutdown now")    

cleanup()
Shutdown_Radxa_Zero()

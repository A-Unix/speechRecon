#!/usr/bin/python3

import os
import subprocess
import time
import speech_recognition as sr
from colorama import init, Fore

# Initialize colorama
init()

# Install colorama and requests using subprocess
subprocess.run(["pip", "install", "colorama"])

print("Please wait!")

time.sleep(3)

# Clear the terminal screen
os.system("clear")

import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))

time.sleep(2)

import sys
print("Python version:")
print(sys.version)
print("Python version:", sys.version_info)

time.sleep(2)

# Check if the script is running as root
print(Fore.BLUE + "Checking if the script is running as root! Please wait!")

time.sleep(2)

if os.geteuid() != 0:
    print(Fore.YELLOW + "This script is not running as root, please run it as root!")
    exit(1)

time.sleep(1)

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(Fore.CYAN + "Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=12)

        try:
            print(Fore.YELLOW + "You said: " + recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print(Fore.RED + "Could not understand audio")
        except sr.RequestError as e:
            print(Fore.GREEN + "Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    recognize_speech()

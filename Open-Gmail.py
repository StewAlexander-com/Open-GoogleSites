#!/usr/bin/env python3
import os
import sys
import requests
import time
import webbrowser
import re

print("\n\n")

print("""
  ┌──────────────────────────────────────────┐
  │                                          │
  │  This program opens Chrome and goes to   │
  │  Gmail,GCalendar and Drive; if Chrome is │
  │  not installed, it installs it first     │
  │                                          │
  └──────────────────────────────────────────┘
""" )

#Check if Google Chrome is installed on the Windows system, if not, install it
#If it is installed, go to gmail.com 

if os.path.exists("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
    #find google chrome
    chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    #open google chrome
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab('https://gmail.com')
    time.sleep(2)
    #open a new tab and go to calendar.google.com
    webbrowser.get('chrome').open_new_tab('https://calendar.google.com')
    time.sleep(2)
    #open a new tab and go to drive.google.com
    webbrowser.get('chrome').open_new_tab('https://drive.google.com')
    time.sleep(2)
else:
    print("Google Chrome is not installed")
    #download the chrome installer from the web and install it on the system
    webbrowser.get('chrome').open("https://www.google.com/chrome/browser/desktop/index.html")
    #wait for the download to finish
    time.sleep(10)
    #install the chrome installer
    os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    #open Google chrome and go to gmail.com
    webbrowser.get('chrome').open("https://gmail.com")
    #open another tab and go to the url https://calendar.google.com/
    webbrowser.get('chrome').open_new_tab("https://calendar.google.com/")

#Keep the program running until the user presses the enter key
input("\n\nPress Enter to quit Chrome and exit the program: ")
#quit chrome
time.sleep(2)
print("\n\n")
sys.exit()

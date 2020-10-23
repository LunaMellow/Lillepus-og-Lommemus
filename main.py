# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020-2023 NoreJ and KnutJ                                     #
#                                                                         #
# V-Cloud is a base layer login script with encrypted read - write code.  #
#                                                                         #
# V-Cloud is free software: you can redistribute                          #
# it and/or modify it under the terms of the GNU General Public License   #
# as published by the Free Software Foundation, either version 3 of the   #
# License, or (at your option) any later version.                         #
#                                                                         #
# V-Cloud is distributed in the hope that it                              #
# will be useful, but WITHOUT ANY WARRANTY; without even the implied      #
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See    #
# the GNU General Public License for more details.                        #
#                                                                         #
# You should have received a copy of the GNU General Public License along #
# with V-Cloud.  If not, see <http://www.gnu.org/licenses/>.              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing libraries
from time import sleep
import datetime
import socket
from tqdm import tqdm
import sys
import json
from urllib.request import urlopen
import interval
from kivy.app import App
from kivy.uix.button import Button

#IPinfo.io database variables
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

#IP variables
IP = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

# defining locationinfo for log.txt
locinfo = 'IP : {4} Region : {1} Country : {2} City : {3} Org : {0}'.format(org,region,country,city,IP)

# Debug console with syntax: Online/Offline
print("\033[1;32;10mDebug variable.function\033[1;32;0m(serv_stat)\n.....................................................")
print("Console variable (syntax: Online/Offline)")
serv_stat_ans = input("Input: ")

# Defining variables
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
time_now = datetime.datetime.now()
serv_stat = serv_stat_ans  # debug: "Online"

# Logging client-side
l = open("log.txt", "w+")
l.write("## Script initiated ##\n")
l.write("Time:%r[GMT]\n" % time_now.strftime("%A %D %X"))
l.write("Ip_address:%r\n" % ip_address)
l.write("\n")
l.write("MiscData: %r\n" % locinfo)
l.write("\n")
l.close()

# Introducing script with purpose and socket information
print(".....................................................")
ip_welcome = "Welcome ip: %s to V-Cloud async verification.\n" % ip_address
for char in ip_welcome:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print(".....................................................")
sleep(1)

# Using the strftime() function
# Defining if day is equal to the 3rd or 23rd
if time_now.strftime("%d") == "3" or "23":
    day_info = "Today is " + time_now.strftime("%A") + " the " + time_now.strftime("%d") + "rd.\n"
    for char in day_info:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

# Defining if day is equal to the 1st or 21st or 31st
elif time_now.strftime("%d") == "1" or "21" or "31":
    day_info = "Today is " + time_now.strftime("%A") + " the " + time_now.strftime("%d") + "st.\n"
    for char in day_info:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

# Defining if day is equal to the 2nd or 22nd
elif time_now.strftime("%d") == "2" or "22":
    day_info = "Today is " + time_now.strftime("%A") + " the " + time_now.strftime("%d") + "nd.\n"
    for char in day_info:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

# Defining if day is in interval [4, 20] or [24, 30]
elif time_now.strftime("%d") == interval([4, 20]) or interval([24, 30]):
    day_info = "Today is " + time_now.strftime("%A") + " the " + time_now.strftime("%d") + "th.\n"
    for char in day_info:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
else:
    print("An error occured when getting the date, continuing procedure")

# Attempting connection to Azure SQL servers
print(".....................................................")
print("We are currently connecting and syncing our sql servers")
loading_dots = "-----------------------------------------------------\n"
for char in loading_dots:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()

# Write server status from debug() to file
f = open("server_status.txt","w+")
if f.mode == 'w+':
    contents = f.read()
    if contents == "":
      f.write(serv_stat)
      f.close()
    else:
      f.close()
      print("\033[1;31;10mFile could not write\033[1;32;0m")
else:
  f.close()
  print("\033[1;31;10mERROR: Server status could not be verified\033[1;32;0m")

# Read server status from file
f = open("server_status.txt","r")
if f.mode == 'r':
  contents = f.read()
  if contents == "Online":
    f.close()
    print("\033[1;32;10m Servers are online and operative. \n Encrypted services have been initialized")
  elif contents == "Offline":
    f.close()
    print("\033[1;31;10mServers are offline, attemping reboot...\033[1;32;0m\n.....................................................")
    print("Sending request to servers")
    print(".....................................................")

# Tqdm request dummy
    Request = [
    'Sending boot request',
    '...',
    'Returned request recieved',
    ]

    for i in tqdm(Request):
      sleep(0.75)
      print(i)
    
    sleep(1)
    print(".....................................................")
    print("Key recieved and verified, booting up") 
    print(".....................................................")
    sleep(1)

# Tqdm recieve dummy
    Recieve = [
    'BIOS booting...',
    '...',
    '..',
    '.',
    'BIOS is running',
    'Updating drivers',
    '...',
    '..',
    'EncrypGet.func has booted sucsessfully',
    'Boot disk server status: Online',
    'Servers are now up and functioning',
    ]
    for i in tqdm(Recieve):
      sleep(1.25)
      print(i)
    serv_stat = "Online"
    if serv_stat == "Online":
      print(".....................................................")
      print("\033[1;32;10m Servers are online and operative. \n Encrypted services have been initialized")
  else:
    f.close()
    print("\033[1;31;10mERROR: Server status could not be verified\033[1;32;0m")
else:
  f.close()
  print("\033[1;31;10mERROR: The file could not be opened due to an unknown error\033[1;32;0m")
f.close()

# Line break for continuation
print("\033[1;32;0m.....................................................")
sleep(1)

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()
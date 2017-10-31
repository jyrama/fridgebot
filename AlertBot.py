import RPi.GPIO as GPIO
import time
import os
from subprocess import Popen

buttonPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

wait_seconds = 120
alert_wait = wait_seconds * 2

t_end = time.time() + wait_seconds
alertfade_time = time.time() + alert_wait
alert = False

while True:
  if GPIO.input(buttonPin):
    if time.time() >= t_end:
      print('Alert sent to mattermost')
      Popen(['mattersend','--config', '/home/pi/techday/fridgebot/mattersend.conf', '-f', '/home/pi/techday/fridgebot/auki.txt'])
      alert = True
      t_end = time.time() + wait_seconds
      alertfade_time = time.time() + alert_wait
  else:
    t_end = time.time() + wait_seconds
    if alert == True and time.time() >= alertfade_time:
      print('Alert off')
      alert = False
      Popen(['mattersend','--config', '/home/pi/techday/fridgebot/mattersend.conf', '-f', '/home/pi/techday/fridgebot/suljettu.txt'])
  time.sleep(0.02)

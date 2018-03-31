import RPi.GPIO as GPIO
import time

import json
from glob import glob
from importlib import import_module

config = json.loads('config.json')

buttonPin = config['button_pin']
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

wait_seconds = config['wait_seconds']
alert_wait = config['alert_wait']

t_end = time.time() + wait_seconds
alertfade_time = time.time() + alert_wait
alert = False

mainloop_sleep = config['mainloop_sleep']

# load sink modules, symlinked etc, from sinks folder
sinks = [import_module(x.replace('/', '.')[:-3]) for x in glob('sinks/*.py')]

if len(sinks) == 0:
    import sys
    print('No modules loaded!')
    sys.exit(1)

# Set config attribute for modules loaded
for module in sinks:
    module.config = config


def send_notifications():
    for sink in sinks:
        sink.notify()


def send_thanks():
    for sink in sinks:
        sink.thanks()


# main loop
while True:
    if GPIO.input(buttonPin):
        if time.time() >= t_end:
            send_notifications()
            alert = True
            t_end = time.time() + wait_seconds
            alertfade_time = time.time() + alert_wait
    else:
        t_end = time.time() + wait_seconds
        if alert and (time.time() >= alertfade_time):
            print('Alert off', flush=True)
            send_thanks()
            alert = False
    time.sleep(mainloop_sleep)

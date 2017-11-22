import RPi.GPIO as GPIO
import time

from glob import glob
from importlib import import_module

buttonPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

wait_seconds = 120
alert_wait = wait_seconds * 2

t_end = time.time() + wait_seconds
alertfade_time = time.time() + alert_wait
alert = False

# load sink modules, symlinked etc, from sinks folder
sinks = [import_module(x.replace('/', '.')[:-3]) for x in glob('sinks/*.py')]

if len(sinks) == 0:
    import sys
    print('No modules loaded!')
    sys.exit(1)

    
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
    time.sleep(0.02)

import RPi.GPIO as GPIO
import time
from subprocess import Popen, PIPE

MATTERSEND_CONF = '/home/pi/techday/fridgebot/mattersend.conf'
DOOR_CLOSED_FILE = '/home/pi/techday/fridgebot/suljettu.txt'
DOOR_OPEN_FILE = '/home/pi/techday/fridgebot/auki.txt'

irc = Popen(['ssh', '-t', 'hacklab-irc'], stdin=PIPE)
irc.stdin.write("pass freenode\nuser\nnick\n".encode())

buttonPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

wait_seconds = 120
alert_wait = wait_seconds * 2

t_end = time.time() + wait_seconds
alertfade_time = time.time() + alert_wait
alert = False


def notify_irc():
    irc.stdin.write("notice #hacklab.jkl :Jääkaapin ovi on jäänyt auki!\n".encode())
    irc.stdin.flush()
    print('Alert sent to IRC', flush=True)


def notify_mattermost():
    Popen(['mattersend', '--config', MATTERSEND_CONF, '-f', DOOR_OPEN_FILE])
    print('Alert sent to Mattermost', flush=True)


def thanks_mattermost():
    Popen(['mattersend', '--config', MATTERSEND_CONF, '-f', DOOR_CLOSED_FILE])


def thanks_irc():
    irc.stdin.write("notice #hacklab.jkl :Jääkaapin ovi on suljettu, kiitos!\n".encode())
    irc.stdin.flush()


while True:
    if GPIO.input(buttonPin):
        if time.time() >= t_end:
            notify_mattermost()
            notify_irc()
            alert = True
            t_end = time.time() + wait_seconds
            alertfade_time = time.time() + alert_wait
    else:
        t_end = time.time() + wait_seconds
        if alert and (time.time() >= alertfade_time):
            print('Alert off', flush=True)
            thanks_mattermost()
            thanks_irc()
            alert = False
    time.sleep(0.02)

from subprocess import Popen, PIPE

MATTERSEND_CONF = '/home/pi/techday/fridgebot/mattersend.conf'
DOOR_CLOSED_FILE = '/home/pi/techday/fridgebot/suljettu.txt'
DOOR_OPEN_FILE = '/home/pi/techday/fridgebot/auki.txt'

def notify():
    Popen(['mattersend', '--config', MATTERSEND_CONF, '-f', DOOR_OPEN_FILE])
    print('Alert sent to Mattermost', flush=True)

def thanks():
    Popen(['mattersend', '--config', MATTERSEND_CONF, '-f', DOOR_CLOSED_FILE])

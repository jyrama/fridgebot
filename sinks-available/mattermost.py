from urllib.request import Request, urlopen
from json import dumps


def init():
    global config, notify_data, thanks_data, headers, url

    headers = {'Content-Type': 'application/json'}
    notify_data = dumps({"text": config['notify_msg']})
    thanks_data = dumps({"text": config['thanks_msg']})
    url = config['url']


def mm(data):
    global url,  headers
    req = Request(url=url, data=notify_data, headers=headers, method='POST')
    urlopen(req)


def notify():
    global notify_data
    mm(notify_data)
    print('Alert sent to Mattermost', flush=True)


def thanks():
    global thanks_data
    mm(thanks_data)
    print('Alert sent to Mattermost', flush=True)

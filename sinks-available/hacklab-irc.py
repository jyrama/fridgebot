from subprocess import Popen, PIPE


def init():
    global config, irc, channel, notify_msg, thanks_msg

    proxy = config['proxy']
    channel = config['channel']
    startup_msg = config['startup_msg']
    startup_notice = "notice {} :{}".format(channel, startup_msg)
    notify_msg = config['notify_msg']
    thanks_msg = config['thanks_msg']

    irc = Popen(['ssh', '-T', proxy], stdin=PIPE)
    irc.stdin.write("pass freenode\nuser\nnick\n".encode())
    irc.stdin.write(startup_notice.encode())
    irc.stdin.flush()


def notify():
    global irc, channel
    irc.stdin.write("notice {} :{}\n".format(channel, notify_msg).encode())
    irc.stdin.flush()
    print('Alert sent to IRC', flush=True)


def thanks():
    global irc, thanks_msg
    irc.stdin.write("notice {} :{}\n".format(channel, thanks_msg).encode())
    irc.stdin.flush()

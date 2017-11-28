from subprocess import Popen, PIPE

irc = Popen(['ssh', '-T', 'hacklab-irc'], stdin=PIPE)
irc.stdin.write("pass freenode\nuser\nnick\n".encode())
irc.stdin.write("notice #hacklab.jkl :Fridgebot is alive".encode())
irc.stdin.flush()

def notify():
    irc.stdin.write("notice #hacklab.jkl :Pakastimen ovi on jäänyt auki!\n".encode())
    irc.stdin.flush()
    print('Alert sent to IRC', flush=True)

def thanks():
    irc.stdin.write("notice #hacklab.jkl :Pakastimen ovi on suljettu, kiitos!\n".encode())
    irc.stdin.flush()

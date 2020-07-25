import time
from blinker import signal


class Ping(object):
    def __init__(self):
        pass

    def ping(self):
        print('Ping!')
        time.sleep(2)


class Pong(object):
    def __init__(self):
        pass

    def pong(self):
        print('Pong!')
        time.sleep(2)


signal_ping = signal('signal_ping')
signal_ping.connect(Ping.ping)

signal_pong = signal('signal_pong')
signal_pong.connect(Pong.pong)

ping = Ping()
pong = Pong()

signal_ping.send()
signal_pong.send()

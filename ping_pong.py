import time
from blinker import signal


class Ping(object):
    def __init__(self):
        pass

    def action(self, sender):
        print('Ping!')
        time.sleep(1)
        signal('s_pong').send()


class Pong(object):
    def __init__(self):
        pass

    def action(self, sender):
        print('Pong!')
        time.sleep(1)
        signal('s_ping').send()


ping = Ping()
pong = Pong()

signal('s_ping').connect(ping.action)
signal('s_pong').connect(pong.action)

signal('s_ping').send()

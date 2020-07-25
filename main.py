import time


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


ping = Ping()
pong = Pong()

ping.ping()
pong.pong()

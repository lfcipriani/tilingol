from twython import TwythonStreamer
from jinglebells import JingleBells
import time
import threading

class GoalStream(TwythonStreamer):

    def configure(self, tpsThreshold, tpsLength):
        self.tpsThreshold = tpsThreshold
        self.tps = 0
        self.tpsLength = tpsLength
        self.tpsList = []
        self.tpsListMax = 20
        self.currentSec = 0
        self.ring = JingleBells(18)
        self.ringThread = threading.Thread(target = self.ring_the_bells, args=(self.ring, 12, 0.1,))

    def calculate_tps(self):
        if self.currentSec == 0:
            currentSec = int(time.time())
        if self.currentSec < (self.currentSec + self.tpsLength):
            self.tps = self.tps + 1
        else:
            self.tpsList.append(self.tps)
            self.tps = 1
            self.currentSec = int(time.time())

    def ring_the_bells(self, bell, iterations, speed):
        print("ring!")
        bell.shake(iterations, speed)

    def on_success(self, data):
        if 'text' in data:
            self.calculate_tps()

            if self.tps >= self.tpsThreshold:
                if not self.ringThread.isAlive():
                    self.ringThread = threading.Thread(target = self.ring_the_bells, args=(self.ring, 12, 0.1,))
                    self.ringThread.start()

            #created_at = data['created_at']
            #time.mktime(time.strptime(created_at,"%a %b %d %H:%M:%S +0000 %Y"))

            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code


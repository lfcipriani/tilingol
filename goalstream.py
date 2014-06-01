from twython import TwythonStreamer
from jinglebells import JingleBells
import time
import thread

class GoalStream(TwythonStreamer):

    def configure(self, tpsThreshold, tpsLength):
        self.tpsThreshold = tpsThreshold
        self.tps = 0
        self.tpsLength = 1
        self.tpsList = []
        self.tpsListMax = 20
        self.currentSec = 0
        self.ring = JingleBells(18)

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
                try:
                    thread.start_new_thread(self.ring_the_bells, (self.ring, 12, 0.1) )
                except:
                    print "Error: unable to start thread"

            #created_at = data['created_at']
            #time.mktime(time.strptime(created_at,"%a %b %d %H:%M:%S +0000 %Y"))

            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code


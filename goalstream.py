from twython import TwythonStreamer
from jinglebells import JingleBells
import time
import threading

SHAKES = 12
SPEED  = 0.1

class GoalStream(TwythonStreamer):

    def configure(self, threshold, window):
        self.threshold = threshold
        self.frequency = 0
        self.window = window
        self.currentSec = 0
        self.ring = JingleBells(18)
        self.ringThread = threading.Thread(target = self.ring_the_bells, args=(self.ring, SHAKES, SPEED,))

    def calculate_frequency(self):
        if self.currentSec == 0:
            self.currentSec = int(time.time())
        if time.time() < (self.currentSec + self.window):
            self.frequency = self.frequency + 1
        else:
            print "  ["+ str(self.currentSec) +"] tweets in the last "+ str(self.window) +" second(s) : " + str(self.frequency)
            self.frequency = 1
            self.currentSec = int(time.time())

    def ring_the_bells(self, bell, iterations, speed):
        print("\\o/ ring! ring! \\o/")
        bell.shake(iterations, speed)

    def is_tweet_valid(self, data):
        return True
        #if 'retweeted_status' not in data:
            #return True
        #else:
            #return False

    def on_success(self, data):
        if 'text' in data:
            if self.is_tweet_valid(data):
                self.calculate_frequency()

                if self.frequency >= self.threshold:
                    if not self.ringThread.isAlive():
                        self.ringThread = threading.Thread(target = self.ring_the_bells, args=(self.ring, SHAKES, SPEED,))
                        self.ringThread.start()

                #print "  >> @" + data['user']['screen_name'].encode('utf-8') + ": " + data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print "Erro: " + str(status_code) + str(data)


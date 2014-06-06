from twython import TwythonStreamer
from peak_detection import PeakDetection
import time
import threading

SHAKES = 12
SPEED  = 0.1

class GoalStream(TwythonStreamer):

    def configure(self, freq_window, moving_average_window, peak_threshold, debug=False):
        self.peak_detector = PeakDetection(freq_window, moving_average_window, peak_threshold)
        self.debug = debug
        if not debug:
            from jinglebells import JingleBells
            self.ring = JingleBells(18)
            self.ringThread = threading.Thread(target = self.ring_the_bells, args=(self.ring, SHAKES, SPEED,))

    def ring_the_bells(self, bell, iterations, speed):
        print("\\o/ ring! ring! \\o/")
        bell.shake(iterations, speed)

    def easteregg(self, data):
        return ("toqueosinopequenino" == data["entities"]["hashtags"][0]["text"])

    def on_success(self, data):
        if 'text' in data:
            self.peak_detector.collect_frequency()

            if self.peak_detector.is_this_a_peak() or self.easteregg(data):
                print "UEPA"
                if not self.debug:
                    if not self.ringThread.isAlive():
                        self.ringThread = threading.Thread(target = self.ring_the_bells, args=(self.ring, SHAKES, SPEED,))
                        self.ringThread.start()

            print data
            #print "  >> @" + data['user']['screen_name'].encode('utf-8') + ": " + data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print "Erro: " + str(status_code) + str(data)


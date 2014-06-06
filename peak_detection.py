import time
import sys
import logging

class PeakDetection:
    def __init__(self, freq_window, moving_average_window, peak_threshold):
        self.freq_window           = freq_window
        self.moving_average_window = moving_average_window
        self.peak_threshold        = peak_threshold
        self.frequency  = 0
        self.currentSec = 0
        self.data       = []
        self.eam        = []
        self.growth     = []
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler('data_'+str(int(time.time()))+'.log')
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def collect_frequency(self):
        if self.currentSec == 0:
            self.currentSec = int(time.time())
        if time.time() < (self.currentSec + self.freq_window):
            self.frequency += 1
        else:
            self.__update_window(self.frequency)
            self.frequency = 1
            self.currentSec = int(time.time())
        
    def is_this_a_peak(self):
        if len(self.growth) > 0:
            if self.growth[-1] > self.peak_threshold:
                return True
        return False

    def __update_window(self, frequency):
        data_entry = ""
        data_entry += str(self.currentSec)

        self.data.append(frequency)
        if len(self.data) > self.moving_average_window:
            self.data.pop(0)
        data_entry += "," + str(self.data[-1])

        if len(self.data) >= self.moving_average_window:
            if len(self.eam) == 0:
                self.eam.append(sum(self.data[0:self.moving_average_window])/float(self.moving_average_window)) 
            else:
                self.eam.append((self.data[-1]-float(self.eam[-1])) * (2/float(self.moving_average_window + 1)) + float(self.eam[-1]))
            if len(self.eam) > self.moving_average_window:
                self.eam.pop(0)
            data_entry += "," + str(self.eam[-1])

        if len(self.eam) >= self.moving_average_window:
            self.growth.append((self.eam[-1]-self.eam[0])/self.eam[0])
            if len(self.growth) > self.moving_average_window:
                self.growth.pop(0) 
            data_entry += "," + str(self.growth[-1])

        self.logger.info(data_entry)


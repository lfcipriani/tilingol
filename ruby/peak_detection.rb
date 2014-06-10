require "logger"

module Tilingol
  class PeakDetection
    def initialize(freq_window, moving_average_window, peak_threshold)
      @freq_window           = freq_window
      @moving_average_window = moving_average_window
      @peak_threshold        = peak_threshold
      @frequency  = 0
      @currentSec = 0
      @data       = []
      @eam        = []
      @growth     = []
      @logger     = Logger.new("data_#{Time.now.to_i}.csv")
      @logger.formatter = proc do |severity, datetime, progname, msg|
        "#{msg}\n"
      end
    end

    def collect_frequency
      now = Time.now.to_i
      @currentSec = now if @currentSec == 0
      if now < (@currentSec + @freq_window)
        @frequency += 1
      else
        update_window(@frequency)
        @frequency = 1
        @currentSec = now
      end
    end
        
    def is_this_a_peak?
      if @growth.size > 0
        return @growth.last > @peak_threshold
      end
      return false
    end

  private

    def update_window(frequency)
      data_entry = ""
      data_entry += @currentSec.to_s

      @data << frequency
      @data.shift if @data.size > @moving_average_window
          
      data_entry += "," + @data.last.to_s

      if @data.size >= @moving_average_window
        if @eam.size == 0
            @eam << @data[0..@moving_average_window].inject {|sum, i| sum + i } / @moving_average_window.to_f
        else
            @eam << (@data.last - @eam.last.to_f) * (2/(@moving_average_window.to_f + 1)) + @eam.last.to_f
        end
        @eam.shift if @eam.size > @moving_average_window
        data_entry += "," + @eam.last.to_s
      end

      if @eam.size >= @moving_average_window
        @growth << (@eam.last - @eam.first) / @eam.first.to_f
        @growth.shift if @growth.size > @moving_average_window
        data_entry += "," + @growth.last.to_s
      end

      @logger.info(data_entry)
    end

  end
end

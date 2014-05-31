require 'pi_piper'
include PiPiper

pin = PiPiper::Pin.new(:pin => 25, :direction => :out)
pin.on
sleep 10
pin.off

module Tilingol
  # Will call python program that has the pin connections to ring the bell
  class JingleBell
    def initialize
      @cmd = "sudo python ../jinglebells.py 20 0.05" #shake the bells
      @pid = nil
    end

    def ring!
      @pid = spawn(@cmd) if @pid.nil? || pid_not_running?(@pid)
    end

  private

    def pid_not_running?(pid)
      begin
        Process.kill(0,pid)
        false
      rescue Errno::ESRCH
        true
      end
    end

  end
end


module Tilingol
  # Will call python program that has the pin connections to ring the bell
  class JingleBell
    def initialize
      @cmd = "sudo python ./jinglebells.py 10 0.1" #shake the bells
      @pid = nil
    end

    def ring!
      @pid = spawn(@cmd) if @pid.nil? || pid_not_running?(@pid)
    end

  private

    def pid_not_running?(pid)
      res = `sudo ps -p #{pid.to_s}`
      !res.index("defunct").nil?
    end

  end
end


import os
import subprocess
import fcntl
import time

class Process(object):
    def __init__(self,command, template=False):
        self.command= command
        self.template= template

    def Start(self):
        self.process = subprocess.Popen(self.command.split(), \
                stderr = subprocess.PIPE, \
                stdout = subprocess.PIPE )
        self._setNonBlocking()

    def _setNonBlocking(self):
        fd = self.process.stderr.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    def isRunning(self):
        self.process.poll()
        if self.process.returncode==None:
            return True
        return False

    def Terminate(self):
        self.process.terminate()

    def Kill(self):
        self.process.kill()

    def ReadLine(self):
        line = ""
        self.process.stderr.flush()
        while(1):
            try: ch= self.process.stderr.read(1)
            except: return line
            if ch=="\n":
                return line
            line+=ch

    def ReadLines(self):
        lines= []

        while(1):
            line= self.ReadLine()
            if not line:
                return lines
            lines+= [line]

class StatusUpdateProcess(Process):
    def __init__(self, command, template=False):
        Process.__init__(self, command, template)

    def UpdateStatus(Process):
        pass



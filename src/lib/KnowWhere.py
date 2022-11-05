# KnowWhere lets the app know where to put things

import os
import sys

PLATFORM = os.name


class KnowWhere:
    def __init__(self):
        self.platform = PLATFORM
        self.home = os.path.expanduser("~")
        if self.platform == "nt":
            self.appdata = os.getenv("APPDATA")
            self.programdata = os.getenv("PROGRAMDATA")
            self.localappdata = os.getenv("LOCALAPPDATA")
            self.temp = os.getenv("TEMP")
        elif self.platform == "posix":
            self.appdata = self.home
            self.programdata = "/usr/share"
            self.localappdata = self.home
            self.temp = "/tmp"
        else:
            raise Exception("Unknown platform")
        # CREATE DIRECTORIES
        self.appdata = self.appdata + "/.cybfi"
        self.programdata = self.programdata + "/cybfi"
        self.localappdata = self.localappdata + "/.cybfi"
        self.temp = self.temp + "/cybfi"
        for path in [self.appdata, self.programdata, self.localappdata, self.temp]:
            if not os.path.exists(path):
                os.mkdir(path)
        # CREATE FILES
        self.STATUSOUT = self.temp + "/status.out"
        if not os.path.exists(self.STATUSOUT):
            open(self.STATUSOUT, "w").close()
        # CONSOLE
        self.STATUSOUT = self.temp + "/statusout"
        self.LOGOUT = sys.stdout

    def write_status(self, text):
        with open(self.STATUSOUT, "w") as f:
            f.write(text + "\r\n")
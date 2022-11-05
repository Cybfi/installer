from lib.Downloader import Downloader
from lib.KnowWhere import KnowWhere

kw = KnowWhere()
base_daemon_url = "https://github.com/cybfi/daemon/releases/latest/download/"

def UNIX():
    ddl = Downloader(base_daemon_url + "unix.zip", kw.programdata + "/daemon.zip")
    ddl.safe_download()

def WINDOWS():
    ddl = Downloader(base_daemon_url + "windows.zip", kw.programdata + "/daemon.zip")
    ddl.safe_download()



if __name__ == '__main__':
    if kw.platform == "posix":
        UNIX()
    elif kw.platform == "nt":
        WINDOWS()
    else:
        print("Unknown / Unsupported platform.")
        exit(1)
import os
import sys
from zipfile import ZipFile

from lib.Downloader import Downloader
from lib.KnowWhere import KnowWhere

base_daemon_url = "https://github.com/cybfi/daemon/releases/latest/download/"


def main(kw: KnowWhere):
    if kw.platform == "nt":
        ddl = Downloader(base_daemon_url + "windows.zip", kw.programdata + "/daemon.zip")
    elif kw.platform == "posix":
        ddl = Downloader(base_daemon_url + "unix.zip", kw.programdata + "/daemon.zip")
    else:
        raise Exception("Unknown platform")
    ddl.safe_download()

    # unzip
    with ZipFile(kw.programdata + "/daemon.zip", "r") as zipObj:
        zipObj.extractall(kw.programdata + "/daemon")


def permission_check(kw: KnowWhere):
    if kw.platform == "nt":
        # check if running as admin and if not, restart as admin
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            import subprocess
            subprocess.run(["powershell", "-Command", "Start-Process", "-Verb", "RunAs", "-FilePath", sys.executable,
                            "-ArgumentList", " ".join(sys.argv)])
            exit(0)
    elif kw.platform == "posix":
        # check if running as root and if not, restart as root
        if os.geteuid() != 0:
            print("Please run as root")
            exit(0)


if __name__ == '__main__':
    kw = KnowWhere()
    permission_check(kw)
    try:
        main(kw)
    except KeyboardInterrupt as e:
        kw.force_clean()

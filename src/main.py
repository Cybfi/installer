from lib.Downloader import Downloader
from lib.KnowWhere import KnowWhere

kw = KnowWhere()

def main():
    # url = "https://github.com/cybfi/daemon/releases/latest/download/package.zip"
    # url = "https://speed.hetzner.de/10GB.bin"
    url = "http://speedtest.tele2.net/10GB.zip"
    path = kw.temp + "/10GB.bin"
    downloader = Downloader(url, path)
    downloader.safe_download()


if __name__ == '__main__':
    main()

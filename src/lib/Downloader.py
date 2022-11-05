import os
import time

import requests as requests

from lib.KnowWhere import KnowWhere

kw = KnowWhere()

class Downloader:
    def __init__(self, url, path, update_interval=1):
        self.url = url
        self.path = path
        self.update_interval = update_interval

    def download(self):
        # Download the file and give update message: e.g. "Downloading @url to @path | 1.2 MB"
        r = requests.get(self.url, stream=True)
        size = int(r.headers.get("content-length", 0))
        dl = 0
        start = time.time()
        last_update = time.time()-self.update_interval
        with open(self.path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    dl += len(chunk)
                    speed = dl / (time.time() - start)
                    if time.time() - last_update > self.update_interval:
                        last_update = time.time()
                        if size > 0:
                            kw.write_status(f"DL:{self.url}->{self.path}:{round(dl/1024/1024,2)}MB:{round(speed/1024/1024,2)}MBs:{round(dl/size*100,2)}%:{round((size-dl)/speed,2)}s")
                            print(f"Downloading {self.url} to {self.path} | {dl / 1024 / 1024:.2f} MB ({dl/size*100:.2f}%) @ {speed / 1024 / 1024:.2f} MB/s, ETA: {((size - dl) / speed) / 60:.2f} minutes", end="\r")
                        else:
                            kw.write_status(f"DL:{self.url}->{self.path}:{round(dl/1024/1024,2)}MB:{round(speed/1024/1024,2)}MBs")
                            print(f"Downloading {self.url} to {self.path} | {dl/1024/1024:.2f} MB @ {speed/1024/1024:.2f} MB/s", end="\r")
                    f.write(chunk)
                    f.flush()

    def safe_download(self):
        if os.path.exists(self.path):
            i = 1
            while os.path.exists(self.path.split(".")[0] + f"({i})." + self.path.split(".")[1]):
                i += 1
            self.path = self.path.split(".")[0] + f"({i})." + self.path.split(".")[1]
        self.download()
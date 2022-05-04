import subprocess
import re
import json

class Short:
    def __init__(self, elem=None, url=None):
        self.elem = elem
        self.url = url
        self.shortId = re.search(r'shorts/(.*)?$', url).group(1)
        self.videoUrl = 'https://youtube.com/watch?v=%s' % self.shortId
        self.metadata = {}

    def get_metadata(self):
        proc = subprocess.run(['./youtube-dl', '-J', self.videoUrl], stdout=subprocess.PIPE)
        self.metadata = json.loads(proc.stdout.decode())
        return self.metadata


class ShortUnavailableException(Exception):
    pass
import re

class Short:
    def __init__(self, elem=None, url=None):
        self.elem = elem
        self.url = url
        search = re.search(".*/(?P<user>@.+?)/video/(?P<videoId>[0-9]+)", url)
        self.shortId = f"{search.group('user')}/{search.group('videoId')}"

class ShortUnavailableException(Exception):
    pass
import subprocess
import re
import json

class Short:
    def __init__(self, elem=None, url=None):
        self.elem = elem
        self.url = url

class ShortUnavailableException(Exception):
    pass
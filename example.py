from TikTokDriver import TikTokDriver
import os
from time import sleep
from shutil import rmtree
import json

# load the driver

driver = TikTokDriver(use_virtual_display=False)

results = driver.search('asmr', scroll_times=5)
print(len(results))
# for video in results:
    # print(video.url)
    # print(video.description)

driver.close()
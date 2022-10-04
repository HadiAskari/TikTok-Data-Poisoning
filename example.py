from TikTokDriver import TikTokDriver
import os
from time import sleep
from shutil import rmtree
import json

# load the driver

driver = TikTokDriver(use_virtual_display=True)

for video in driver.search('trump'):
    print(video.url)


driver.goto_shorts()

for i in range(10):
    print(driver.get_current_short().url)
    driver.next_short()
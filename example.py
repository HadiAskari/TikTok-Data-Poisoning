from YTShortDriver import YTShortDriver
import os
from time import sleep
from shutil import rmtree
import json

# load the driver

topics = [
    'weight loss',
    'jordan peterson',
    'sigma male'
]

if os.path.exists('screenshots'):
    rmtree('screenshots')

data = {}

for topic in topics:
    driver = YTShortDriver(browser='chrome', verbose=True)

    data[topic] = dict(training=[], testing=[])

    os.makedirs(os.path.join('screenshots', topic))

    shorts = driver.search(topic, scroll_times=10)


    print(len(shorts))

    for ind, short in enumerate(shorts[:30]):
        driver.play(short, duration=30)
        data[topic]['training'].append(driver.get_current_short().get_metadata())
        driver.save_screenshot(os.path.join('screenshots', topic, 'training%s.png' % ind))

    driver.goto_shorts()

    for ind in range(15):
        sleep(1)
        data[topic]['testing'].append(driver.get_current_short().get_metadata())
        driver.save_screenshot(os.path.join('screenshots', topic, 'testing%s.png' % ind))
        driver.next_short()

    driver.close()

    with open('data.json', 'w') as f:
        json.dump(data, f)
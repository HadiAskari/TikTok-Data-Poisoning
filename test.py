import pyktok as pyk
import json

tt_json = pyk.get_tiktok_json('https://www.tiktok.com/@tiktok/video/7011536772089924869?is_copy_url=1&is_from_webapp=v1')
key_id = list(tt_json['ItemModule'].keys())[0]
tt_json = tt_json['ItemModule'][key_id]

print(tt_json['id'])
print(tt_json['desc'])
print(tt_json['stats']['playCount'])


# id, desc, stats.playCount

import requests
import base64
import uuid
import random
import string
from config.endpoints import *

#POST

headers = {'accept': 'application/json','Content-Type': 'application/json'}
image_file = '206-2065273_spongebob-boi-png-jpg-royalty-free-library-clipart.jpg'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")
# img = {'media': open('6367374075618405841743017.jpg', 'rb').decode("utf8")}

def get_data():
    data = {"data": im_b64,
        "data_angle": 0,
        "data_format": 0,
        "data_id": "bd65600d-8669-4903-8a14-af88203add38",
        "data_side": 0,
        "data_type": 0,
        "device": "my_device",
        "lighting_strength": 0,
        "lighting_type": 0,
        "name": "test"
    }
    return data


r1 = requests.post(url=domain_beta + path_post, json=get_data(), headers=headers)
print("Beta text after posted:\n" + r1.text)

r2 = requests.post(url=domain_production + path_post, json=get_data(), headers=headers)
print("Production text after posted:\n" + r2.text)

#testCase

def test_data():
    ran_bool = bool(random.getrandbits(1))
    ran_integer = random.randint(3,10)
    ran_negative_num = random.randint(-10,-1)
    ran_float = random.random()
    ran_str = "".join(random.sample(string.ascii_letters + string.digits, 5))
    ran_str_max = "".join([random.choice("abcdefg") for _ in range(1026)])
    ran_symbol = random.choice('!@#$%^&*()')
    ran_uuid = str(uuid.uuid4())
    return [0, 1, ran_bool, ran_integer, ran_negative_num, ran_float, ran_str, ran_str_max, ran_symbol, ran_uuid]

for key in get_data().keys():
    for value in test_data():
        print("\n")
        print(key, value)
        # continue
        test_model = get_data()
        test_model[key] = value
        res = requests.post(url=domain_beta + path_post, json=test_model, headers=headers)
        print(res)
        print(res.text)


import json
import re

import requests
import time
import hashlib
from datetime import datetime

# 获取当前时间戳（以秒为单位）
timestamp = int(datetime.now().timestamp())

# 将时间戳转换为字符串
timestamp_str = str(timestamp)

access_key = '9279eeca82c461b7b086bab8f2af32e9'
api_key = 'cc87db821892d2ff423c640117e0a3c2'

# 计算第一个MD5哈希：md5($api_key.md5($timestamp))
inner_md5 = hashlib.md5(timestamp_str.encode()).hexdigest()
combined = api_key + inner_md5
final_md5 = hashlib.md5(combined.encode()).hexdigest()

token = final_md5
print(token)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    'access-key': access_key,
    'token': token,
    'timestamp': timestamp_str,
    'Content-Type': 'application/octet',
    'HTTP/1.1 Host': 'ss-api.mintegral.com',
}

params_1 = {
    "start_time": "2023-08-01",
    "end_time": "2023-08-01",
    "timezone": "+8",
    "type": 1,
    "dimension_option": "Offer,Campaign"
}

data_url = 'https://ss-api.mintegral.com/api/v2/reports/data'
# url2 = 'https://adv.mintegral.com/reports'

response = requests.get(url=data_url, headers=headers, params=params_1)
print(response.text)

params_2 = {
    "start_time": "2023-08-01",
    "end_time": "2023-08-01",
    "timezone": "+8",
    "type": 2,
    "dimension_option": "Offer,Campaign",

}

response_data = requests.get(url=data_url, headers=headers, params=params_2)
data = response_data.text
list1 = re.split(r'[\t,\n]', data)
print(data)
# print(list1)


def split_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size) if i + chunk_size <= len(input_list)]


chunk_size = 15  # 每组的大小
result = split_list(list1, chunk_size)
print(result)
for group in result:
    print(group)





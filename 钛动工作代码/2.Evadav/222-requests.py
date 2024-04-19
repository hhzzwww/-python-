import requests
import re
from selenium import webdriver

url = 'https://evadav.com/login'

# login接口中payload的csrf值
html = requests.get(url).text
csrf = re.findall(' <input type="hidden" name="md" value="(.*?)">', html)[0]
# print('csrf:', csrf)

# login接口中payload的recaptcha值
iframe_url = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Le4y6MZAAAAAE4T-7jZYVXRw4r9WZMCpkCsA03C&co=aHR0cHM6Ly9ldmFkYXYuY29tOjQ0Mw..&hl=zh-CN&v=SglpK98hSCn2CroR0bKRSJl5&size=invisible&cb=z6ihri5lof56'
iframe_response = requests.get(iframe_url)
print(iframe_response.text)
recaptcha_token = re.findall('<input type="hidden" id="recaptcha-token" value="(.*?)">', iframe_response.text)[0]
# print('recaptcha_token:', recaptcha_token)

# login登录
login_url = 'https://evadav.com/login'

headers = {
    "Origin": "https://evadav.com",
    "Referer": "https://evadav.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

from_data = {
    '_csrf': f'{csrf}',
    'reCaptcha': '{}'.format(recaptcha_token),
    'email': 'sarah.shi@tec-do.com',
    'password': '9yPs&z6/Y&?,'
}
response = requests.post(url=login_url, headers=headers, data=from_data)
print(response)








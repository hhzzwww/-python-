import re
import time
import requests
from selenium import webdriver
from requests.utils import dict_from_cookiejar
from requests.sessions import RequestsCookieJar
from selenium.webdriver.common.by import By
from requests.utils import dict_from_cookiejar
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # 无界面模式
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
# 模拟登录页面
driver.get('https://my.tacolo.co/signin')

driver.maximize_window()

driver.find_element_by_xpath('//div/input[@id="email"]').send_keys('838309518@qq.com')
time.sleep(1)

driver.find_element_by_xpath('//div/input[@id="passwordinput"]').send_keys('Aabb11223344!')
time.sleep(1)

driver.find_element_by_xpath('//div/button').click()

# cookies1 = driver.get_cookies()
# print(cookies1)
time.sleep(3)
# 保存cookie信息

# html_data = driver.page_source
# print(html_data)

cookies = driver.get_cookies()
print(cookies)


# 将之前selenium登录获取的cookie信息保存到requests的会话中

s = requests.session()
cookie = dict()
for item in cookies:
    cookie[item["name"]] = item["value"]

# print(cookie)

headers = {
    "authority": "my.tacolo.co",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "referer": "https://my.tacolo.co/signin?ReturnUrl=^%^2Fprofile",
    "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

login_url = 'https://my.tacolo.co/reportbycampaign'


# ses_cookies = driver.get_cookies()
# # print(ses_cookies)
# # 获取得到的Token
# token = ses_cookies[0]['value']
# print(token)
# # cookie_dict = dict_from_cookiejar(s.cookies)
# # print(cookie_dict)
#
res = s.post(url=login_url, headers=headers, cookies=cookie)
# time.sleep(2)
print(s.cookies)
# cookie_dict = dict_from_cookiejar(s.cookies)
# print(cookie_dict)
# time.sleep(3)

# print(res.text)

# driver.get(login_url)


# print(driver.page_source)







import re
import time
import requests
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 无界面模式
driver = webdriver.Chrome(chrome_options=chrome_options)
# 模拟登录页面
driver.get('https://my.tacolo.co/reportbycampaign')
driver.maximize_window()

driver.find_element_by_xpath('//div/input[@id="email"]').send_keys('838309518@qq.com')
time.sleep(0.5)

driver.find_element_by_xpath('//div/input[@id="passwordinput"]').send_keys('Aabb11223344!')
time.sleep(0.5)

driver.find_element_by_xpath('//div/button').click()

time.sleep(2)
# print(driver.page_source)

cookies = driver.get_cookies()
# print(cookies)


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

login_url = f'https://my.tacolo.co/reportbycampaign/get?startDate=2023-01-01&endDate=2023-06-16'

ses_cookies = driver.get_cookies()
# print(ses_cookies)
# 获取得到的Token
token = ses_cookies[0]['value']
print(token)
# cookie_dict = dict_from_cookiejar(s.cookies)
# print(cookie_dict)

res = s.post(url=login_url, headers=headers, cookies=cookie)
campaings = res.json()

for campaign in campaings:
    print(campaign)
    campaign_id = campaign['id']
    campaign_name = campaign['name']
    impressions = campaign['impressions']
    clicks = campaign['clicks']
    cost = campaign['cost']
    print(campaign_id, campaign_name, impressions, clicks, cost)

# driver.get(login_url)


# print(driver.page_source)
















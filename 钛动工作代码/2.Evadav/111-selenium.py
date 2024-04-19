import re
import time
import requests
from requests.utils import dict_from_cookiejar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = 'https://evadav.com/login'

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # 无界面模式
# driver = webdriver.Chrome(chrome_options=chrome_options)

html = requests.get(url).text
# print(html)
csrf = re.findall('<input id="csrf-token" type="hidden" name="_csrf" value="(.*?)">',html)[0]
print(csrf)


options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/114.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

# 防止被浏览器识别 --检查是否被识别的代码---window.navigator.webdriver
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                    """
})

# 模拟登录页面
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, '//div/button[@class="main-h__btn my-btn no-bg reset is-btn-login"]').click()
time.sleep(0.5)

driver.find_element(By.XPATH, '//div/input[@name="email"]').send_keys('sarah.shi@tec-do.com')
time.sleep(0.5)

driver.find_element(By.XPATH, '//div/input[@name="password"]').send_keys('9yPs&z6/Y&?,')
time.sleep(0.5)

driver.find_element(By.XPATH, '//div/button[@class="my-form__is my-btn reset"]').click()

time.sleep(2)
cookies = driver.get_cookies()
# print(cookies)

cookie = dict()
for item in cookies:
    cookie[item["name"]] = item["value"]

# print(cookie)
# 将cookiejar形式转化为字典
# cookie_dict = dict_from_cookiejar(s.cookies)
# print(cookie_dict)
token = cookie['_identity-front']
# print(token)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Referer': 'https://evadav.com/login'

}
data = {

    "columns[0][data]": "campaignId",
    "columns[0][name]": "",
    "columns[0][searchable]": "true",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "function",
    "columns[1][name]": "campaign",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "false",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "impressions",
    "columns[2][name]": "",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "clicks",
    "columns[3][name]": "",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "ctr",
    "columns[4][name]": "",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "cpc",
    "columns[5][name]": "",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "cost",
    "columns[6][name]": "",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "leads",
    "columns[7][name]": "",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "cpl",
    "columns[8][name]": "",
    "columns[8][searchable]": "true",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "payout",
    "columns[9][name]": "",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "columns[10][data]": "profit",
    "columns[10][name]": "",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",
    "columns[11][data]": "roi",
    "columns[11][name]": "",
    "columns[11][searchable]": "true",
    "columns[11][orderable]": "true",
    "columns[11][search][value]": "",
    "columns[11][search][regex]": "false",
    "columns[12][data]": "function",
    "columns[12][name]": "winRate",
    "columns[12][searchable]": "true",
    "columns[12][orderable]": "true",
    "columns[12][search][value]": "",
    "columns[12][search][regex]": "false",
    "order[0][column]": "6",
    "order[0][dir]": "desc",
    "start": "0",
    "length": "30",
    "search[value]": "",
    "search[regex]": "false",
    "_csrf": f"{csrf}",
    "filter[period]": "01.05.2023 - 31.05.2023",
    "filter[format]": "all",
    "filter[pricing]": "all",
    "filter[os]": "all",
    "filter[browser]": "all",
    "reDrawCharts": "true"
}

login_url = 'https://evadav.com/ajax/adv/statistics/campaign'
res = requests.post(url=login_url, headers=headers, cookies=cookie, data=data).json()
# print(res)
res_data = res['data']['data']
for data in res_data:
    campaign = data['campaign']
    cost = data['cost']
    print(campaign, cost)





















import csv
import re
from selenium.webdriver.common.by import By
from requests.utils import dict_from_cookiejar
from selenium import webdriver
import time
import requests

url = 'https://portals.aliexpress.com/unify.htm?DailyReport=Report'

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                    """
})

driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH, '//span/input[@label="Email"]').send_keys('nora.liang@tec-do.com')
time.sleep(0.5)

driver.find_element(By.XPATH, '//span/input[@label="Password"]').send_keys('mobisummer123')
time.sleep(0.5)

driver.find_element(By.XPATH, '//button[@aria-label="Sign in"]/span').click()

time.sleep(5)

# # 定位滑块元素和滑块背景元素
# slider = driver.find_element(By.XPATH,'//div/span[@class="nc_iconfont btn_slide"]')
# slider_background = driver.find_element(By.XPATH,'//div/span[@class="nc-lang-cnt"]')
#
# # 获取滑块的初始位置和宽度
# slider_width = slider.size['width']
#
# # 创建 ActionChains对象
# action_chains = ActionChains(driver)
#
# # 将滑块拖动到目标位置
# action_chains.click_and_hold(slider).move_by_offset(slider_width, 0).release().perform()
#
# # 等待一段时间，观察验证是否成功
# time.sleep(5)

# 关闭弹窗
# driver.find_element(By.XPATH, '//div/span[@class="upgrade-close"]').click()
# time.sleep(1)

# # 刷新页面
# driver.find_element(By.XPATH, '//div/a[@class=" current-nav-a"]/span').click()
# time.sleep(1)

cookies = driver.get_cookies()
# print(cookies)

cookie = dict()
for item in cookies:
    cookie[item["name"]] = item["value"]

# print(cookie)

# data_url中需要用到的csrf_token储存在第一个url的cookie中,取出即可
# 后续爬虫可以查看csrf_token是否属于回调参数---前面网页接口已经出现过

csrf_token_text = cookie['acs_usuc_t']
csrf_token = re.findall('x_csrf=(.*?)&acs_rt=(.*?)', csrf_token_text)[0][0]
# print(csrf_token)
headers = {
    "Pragma": "no-cache",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
ses = requests.Session()
ses.post(url=url, cookies=cookie, headers=headers)

# print(ses.cookies)
ses_cookies = dict_from_cookiejar(ses.cookies)
# print(ses_cookies)
data_url = 'https://portals.aliexpress.com/cpi/report/daily.do'

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Length": "103",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://portals.aliexpress.com",
    "Referer": "https://portals.aliexpress.com/unify.htm?DailyReport=Report",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Xsrf-Token": "{}".format(csrf_token)
}

json = {
    "pageNum": "1",
    "pageSize": "50",
    "timeBeg": "2023-05-30",
    "timeEnd": "2023-06-29",
    "_csrf_token_": "{}".format(csrf_token)
}
data_cookie = {'isg': 'BJaWMtCD7tG1jtp12TnsjwQa50yYN9pxUqctfAD_lnkUwzRdaMUigajxX18v7tKJ',
               'l': 'fBOSEGMPNkNI9DUQXOfCEurza779bIR4SuPzaNbMi9fPOp5v5LYeX1_YChLJCnGVesZpR3lDK4dwBzY1uyCV-JTFkteq1do-FwIvEn3A.',
               'x-hng': 'lang=en-US',
               'JSESSIONID': '4E116CF001D421C2D4377D16B7F3D1AE',
               'xman_t': 'nonj5Nhj6GmSmrYMr5LTk522hQxi/mJ1WrfvB6CAsv0fU7frTseY+0y2dUIrEfJYd1XnyNrn+F6tEjUGf31OswOD3pbHl3RuBHSzUvaL8u3lxAXWXJY+xl65hKuL2e9/WeaV9RaPE7melBJyUpccR1f4L/jlFNuZ0l7ACMYGA0dHnGC/AdBi2MtAuTBixON56k203XLksGwYWcDx2NYgUgQ7rNIP8/7ocLFrWyJvS30pSuQWat7hcv+RkvzfjN7yul8DQmU6/qCxdWrKd1W5HlcBIsatvMjKyRa7UafoexpZ+d0wKKBMD07SQiZaJ7rfkQIH+LlKqBgs/sfFja1P4qbNVqdAs8kT8ODmWD3Dxjg3KxTNCPxwOgU3CKBNRDQZDqVLe4N+wMhySd1oYjWAmr/cJ7lpg7XEPD4mqs1sIusUqsOL/PF4wRk25CfHq/0k+ftzq6ebgLAH8hKVPbpGQYDGATyujZM28sb5ZwErrDfevWkOuh6J+v/BKbHt+uTh1HCAT7nprpJoRboXJzWz0fE1do5yFv6HE9iJhYHc2Irem/z9w4W7fGfdjUAB0D8JQMl1ZFzoTNRCOeEfveHXwbEfoPiqc8cfsKC+zQUct+DDuH2nfF/ZKqEdu6NQZV0Jygv/RkGUU4KmScFVcRDj8Lk3TnfvdQSU9Pb9nJvYR9KFIhbBs5KHIRb1O6gnrupAksHt72JTLPvNnh4vEjX/eyJjEBHauTGSUjFHQ21gGztRSZVEtlF15FTg795GS9YK',
               'tfstk': 'cUblB7qe_g-WTaUdhTT7yM9l7BLlZIgeIw7fuW7JFmSWzh_Vi0mqbPYaiL2_UD1..',
               'aep_common_f': 'qBGo9AB8amRzALuaiGLom8MsD9U83lHB/Wshb4SSrDQkrXl2JsWi2A==',
               'sgcookie': 'E100QRbRbHvWEJfA80RZdX+biXGoTDiNDIKFz+Axsl3JiYPoft6aRZSblglO/6Zv6XUaQJ9JrfzINbHyKhm9+y2I/5loVZtwbXYJ3bOx+5jWoms=',
               'xman_f': 'R5Qfg/IicZSVuHOLzXh3xCxjUbCNJAnLzoHP7n5LhxuZ3j/doCPtPfRf9wxaaTyzvRS499EPFQPdG4vs+rsSeTcwjbfacGrYr9Gdj/7xeuqWThCWZyn8Kslcc9eoX+ihjlLqrGEJtLlBaCcMTUlh9qwJxaEQprE0QT5yEcs3hlc2kwcTj78cGX/wflVBSZsYqnn2PuwlzNcaDg1aT4bR4nAuJDaiwVbnO3z5fylbvoHV18fAr0xBNZp+fGmTcCD/+ixYr+Beg/wvQTLymaDNPhCMHfBQitNTpt3aLxfC+BG6p0dMFsXeDN6SaCkRUPq7f46bCDaNkQteca158GBY+UBIfOtl0JjTZcvKrpbc69b+K3ap55zKyf8rGCLXSBpf+SeKlbWTaVZhC/cH+ifDICVUsufzscKH',
               'x_router_us_f': 'x_alimid=2661531430',
               'havana_tgc': 'NTGC_47f1f860ba8f296ac160cda92387a064',
               'intl_common_forever': 'blTkka+HzlDEtH+FzpxuVMDFYVbR+ka8KgvKG2mB7gior75/6fkXwA==',
               'xlly_s': '1',
               'ali_apache_track': '',
               '_hvn_login': '13',
               'xman_us_f': 'zero_order=y&x_locale=en_US&x_l=0&x_user=US|nora.liang|user|ifm|2661531430&x_lid=us1061881223wbxae&x_c_chg=1&acs_rt=531ba09d6c7240d99e25618452eb8ce5',
               'intl_locale': 'en_US',
               'cna': 'Vdc3Hc4jOVECAWeMnE2uhEEE',
               'acs_usuc_t': 'x_csrf={}&acs_rt=531ba09d6c7240d99e25618452eb8ce5'.format(csrf_token),
               'aep_usuc_f': 'site=glo&b_locale=en_US&isb=y&x_alimid=2661531430&isfb=y',
               'ali_apache_tracktmp': '',
               'xman_us_t': 'x_lid=us1061881223wbxae&sign=y&rmb_pp=nora.liang@tec-do.com&x_user=AwX9btZuL7P9ghKntIyrjz7kRoTX/7shizBcWW+uE6w=&ctoken=16c2s8pcm6n7d&l_source=aliexpress',
               'ali_apache_id': '33.22.97.136.1689315668479.607236.5'}
response = requests.post(url=data_url, json=json, headers=headers,cookies=data_cookie).json()
# print(response)
#
data_list = response['data']['dailyReportVOList']
# print(data_list)
for data in data_list:
    Valid_activation = data['normalCnt']

    print(Valid_activation)




import re
import time
import requests
from selenium import webdriver


class Login:
    def __init__(self):
        self.driver = None
        self.cookies = None
        self.ses = requests.session()

    def login(self):
        self.driver = webdriver.Chrome()
        # 执行登录等操作
        self.driver.get('https://my.tacolo.co/signin')
        self.driver.find_element_by_xpath('//div/input[@id="email"]').send_keys('838309518@qq.com')
        time.sleep(1)

        self.driver.find_element_by_xpath('//div/input[@id="passwordinput"]').send_keys('Aabb11223344!')
        time.sleep(1)

        self.driver.find_element_by_xpath('//div/button').click()
        time.sleep(3)

        # 获取当前会话的 Cookies
        self.cookies = self.driver.get_cookies()
        print(self.cookies)

        cookie = dict()
        for item in self.cookies:
            cookie[item["name"]] = item["value"]

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

        url = 'https://my.tacolo.co/profile'
        res = self.ses.post(url=url, headers=headers, cookies=cookie)
        print(res)

        # return self.ses.post(url, headers=headers, cookies=cookie)

    def parse_response(self):
        try:
            ses_cookies = self.cookies
            token = ses_cookies[0]['value']
            print(token)
            return True
        except Exception as e:
            print(e)


# 创建类实例
my_instance = Login()

# 登录并维持会话
my_instance.login()

# 在另一个函数中使用 Cookies
my_instance.parse_response()

# 关闭浏览器驱动























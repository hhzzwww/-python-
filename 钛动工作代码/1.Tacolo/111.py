import time
import requests
from selenium import webdriver
from requests.sessions import RequestsCookieJar
from selenium.webdriver.common.by import By


class login:

    def __init__(self):
        self.session = requests.Session()
        self.driver = webdriver.Chrome()

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Referer': 'https://my.tacolo.co/signin?ReturnUrl=%2Fprofile'

        }

    def login_simulation(self):
        self.driver.get('https://my.tacolo.co/signin?ReturnUrl=%2Fprofile')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        """输入用户名和密码"""
        self.driver.find_element_by_xpath('//div/input[@id="email"]').send_keys('838309518@qq.com')
        time.sleep(1)

        self.driver.find_element_by_xpath('//div/input[@id="passwordinput"]').send_keys('Aabb11223344!')
        time.sleep(1)

        self.driver.find_element_by_xpath('//div/button').click()


    # 维持会话
    def get_cookie(self):
        # 此时已进入最终目标页面，可以直接获取最终目标页面的cookie
        cookies = self.driver.get_cookies()

        s = self.requests.session()
        c = self.requests.cookies.RequestsCookieJar()
        for item in cookies:
            c.set(item['name'], item['value'])

        # 将cookies更新为登录后的cookies
        cookies_login = s.cookies.update(c)

        login_url = 'https://my.tacolo.co/profile'

        res = self.session.get(url=login_url, cookies=cookies_login, headers=self.headers)

        print(res.text)


ll = login()
# ll.login_simulation()
ll.get_cookie()

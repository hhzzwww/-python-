import base64
import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# from constants import BILIBILI_USERNAME, BILIBILI_PASSWORD


driver = webdriver.Chrome()
driver.get('https://my.tacolo.co/signin?ReturnUrl=%2Fprofile')
driver.implicitly_wait(10)
driver.maximize_window()

"""输入用户名和密码"""
driver.find_element_by_xpath('//div/input[@id="email"]').send_keys('838309518@qq.com')
time.sleep(0.5)

driver.find_element_by_xpath('//div/input[@id="passwordinput"]').send_keys('Aabb11223344!')
time.sleep(0.5)


driver.find_element_by_xpath('//div/button').click()

time.sleep(2)
# 此时已进入最终目标页面，可以直接获取最终目标页面的cookie
# cookie_tag = driver.get_cookies()
# print(cookie_tag)

s = requests.session()
login_url = 'https://my.tacolo.co/profile'

login_ret = s.post(login_url,headers = header,)





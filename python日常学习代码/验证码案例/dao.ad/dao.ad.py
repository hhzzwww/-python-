import base64
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from constants import DAO_USERNAME, DAO_PASSWORD


driver = webdriver.Chrome()
driver.get('https://my.tacolo.co/profile')
driver.implicitly_wait(10)
driver.maximize_window()


# 输入用户名和密码 点击

driver.find_element_by_xpath('//div/input[@id="email"]').send_keys('838309518@qq.com')
driver.find_element_by_xpath('//div/input[@id="passwordinput"]').send_keys('Aabb11223344!')

time.sleep(3)

driver.find_element_by_xpath('//div/button/span').click()




















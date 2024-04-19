"""selenium以此点击列表页标签对象"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://cs.lianjia.com/ershoufang/')
driver.maximize_window()
driver.implicitly_wait(10)

# 第一次进去获取所有标签对象
lis = driver.find_elements(By.CSS_SELECTOR, '.clear.LOGCLICKDATA')
# print(lis)
# print(len(lis))


j = 1
for i in range(len(lis)):
    # 满足此条件需要重新获取列表页标签对象,
    # 因为列表页从第二次点击开始会是旧页面数据, 会有元素过期的问题, 下放代码刷新页面可以解决旧页面元素过期的问题
    if j != 1:
        lis = driver.find_elements(By.CSS_SELECTOR, '.clear.LOGCLICKDATA')

    # 获取详情页标签对象点击, 会打开新的浏览器窗口
    # 打开后会有两个窗口, 一个列表页窗口, 一个详情页窗口, 并且点击后会自动切换到详情页窗口
    # 详情页信息采集完了, 可以关闭, 那么就到了列表页窗口
    lis[i].find_element(By.CSS_SELECTOR, '.title>a').click()
    time.sleep(1)
    with open('a.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    # 步骤1: 获取窗口句柄
    windows = driver.window_handles
    # 步骤2: 切换到新窗口
    driver.switch_to.window(windows[-1])

    price = driver.find_element(By.CSS_SELECTOR, '.area>div.mainInfo').text  # 获取详情页中的房子价格
    print(price)

    driver.close()  # 关闭详情页窗口

    driver.switch_to.window(windows[0])  # 关闭后将窗口句柄切换到第一个窗口
    driver.refresh()  # 刷新当前页面, 不然会导致就业面元素过期

    j = 0  # 第一个数据详情页采集完后修改 i 的值

input()
driver.quit()

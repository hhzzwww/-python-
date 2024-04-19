import csv

from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

# selenium模拟登录,维持登录信息

driver = webdriver.Chrome()

driver.get('https://hq1.appsflyer.com/partner-marketplace/explore/trending')
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH, '//label/input[@aria-label="user-email"]').send_keys('noah.lin@hellocutty.com')
time.sleep(0.5)

driver.find_element(By.XPATH, '//label/input[@aria-label="Password"]').send_keys('.5viKR?5KmPYXQw')
time.sleep(0.5)

driver.find_element(By.XPATH, '//button/span').click()

time.sleep(2)

cookies = driver.get_cookies()
# print(cookies)

# 将之前selenium登录获取的cookie信息保存到requests的会话中,并转化为字典形式

cookie = dict()
for item in cookies:
    cookie[item["name"]] = item["value"]

# 使用维持会话的信息，访问目标数据的api接口
# 目标数据api接口
for page in range(0, 56):
    login_url = f'https://hq1.appsflyer.com/partner-marketplace/exploration/search/partners?type=trending&page={page}&preview=false'

    headers = {
        # "Accept": "application/json",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        # "Cache-Control": "no-cache",
        # "Content-Length": "91",
        # "Content-Type": "application/json",
        # "Origin": "https://hq1.appsflyer.com",
        # "Pragma": "no-cache",
        # "Referer": "https://hq1.appsflyer.com/partner-marketplace/explore/trending",
        # "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        # "Sec-Ch-Ua-Mobile": "?0",
        # "Sec-Ch-Ua-Platform": "\"Windows\"",
        # "Sec-Fetch-Dest": "empty",
        # "Sec-Fetch-Mode": "cors",
        # "Sec-Fetch-Site": "same-origin",
        # "Traceparent": "00-00000000000000006155d19db2687210-43238242698f0410-00",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    # 第一页有两个相同login_url地址,使用请求体数据payload区分
    # HTTP请求中不同的请求方式和设置不同的Content-Type时，参数传递的方式会不一样，一起了解这三种形式：Query String Parameters-查询字符串参数、Form Data、Request Payload；
    """
    Query String Parameters：查询字符串参数 --对应params
    Form Data:表单数据、 --对应data
    Request Payload：请求负载 --对应json
    """

    requests_payload = {
        'orderBy': {'rankByGrowth': "desc"}, 'extraParams': {'excludePartners': []}, 'showActive': f'alse'
    }

    response = requests.post(url=login_url, headers=headers, cookies=cookie,json=requests_payload).json()
    # print(response)
    data_names = response['data']
    # print(data_names)

    for data_name in data_names:
        name = data_name['details']['name']
        print(name)
        with open('appsflyer.csv', mode='a', encoding='utf-8', newline='') as f:
            # 创建 CSV writer 对象
            csv_write = csv.writer(f)
            # 写入数据行
            csv_write.writerow([name])

    print('---------第{}爬取完成--------------'.format(page))

    time.sleep(1)







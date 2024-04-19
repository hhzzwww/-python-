# -*- codeing = Utf-8 -*-
# @Time :2023/5/15 19:40
# @Author :ZunKki
# @File :python高级开发.py
# @Software: PyCharm
# 学号：120771

import requests

def get_proxy():
    url = 'http://zltiqu.pyhttp.taolop.com/getip?count=3&neek=76847&type=2&yys=0&port=2&sb=&mr=2&sep=0&city=440100'
    response = requests.get(url=url)
    json = response.json()
    print(json)
    # ip = json['data'][0]['ip']
    # port = str(json['data'][0]['port'])
    # proxies = {
    #     'http': 'http://' + ip + ':' + port,
    #     'https': 'http://' + ip + ':' + port,
    # }
    #
    # print('构建好的代理：', proxies)
    # return proxies


if __name__ == '__main__':
    proxies = get_proxy()
    response = requests.get(url='https://www.baidu.com', proxies=proxies)
    # print(response.text)


# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
# # 代理ip
# proxy = '175.147.100.36:64256'
# # 设置代理
# chrome_options.add_argument('--proxy-server=%s' % proxy)
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.douban.com')
# print(driver.page_source)

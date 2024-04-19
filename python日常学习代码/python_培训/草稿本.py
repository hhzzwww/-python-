# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2022/1/19 22:58
# @Author:86151
# @Site:
# @File:草稿本.py
# @Software:PyCharm
'''
import requests
import re
import pprint
import json
url ='https://image.so.com/j'

def get_params(page):
    params = {
        'callback':' jQuery183022264942468620963_1642605177533',
        'q':' 风景',
        'qtag':' ',
        'pd':' 1',
        'pn':' 60',
        'correct':' 风景',
        'adstar':' 0',
        'tab':' all',
        'sid':' 742f382c4e600fea3601a26fda0d5cd7',
        'ras':' 0',
        'cn':' 0',
        'gn':' 0',
        'kn':' 0',
        'crn':' 0',
        'bxn':' 0',
        'cuben':' 0',
        'pornn':' 0',
        'manun':' 0',
        'src':' srp',
        'color':' pink',
        'sn':page,
        'ps':page,
        'pc':' 60',
        '_':' 1642605323271',
    }
    return params

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'

}
for i in range(60,181,60):
    params = get_params(i)
    response = requests.get(url = url,headers = headers,params=params).text
    # 得出的json_data为str类型
    for j in range(3,6):
        json_ = 'jQuery183022264942468620963_164260517753'+str(j)+'\((.*?)\)'
        json_data = re.findall(json_,response,re.S)
        json_data = json_data[0]
        # print(type(json_data)) #得出字符串类型的json_data
        json_data1 = json.loads(json_data) #将str类型数据转化为字典对象
        # pprint.pprint(json_data1)

        list_data = json_data1['list']
        # print(list_data)
        for data in list_data:
            img_urldata = data['img']
            print(img_urldata)
        print('*'*100)

'''
import csv
import time

'''
# 猫眼电影排行爬取--保存为json数据格式


import requests
import parsel
import time
import json

#找数据对应的地址
url = 'https://www.maoyan.com/board/4'

def page_params(page):
    params = {
        'timeStamp':' 1643029316911',
        'channelId':' 40011',
        'index':' 3',
        'signKey':' 6a7674923b26b7d092d2396e712dc16c',
        'sVersion':' 1',
        'webdriver':' false',
        'offset': page
}
    return params


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


json_list = []

for page in range(0,91,10):
    time.sleep(2)
    params = page_params(page)

#请求数据
    response = requests.get(url = url,params = params,headers = headers)
    html_data = response.text

# print(html_data)

#数据解析
    selector = parsel.Selector(html_data)  #-----转换数据类型，使其可用parsel中的css进行解析
    dds = selector.css('.board-wrapper>dd') #所有的dd标签

    for dd in dds:
        title = dd.css('.name a::text').get()
        star  = dd.css('.star ::text').get().strip()
        releasetime = dd.css('.releasetime ::text').get()
        score = dd.css('.score ::text').getall()
        # score = score[0]+score[1]
        score = ''.join(score)

        # print(title,star,releasetime,score)
        d = {'电影名字':title,'主演':star,'上映时间':releasetime,'评分':score}
        json_list.append(d)

print(json_list)
#序列化操作
#ensure_ascii=False---拒绝json的unicode编码，因为中文不接受unicode
json_str = json.dumps(json_list,ensure_ascii=False)
with open('data.json',mode = 'w',encoding = 'utf-8') as f:
    f.write(json_str)

'''

'''
豆瓣电影250排行爬取--保存到excel文件

import requests
import parsel
import time
import openpyxl

work_book = openpyxl.Workbook() #创建工作簿
sheet = work_book.create_sheet('豆瓣250') #创建工作表

for page in range(0,251,25):
    time.sleep(5)
    url = 'https://movie.douban.com/top250?start={}'.format(page)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    response = requests.get(url = url,headers = headers)
    html_data = response.text
    # print(html_data)


    selector = parsel.Selector(html_data)

    lis = selector.css('.grid_view>li')

    for li in lis:
        title = li.css('a span ::text').getall()
        title1 = title[0] +title[1]
        info = li.css('.bd ::text').getall()
        info1 = info[1].strip()
        star = li.css('.star ::text').getall()
        score = star[2]
        follow = star[5]

        print(title1,info1,score,follow)
        # print(type(title1))
        sheet.append([title1,info1,score,follow])
work_book.save('豆瓣250.xlsx')

'''

'''
a = {'x': 5, 'k': 6, 'b': 5}
for key in a.keys():
    print(a[key])
'''

'''
前程无忧----爬取职位----使用csv模块储存数据--保存为csv文件

import requests
import re
import json
import pprint
import csv
import time

f = open('前程无忧.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['公司名字', '职位名字', '地区', '经验', '学历', '薪资', '招聘详情页'])
csv_writer.writeheader()

for page in range(1,21):
    print(f'==============================正在爬取第{page}页数据内容=============================================')
    time.sleep(1.5)
    url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,{page},1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'Cookie': '_uab_collina=164473615882505859344207; partner=sem_pcbaidupz_2; guid=4031bbdcf87745af70520f3825371dbc; _ujz=MTkyMTQ1NzU4MA%3D%3D; ps=needv%3D0; 51job=cuid%3D192145758%26%7C%26cusername%3DSnNo0JmukzODfT0afCHIVhq8B2l89zLpbN1CjP%252FJFyU%253D%26%7C%26cpassword%3D%26%7C%26cname%3DtUmkPEg15YMSDHjDbNaFMQ%253D%253D%26%7C%26cemail%3DbgedWmG58HzA%252FI5EfkW9BGGxm2AeW7w1IUUJsoCpM0k%253D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0gcC6vfckM5Q%26%7C%26cconfirmkey%3D22WXEshx.KkVs%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D22RU.s%252FDo%252F0WQ%26%7C%26to%3D563740f5741e30764260e4a9a7791ceb6208ae98%26%7C%26; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20220213%26%7C%26securetime%3DBDgBNFU3VTVXMlNuXGEPZVdhCj8%253D; privacy=1644736155; acw_tc=2f624a5216447361563004766e1007a686f2cd3c833c0b5008a5d09f366f1f; acw_sc__v2=6208ae9eef906500fd45b163dbe321f63c11616a; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%FD%BE%DD%B7%D6%CE%F6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; ssxmod_itna=QqAxyDcDgGDQ6bxl+D+rFx9itwCPxD5mNjjiQD/DpDnqD=GFDK40oE7+0KoDO8SgYmhWtKGxhvWh9j3OIWKScdawfWmDB3DEx06xZmG4iicDCeDIDWeDiDG4GmS4GtDpxG=Dj0FUZMUxi3Dbh=Df4DmDGY9QqDgDYQDGMp6D7QDIw6QKAx9bCLKLLRgKY23fG=DjMbD/4xFMQRFs6hZbjnTwE5qD0psB6+5B1AzWi0WQqGybKGuULt/SfbzsLNlen54bE54mGvzixhaKA+iWGGKlAkdfDQq9BxoKihiKhlyM/4zn5DA4/+0WxxD=; ssxmod_itna2=QqAxyDcDgGDQ6bxl+D+rFx9itwCPxD5mNjjiG9iuWDBude7PmxDO+ciQ8x8xoIHpKBRnuD0xeMplHp1x2rDyU32f=WTLwaWQ6pj8a193qtOOdMnkSmwXcjYFXR5udE1plmSudszvsSAGGL5OBoj/SRtjzf+kjTfSfBUxDj5iif6+tn08S3LG3dANkCNbXj3ZSL+f08TFwhrWxSKiveAYklUnnPY45eA64gR5Nku8zW=kXqFoOF9GzlnAqzchBo6==WupDbjKwcLiffIQUrhi9OAkYAYh4sQUGsv8tbF4/rFbGXYqmbFqQeHrKqpLFiDq6PSOY2BUkYL5SpFpvo+G3n+oFhh1AQYAS=mxAwxWYGWK6gL7j2y25az6sjrPpeaIfmB4zeu7nALouzAAfjrKIRzlNhRqManYU2mzE0EG=6vm7whFR+/qwFcf6rL/U=/QmS6hna0/ckFnMYqHC6yEtWtjL1ea4eOeHF9w5aKpba2ffZ/RERyVSHahv=U5EW7mmbWDG2f2DWDxz2iCiQKDejRwwlDf4p6CH05DFqD+cDxD'
    }
    response = requests.get(url = url,headers = headers).text
    # print(response)
    html_data = re.findall('<script type="text/javascript">(.*?)</script>',response,re.S)[0]
    html_data = html_data.replace('window.__SEARCH_RESULT__ = ','')
    # print(html_data)
    json_data = json.loads(html_data)["engine_jds"]
    # pprint.pprint(json_data)
    for index in json_data:
        company_name = index['company_name']
        job_name     = index['job_name']
        job_href     = index["job_href"]
        providesalary_text = index['providesalary_text']
        area = index['attribute_text'][0]
        job_exp = index['attribute_text'][1]
        job_edu = index['attribute_text'][2]
        # print(company_name)
        dic = {
            '公司名字': company_name,
            '职位名字': job_name,
            '地区': area,
            '经验': job_exp,
            '学历': job_edu,
            '薪资': providesalary_text,
            '招聘详情页': job_href,

        }

        csv_writer.writerow(dic)
        print(company_name,job_name,area,job_exp,job_edu,providesalary_text,job_href,sep = ' ')

'''
'''
批量爬取--绝对领域--图片数据--使用os模块储存数据


import requests
import parsel
import os

url = 'https://www.jdlingyu.com/tuji'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'

}

response = requests.get(url = url,headers = headers)
html_data = response.text

selector = parsel.Selector(html_data)

lis = selector.css('.post-list-item.item-post-style-1')

for li in lis:
    title = li.css('h2 a ::text').get()
    # print(title)
    href = li.css('h2 a::attr(href)').get()
    # print(href)
    """如果python文件夹没有该图片数据文件夹，就将图片数据所在的文件夹加载入python文件夹，"""
    if not os.path.exists(f'python_data\\{title}'):
        os.mkdir(f'python_data\\{title}')

    html_data1 = requests.get(url = href,headers = headers).text
    # print(html_data1)

    selector = parsel.Selector(html_data1)
    img_urls = selector.css('.entry-content img::attr(src)').getall()
    # print(img_urls)
    for img_url in img_urls:
        img_data= requests.get(url = img_url,headers = headers).content
        img_name = img_url.split('/')[-1]
        with open(f'python_data\\{title}\\' +img_name,mode = 'wb') as f:
            f.write(img_data)
            print('下载完成',img_name)
            
'''
'''
#导入浏览器模块
from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://gitee.com/')

driver.find_element_by_css_selector('.item.git-nav-user__login-item').click()
time.sleep(2)
driver.find_element_by_css_selector('.login-password__account-input').send_keys('15171286980')
time.sleep(2)
driver.find_element_by_css_selector('#user_password').send_keys('hzw1234567')
time.sleep(2)
driver.find_element_by_css_selector('.ui.fluid.orange.submit.button.large:nth-child(1)').click()

'''
'''
# 案例、selenium---采集京东数据
from selenium import webdriver
import csv

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.jd.com/')
driver.maximize_window()
driver.implicitly_wait(10)  # 隐式等待


def get_product(key_word):
    """商品搜索功能"""
    driver.find_element_by_css_selector('#key').send_keys(key_word)
    driver.find_element_by_css_selector('.button').click()


def drop_down():
    """模拟页面下拉操作"""
    for h in range(1, 11, 2):  # h可以拿到1、3、5、7、9
        j = h / 11  # 5次循环，j取值1/11、3/11、5/11、7/11、9/11
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight*%f' % j  # 获取整体高度的1/11、3/11、5/11、7/11、9/11
        driver.execute_script(js)
        time.sleep(1)


def parsel_data():
    """解析数据，并保存"""
    lis = driver.find_elements_by_css_selector('.gl-item')  # li标签
    # print(lis)

    for li in lis:
        name = li.find_element_by_css_selector('.gl-item div.p-name a em').text  # 商品名字
        name = name.replace('京品电脑', '').replace('京东超市', '').replace('\n', '')

        price = li.find_element_by_css_selector('.gl-item div .p-price i').text  # 价格

        commit = li.find_element_by_css_selector('.gl-item div.p-commit').text  # 评论数量

        shop_name = li.find_element_by_css_selector('.gl-item .curr-shop.hd-shopname').text  # 店铺名字
        print(name, price, commit, shop_name, sep='|')
        with open('jd_data.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([name, price, commit, shop_name])


def get_next():
    """下一页点击"""
    driver.find_element_by_css_selector('.pn-next').click()

    # 调用商品搜索的函数


get_product('笔记本')

for page in range(100):
    # 调用页面下拉的操作
    drop_down()
    # 调用数据解析
    parsel_data()
    # 调用点击下一页函数
    get_next()

input()
driver.quit()
'''

from selenium import webdriver
import csv
import warnings
from selenium.webdriver import ActionChains

warnings.filterwarnings("ignore")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://music.163.com/#/discover/toplist?id=3778678')
# driver.maximize_window()
# driver.implicitly_wait(10)  # 隐式等待

iframe = driver.find_element_by_css_selector('#g_iframe')  # 进入有评论的嵌套框架
driver.switch_to.frame(iframe)


def jx_page():
    comments = driver.find_elements_by_css_selector('.cmmts.j-flag>.itm')
    # print(type(comments))
    for comment in comments:
        name = comment.find_element_by_css_selector('div.cntwrap a').text
        content = comment.find_element_by_css_selector('div.cntwrap div.cnt.f-brk ').text
        date = comment.find_element_by_css_selector('div .rp>.time.s-fc4').text
        # zan = comment.find_element_by_css_selector('.cmmts.j-flag>.itm .rp a:nth-child(2)').text
        print(name, content, date, sep='|')

        with open('网易云.csv', mode='a', encoding='utf-8', newline='') as f:
            write = csv.writer(f)
            write.writerow((name, content, date))


def get_next():
    """下一页点击"""
    driver.find_element_by_css_selector('.zbtn.znxt').click()


for page in range(1, 21):
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    driver.execute_script(js)
    print(f'正在爬取网易云第{page}页评论信息')
    jx_page()
    get_next()
    time.sleep(1)

# driver.close()

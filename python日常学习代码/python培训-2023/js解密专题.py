# -*- codeing = Utf-8 -*-
# @Time :2023/5/18 20:51
# @Author :ZunKki
# @File :js解密专题.py
# '# @Software':  'PyCharm'
'''
import requests
import execjs
# pip install pyexecjs -- 安装模块名
url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1684417951041_1684417964134_E087qNlr8ytxWVeeJoaOn+iUn7f6G8JLbXN7OMWfEmqLPh+4XhjapV80aRaL3pzA30vbweJFMmfm76WtM2dHHe9tmFwpR+pKM7jPdmp29fVQ43HODegupXEGm5G2d/B/bKkRUWoX/+pUIDYvHNzO45CrzmuCV1ec27aM0NvajZxnqGSy8w8U6Cuf2YwrgXO0hgGmKnykVqQzP5lvPaepavTgF5STJ/u+uwlFBwBgqwcA2IhUQCu5H9bMD89YxVSyyCLQOzE/hyR/qa4qbMcJIn/Gcw+hLyNOPtszTg9BllUgJIR6NpF7nemiB3Xq5s1/Nw8/cZa2JkBk6fWbHjNbTkrzVIQZ9D6qP9E6/2+ZolvjTvyR8c2Xd0gbzvWeozJOQ4SiJoSO2ERP3Aj9GsQGL82RduvnWnVAXHfIYTvrXiSEflXZGL4jfmx1MoyoKaQk6gnJw6mm51MFb3lGZHGLjNLYukgR/hvhtPDjZHHFr7g=',
    'Connection': 'keep-alive',
    'Content-Length': '166',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=9D88EC91449A4333588691749F4D00CE; PSTM=1684417935; BAIDUID=9D88EC91449A43338EA921E8FFDFAD7A:FG=1; H_PS_PSSID=; delPer=0; PSINO=6; BAIDUID_BFESS=9D88EC91449A43338EA921E8FFDFAD7A:FG=1; BA_HECTOR=ag808la4210g2g018lah256i1i6cbcf1m; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=cAUSZEAqi2FqOfozkyYaSYKbryfmuQo7oBcCWQXo384:C; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1684417948; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1684417948; ab_sr=1.0.1_NTJhMmMxZTg2MWNhM2QxZWYwNzQ1NzQ3ZTY2ZjhkYzkyM2YwNTUyNzExNzc5NGFkNzhlZDA0NjJiOTYzNGQ0YjdkOTI5NWYyZTY3NTAzNWViYjMzZGI0MmY5YzM1MDEzMGUyODFlNWQ0MWU1Y2UyNzA4MDI2OGU4YTkzNDBkN2RkMjMyNzBiOGNkNjVkOTI4MDFmMWVkODJjNTg5N2UwNQ==',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"r'
}
data = {
    'from': 'zh',
    'to': 'en',
    'query': '你好',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '232427.485594',
    'token': 'ae64f01d9ec87033e7cf03484eb724c7',
    'domain': 'common',
    'ts': '1684417964119'
}

response = requests.post(url=url, data=data, headers=headers)
json_data = response.json()
# print(json_data)

'''
'''
js代码逆向思路：
    找加密的数据：1.查询参数、2.请求参数、3.请求头字段信息 4.数据包返回的数据加密了
    
    通过数据包逆向分析，找到js加密的主要函数逻辑，执行函数
    
    根据报错缺哪补哪
'''

'''
# 1.模拟请求，发现问题
import requests
import execjs
import json
url = 'https://vipapi.qimingpian.cn/DataList/productListVip'

headers = {
    'Host': 'vipapi.qimingpian.cn',
    'Origin': 'https://www.qimingpian.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': '1',
    'num': '20',
    'unionid': ''
}

response = requests.post(url=url, data=data, headers=headers)
# print(response.json()['encrypt_data'])
#
with open('企名片js解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

# 调用 execjs.compile() 编译并加载 js 文件内容
compile_obj = execjs.compile(js_code)

# 调用js代码---execjs.call
result = compile_obj.call('s', response.json()['encrypt_data'])


print(result)

print(json.loads(result))

'''

'''
编码与解码
中文与英文都是一种格式
'''

'''
hello = '你好，世界！'

# 编码 encode
encode_str = hello.encode('utf-8')
print(encode_str)
# 二进制(b) 八进制(o) 十六进制(x)

# 解码 decode
print(encode_str.decode('utf-8'))


# 二进制与十六进制

import binascii

print(encode_str)
# 十六进制转化威二进制
a = binascii.b2a_hex(encode_str)
print(a)
print(a.decode('utf-8'))  # 二进制内容解码为字符串
# 二进制转化为十六进制
b = binascii.a2b_hex(a)
print(b)
'''

'''
urlencode
'''

"""
url编码，url默认的情况下不支持中文
表单提交
"""

'''
import urllib.parse

url = 'https://www.maoyan.com/query?kw=%E8%9C%98%E8%9B%9B%E4%BE%A0'
# unquote url 内容的解码
print(urllib.parse.unquote('%E8%9C%98%E8%9B%9B%E4%BE%A0'))

# urlencode
# 以后一旦遇到 % +两个大写英文单词，第一时间想到url编码
print(urllib.parse.quote('蜘蛛侠'))
'''

'''
Base64编码
'''

'''
import base64

hello = '你好,世界!'

# 计算机的编码解码，或者一些加密算法，都是基于二进制的
# 可以被加密，可以继续拆分
# base64编码
print(base64.b64encode(hello.encode('utf-8')))
# b'5L2g5aW9LOS4lueVjCE=' 一旦看到类似的字符串第一反应是不是base64的编码
encode_b64 = base64.b64encode(hello.encode('utf-8'))
decode_b64 = base64.b64decode(encode_b64)
print(decode_b64)
print(decode_b64.decode('utf-8'))
'''

import requests
import parsel

url = 'https://www.plap.cn/index/selectAllByTabs.html?articleTypeId=1&secondArticleTypeId=23'
headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 113.0.0.0Safari / 537.36'
}

response = requests.get(url=url, headers=headers)
selector = parsel.Selector(response.text)
# print(response.text)
lis = selector.css('.categories.li_square>li')
# print(lis)
for li in lis:
    title = li.css('li>a::attr(title)').get()
    print(title)
    pub_time = li.css('li>.col-md-3.col-sm-3.col-xs-6.tc.p0::text').get()
    print(pub_time)
    img_url = li.css('li>a::attr(href)').get().replace('selectArticleNewsById.do', 'downloadDetailsImage.html')
    print(img_url)

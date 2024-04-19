import re

import requests

session = requests.session()
cookies = {
    '_ga': 'GA1.2.1921803061.1686660464',
    '_gid': 'GA1.2.1773451880.1686660464',
    '_ym_uid': '1686660466680383982',
    '_ym_d': '1686660466',
    '.AspNetCore.Antiforgery.9TtSrW0hzOs': 'CfDJ8EHguMx5FNJFiMvrdn4FRxUgonESIh2ENATiyEKvxGyzRn30as4gHmlt6NqWXqaRmWtdE5hqNQD-2fxh10vH3J02eJ3wpLZ0LNDxOiTHtJnBYi58-EovU8oZZDVgCSAKoVn6minlPYpQbmAvcFOVijc',
    '_ym_isad': '2',
    '_dc_gtm_UA-164244071-1': '1',
    '_gat_UA-97031288-1': '1',
    '_ym_hostIndex': '0-4%2C1-4',
}

headers = {
    'authority': 'my.tacolo.co',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.1921803061.1686660464; _gid=GA1.2.1773451880.1686660464; _ym_uid=1686660466680383982; _ym_d=1686660466; .AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8EHguMx5FNJFiMvrdn4FRxUgonESIh2ENATiyEKvxGyzRn30as4gHmlt6NqWXqaRmWtdE5hqNQD-2fxh10vH3J02eJ3wpLZ0LNDxOiTHtJnBYi58-EovU8oZZDVgCSAKoVn6minlPYpQbmAvcFOVijc; _ym_isad=2; _dc_gtm_UA-164244071-1=1; _gat_UA-97031288-1=1; _ym_hostIndex=0-4%2C1-4',
    'referer': 'https://my.tacolo.co/profile',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

html_data = session.get('https://my.tacolo.co/signin?ReturnUrl=/profile', cookies=cookies, headers=headers).text
token = re.findall('<meta name="anti-csrf-token" content="(.*?)" />', html_data)[0]
"""
'email': '838309518@qq.com',
'fingerprint': '25949c918fab67d6466b7cbdf8c7dc36',
'password': '111111',
"""
headers['x-anti-csrf-token'] = token
headers['email'] = '838309518@qq.com'
headers['password'] = 'Aabb11223344!'
text=session.get('https://my.tacolo.co/public/login', headers=headers).text
print(text)






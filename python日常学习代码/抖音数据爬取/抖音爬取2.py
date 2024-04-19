# -*- codeing = Utf-8 -*-
# @Time :2023/5/27 23:13
# @Author :ZunKki
# @File :抖音爬取2.py
# @Software: PyCharm,

import requests


url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAAAKy2_R6k-oFWT5E-97gbGZQ1laaweQMWImJDkDaef0&max_cursor=1627115511000&locate_item_id=7006257969608346921&locate_query=false&show_live_replay_strategy=1&count=10&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=113.0.0.0&browser_online=true&engine_name=Blink&engine_version=113.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7237877034377299513&msToken=_OzFgXfk90dgjnowDAO4P5A86kvK6RK68Yk53QxwuWrZJlkwIVQib_yYOoIV9mPrRVsdfUzqc_mBUcvoHXRxRY26xYncNStS3xBjs9onzcRvShkBuz8XgxwRbi361A==&X-Bogus=DFSzswVYb8TANto5tS-lkF9WX7ri'
# 请求参数
headers = {
    'Referer': 'https://www.douyin.com/user/MS4wLjABAAAAAAKy2_R6k-oFWT5E-97gbGZQ1laaweQMWImJDkDaef0?relation=0&vid=7006257969608346921',
'Cookie': 'ttwid=1%7CgdRFttoZ6Jpdgari1mivGtkyHecWc5o11ycqwrq1nj0%7C1685199578%7Cb68680ee2fb8ce3637e91d81e35e6b7d74af447f0d1e1de5a3b5f2ac5846f29f; douyin.com; strategyABtestKey=%221685199580.168%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1685804380179%2C%22type%22%3A1%7D; passport_csrf_token=72243c420c90c4551cc218e7e8d53339; passport_csrf_token_default=72243c420c90c4551cc218e7e8d53339; s_v_web_id=verify_li64bi7r_33Sku68D_Igl1_4zRB_9j8l_DdpJBhv3ZmK3; csrf_session_id=5af7d0b2629f74490fbc461d555ab9da; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEVENCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRU4reFo5RndFN1o2TGZjQXk2RXJ2MlozNlxyXG5tbnFzNzlQelJ4RCtNMkxqSzVkQ0dNOE96OHlNNWxla2IxUzM5bjFQSFFpMFhPZzdTWXhhY2V1a2d6cHk1YUFzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEUndBd1JBSWdQaFkvVWVQL0hWWG9VckpNYWg2TEhTa2tkYitjOUNtaUtmdHBRWDM5b01VQ1xyXG5JRW8rR2JZSjZnck56UXN3TnUxR0ZYS2Y1dXRYZ25VcVhPOU1iZXI2amxjSVxyXG4tLS0tLUVORCBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS1cclxuIn0=; ttcid=8489b364bd184be6bb69fff6906fe29a42; __ac_nonce=064721ae6001b0d55c94c; __ac_signature=_02B4Z6wo00f0197FN6gAAIDDXsfN6FtZKaPe5TMAAJPMbIr6ZCqFLeYj2cdxrfLgpeuMrf4tKY49OlngDzYe9SBg7tQk9wAUWcQmK9s3NKcNw4paUHhXVRdqw6OJ7Tci5d3uKOxG.ytBn6ehe7; download_guide=%221%2F20230527%2F0%22; home_can_add_dy_2_desktop=%221%22; msToken=3kXSBq4HqI5U5VSIXqWWUSsSMX-FUog9I8j2f4hkqvcLUC2bWbzBgObTiowFya4bFMldupiTWmWfJs85zU5Xi03q59F178hgs3H2cCo7xwhDiVXyKo6T; msToken=b2vC0Etk4Urwz4nt1qjL-z9eiWaNsJy88XwOM5cLKuaDiPQ_fGS8lCHS6eMrcJLA_tCbC8_1he_ykzHtDzcY6xCa-grh61gTJWwLjgZMq9Yq-BgxPA4Q; tt_scid=Ol5JDuvNbSg6xp-z6zz1xrKVDWLvVDESgLNhvKCi8QRYAnetLlkstpwjrkmyXoJKecfb; pwa2=%221%7C0%22',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


# 获取源页面json数据
response = requests.get(url=url, headers=headers)

print(response.json())
# print(response.request.url)
# print(response)
#
# 取出所有字典数据
# id_lists = response['aweme_list']
# # 遍历字典数据，取出每一个视频对应的id
# for id_list in id_lists:
#     video_id = id_list['aweme_id']
#     print(video_id)

# -*- codeing = Utf-8 -*-
# @Time :2023/5/27 14:01
# @Author :ZunKki
# @File :抖音数据爬取.py
# @Software: PyCharm


import requests
import re
import urllib.parse

# 请求链接
url = 'https://www.douyin.com/video/7006257969608346921'

headers = {
    'Cookie': 'douyin.com; __ac_nonce=06471a56300d06cd82b93; __ac_signature=_02B4Z6wo00f01v-eEEAAAIDCf5zqAKDEqQL.vhTAANuj69; ttwid=1%7CBbu6Od88jZ-Z5wx5zVqplQ5jVYiWS81VpXrG2ZNtvdg%7C1685169508%7C4403a00d0970fa6cb7c5783a76fb8b21bf6bcf373f870f138c4e47ea38a2c127; strategyABtestKey=%221685169509.25%22; passport_csrf_token=a3c110d5de634c9ada91ca986c5181e2; passport_csrf_token_default=a3c110d5de634c9ada91ca986c5181e2; s_v_web_id=verify_li5mf0cb_fx5ddFcq_U1li_4oDm_9cjS_A6m84ov4bzGd; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEakNCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRXlmRnZ6RlNvWXlmaTJQZnBYWUliS2prT1xyXG4vVDZRa1ZMam1YdDJzNWc2aHpJOUNJWmlPZmVYckRFOFdwN25qdE5mbDRNYnMyb2RkVjJJc2VUM3h6ZmMyYUFzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEU0FBd1JRSWhBSlVsTzg2SktLeFFEekwwekhTN244YWxTQWQ2ZnlqM0JCQXpKZjFnbHgwVVxyXG5BaUJpZ0kvRjQrQXlheGpEbEtvbTlheWovaTR2bFBJT0JGWmErazdNYktDS0hRPT1cclxuLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbiJ9; ttcid=fb3bce4ba6714c1c97c50b4f6dd3a33d13; tt_scid=6Co9oW4bJZg3Fcof4KKR8.GMVIgPdlv0YPqs32.eDEW58VTeqaDPe-tPE7pF4iO290af; download_guide=%222%2F20230527%22; pwa2=%222%7C0%22; home_can_add_dy_2_desktop=%221%22; msToken=YpCLwwT2OBUY7pjbgrW7HnmeMfVuwp4ieGjWNzLcgfSCO-s__gIJ4Wc8jtnhMUhgu8F5EyCKPmwUW9Wks-SX5bODqM0G9moLCoNsg_hAeAG6ybap-a7mxGTgfh8vig==; msToken=5dFVuI-BdpGegeZsq-K2qXssQTVUlFw9OaPSY1ahaufDb34xnKD9-ogEW8pQYu4TQbTUDdAzphsQil_xYYX3sTJ9kz7MbZk9_O3l4Ttq_GC3rF5fTilUOLRj5EdTRw==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

# 获取网页源代码
response = requests.get(url=url, headers=headers)
# print(response.text)

# 解析数据
# 分析可知视频播放地址和标题均在网页源代码，播放网址进行过url编码

title = re.findall('<title data-react-helmet="true">(.*?) - 抖音</title>', response.text)[0]
print(title)
video_url = re.findall('src(.*?)%22%7D', response.text)[7]
# print(video_url)

# 网页中除了目标视频还有其他推荐视频网址，遍历找出目标视频网址
# for i in video_url:
#     video_url = urllib.parse.unquote(i).replace('":"', 'https:')
#     print(video_url)

# url地址解码
video_url1 = urllib.parse.unquote(video_url).replace('":"', 'https:')
print(video_url1)

# 获取目标视频二进制数据
video_content = requests.get(url=video_url1, headers=headers).content

# 保存目标视频二进制数据
with open('video\\' + title + '.mp4', mode='wb') as f:
    f.write(video_content)
    print(title, '保存成功')

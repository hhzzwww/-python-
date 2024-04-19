# -*- codeing = Utf-8 -*-
# @Time :2023/5/29 20:14
# @Author :ZunKki
# @File :img_api.py
# @Software: PyCharm
import requests
import json
import base64
from constants import KUAI_USERNAME, KUAI_PASSWORD

'''
1	纯数字
1001	纯数字2
2	纯英文
1002	纯英文2
3	数英混合
1003	数英混合2
4	闪动GIF
7	无感学习(独家)
66	问答题
11	计算题
1005	快速计算题
5	快速计算题2
16	汉字
32	通用文字识别(证件、单据)
29	旋转类型
19	点选1个坐标
20	点选3个坐标
21	点选3 ~ 5个坐标
22	点选5 ~ 8个坐标
27	点选1 ~ 4个坐标
48	轨迹类型
18	缺口识别（需要2张图 一张目标图一张缺口图）
33	单缺口识别（返回X轴坐标 只需要1张图）
53	拼图识别
'''


def base64_api(uname, pwd, img, typeid):
    """
    识别验证码主函数
    uname：用户名
    pwd：密码
    img：图片路径
    typeid：识别类型
    """
    # 打开图片，把图片转化成字符串形式
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()

    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}

    result1 = requests.post("http://api.kuaishibie.cn/predict", data=data).json()
    if result1['success']:
        return result1["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result1["message"]
    return ""


if __name__ == "__main__":
    img_path = "yzm.png"
    # typeid 验证码识别类型
    result = base64_api(uname=KUAI_USERNAME, pwd=KUAI_PASSWORD, img=img_path, typeid=7)
    print(result)



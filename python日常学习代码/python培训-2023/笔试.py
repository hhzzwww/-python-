"""
https://www.soyoung.com/post
爬取这个页面里面，至少20篇文章，包括文章标题，内容，以及里面的图片。文章保存到excel中，图片单独存储。
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# 数据写入excel
# 创建工作簿对象和表对象
work = openpyxl.Workbook()
sheet1 = work.active
sheet1.append(['标题', '内容'])


# 页面下拉
def drop_down():
    """模拟人去滚动页面"""
    '''部分详情页需下拉获取所有内容'''
    for h in range(1, 10, 2):
        j = h / 9
        js_all = f'document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}'
        driver.execute_script(js_all)
        time.sleep(0.5)


# 获取标题和详情页内容
def get_pages():
    # 解析出总的列表页
    buttons = driver.find_elements(By.CSS_SELECTOR, '.card-diary')
    # print(len(buttons))

    j = 1
    count = 1
    for i in range(len(buttons)):
        # 列表页从第二次点击开始会是旧页面数据, 会有元素过期的问题,每一次过期都需重新刷新列表页
        if j != 1:
            buttons = driver.find_elements(By.CSS_SELECTOR, '.card-diary')

        button = buttons[i]
        # 获取标题内容和图片网址
        title = button.find_element(By.CSS_SELECTOR, '.title').text
        # print(title)
        # 获取详情页内容
        # selenium直接点击无效，用js代码来触发点击操作
        driver.execute_script("arguments[0].click();", button)
        # 打开窗口句柄
        windows = driver.window_handles
        # 切换到详情页
        driver.switch_to.window(windows[-1])
        # 部分详情页需下拉获取所有内容
        drop_down()
        # 提取内容
        content = driver.find_element(By.CSS_SELECTOR, '.post-p').text
        content1 = content.replace('\n', '').replace(' ', '')
        # print(content1)
        # 将标题和内容添加到excel文档
        sheet1.append([title, content1])

        # 部分网页的解析语法不一致以及存在视频的形式，用异常捕获爬取大多数解析语法一直的图片
        try:  # 异常捕获
            img_url = driver.find_element(By.CSS_SELECTOR, '.swiper-slide.swiper-slide-active .blur-img>img').get_attribute('src')
            # print(img_url)
            # 获取图片二进制数据
            # 请求图片数据
            img_content = requests.get(url=img_url, timeout=1).content
            # 准备文件名
            file_name = str(count) + '.jpg'
            count += 1
            with open('img\\' + file_name, mode='wb') as f:
                f.write(img_content)
                print('保存完成：', file_name)
        except Exception as e:
            print(e)
        # 关闭详情页
        driver.close()
        # 切换到原页面
        driver.switch_to.window(windows[0])
        # 刷新当前页面，元素会过期
        driver.refresh()

        time.sleep(1)

        j = 0


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.soyoung.com/post/')
    driver.implicitly_wait(5)
    driver.maximize_window()

    # 获取标题和内容
    get_pages()

    work.save('笔试.xlsx')

    input()
    driver.quit()






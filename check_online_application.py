# -*- coding:utf-8 -*-

# 自动太难写前端也面表格数据

from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import urllib.request

# 巡检服务
ceshi=["http://ybz-sample-c-prd.online.app.yyuap.com/ping"]
for check_status in ceshi:
    res = urllib.request.urlopen(check_status)
    print(res.status)
    if res.status != 200 :
        print("%s 服务不正常" % check_status)
    else:
        print("服务都正常")


# 读取网页内容
html_doc = "http://172.20.52.54:11311/oom/yonyou/daily-checklist/?uri=yyc"
req = urllib.request.Request(html_doc)
webpage = urllib.request.urlopen(req)
html = webpage.read()
base_url = "http://172.20.52.54:11311"

#文档对象
soup = BeautifulSoup(html, 'html.parser')
# 查找 a 标签
for k in soup.find_all('a'):
    # print(k['href'])
    print(base_url + k['href'])

# 开启浏览器
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    dirvers = webdriver.Chrome(options=option)
    return dirvers

# 授权操作
def operationAuth(dirvers):
    url = base_url + k['href']
    dirvers.get(url)

    elem_domain = driver.find_element_by_id("domain")
    elem_domain.send_keys("平台")
    elem_checker = driver.find_element_by_id("checker")
    elem_checker.send_keys("方亚利")
    elem_info = driver.find_element_by_id("info")
    elem_info.send_keys("正常")

    # 提交表单
    # driver.find_element_by_xpath("//*[@class='btn btn-lg btn-info btn-block']").click()

    print('浏览器打开成功！')

if __name__ == '__main__':

    # 加启动配置
    driver = openChrome()
    operationAuth(driver)
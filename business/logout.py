# coding = utf-8
# @Time : 2020/11/29 16:31
# @Author : 崔孟泽
# @File : logout.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from time import sleep
def logout(self):
    web = self.web                # web是WebDriver对象，即WebDriverObj
    # 点击退出
    quit=web.find_element(By.LINK_TEXT,'安全退出')
    sleep(3)                      # 强制等待，此处必须强制等待，否则被点击元素被div覆盖时点击不到Element <a> is not clickable at point another element <div id="ajax-loader"> obscures it
    quit.click()
    # 点击确认
    sleep(1)
    ok=web.find_element(By.XPATH,"//a[@class='layui-layer-btn0']")
    ok.click()
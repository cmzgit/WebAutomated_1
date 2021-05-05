# coding = utf-8
# @Time : 2020/11/29 17:21
# @Author : 崔孟泽
# @File : switchPlatform.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from time import sleep
def switchPlatform(self):
    web = self.web
    # 点击平台切换
    switch = web.find_element(By.LINK_TEXT,'平台切换')
    sleep(4)                # 此处必须强制等待，否则 Element <a> is not click-able at point
    switch.click()
    sleep(3)                # 此处也须强制等待，否则 Element could not be scrolled into view
    # 切换进frame页面-平台选择
    web.switch_to.frame('get')
    # 点出下拉菜单
    select = web.find_element(By.XPATH,"//div[@class='ui-select-text']")
    select.click()
    sleep(2)
    # 点击所选机构
    myPlat = web.find_element(By.XPATH,"//div[@title='自动化测试机构']")
    myPlat.click()
    # 切换出frame页面-平台选择（切换回到默认页面）
    web.switch_to.default_content()
    # 点击确认
    ok=web.find_element(By.XPATH,"//a[@class='layui-layer-btn0']")
    ok.click()
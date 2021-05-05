# coding = utf-8
# @Time : 2020/11/28 22:05
# @Author : 崔孟泽
# @File : login.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
def login(self,username,password):
    web = self.web                 # web是WebDriver对象，即WebDriverObj
    # 定位元素
    usr = web.find_element(By.ID, 'username')
    pwd = web.find_element(By.ID, 'password')
    btn = web.find_element(By.ID, 'btnlogin')
    # 元素操作
    usr.send_keys(username)
    pwd.send_keys(password)
    btn.click()
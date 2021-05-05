# coding = utf-8
# @Time : 2020/11/29 16:15
# @Author : 崔孟泽
# @File : test_logout.py
# @Software: PyCharm
from config.USER_INFO import USERNAME,PASSWORD,URL
from business.login import *
from business.logout import *
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest,time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:           #整个测试前执行
        pass
    @classmethod
    def tearDownClass(self) -> None:        #整个测试后执行
        pass
    def setUp(self):                        # 每个测试方法前执行
        print('开始测试用例..')
        self.web=WebDriver()
        web=self.web
        web.implicitly_wait(5)             # 创建web后先设置页面加载时长
        web.get(URL)
    def tearDown(self):                     # 每个测试方法后执行
        time.sleep(5)
        self.web.quit()
        print('结束测试用例..')
    # 测试用例1-登录
    def test_login(self):
        web = self.web
        web.implicitly_wait(5)
        # 用例操作步骤
        login(self, USERNAME, PASSWORD)
        # 断言登录后的界面（比较预期结果与实际结果）
        expect = '安全退出'
        actual = web.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/ul/li[4]/a').text
        try:
            self.assertEqual(expect,actual)
        except:
            print('登陆失败，该登录测试用例不通过X')
        else:
            print('登录成功，该登录测试用例通过√')
if __name__ == '__main__':
    unittest.main()
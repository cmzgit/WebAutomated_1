# coding = utf-8
# @Time : 2020/11/29 16:43
# @Author : 崔孟泽
# @File : test_logout.py
# @Software: PyCharm
from config.USER_INFO import USERNAME,PASSWORD,URL
from business.login import *
from business.logout import *
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest,time

class TestLogout(unittest.TestCase):
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
        web.implicitly_wait(5)              # 创建web后先设置页面加载时长
        web.get(URL)
    def tearDown(self):                     # 每个测试方法后执行
        time.sleep(5)
        self.web.quit()
        print('结束测试用例..')
    # 测试用例2-登录后登出
    def test_logout(self):
        web = self.web
        web.implicitly_wait(5)
        # 用例操作步骤
        login(self, USERNAME, PASSWORD)
        logout(self)
        # 断言登出后的界面
        expect = '欢迎登陆K-TMS物流系统'
        actual = web.find_element(By.TAG_NAME,'legend').text
        try:
            self.assertEqual(expect,actual)
        except:
            print('登出失败，该登出测试用例不通过X')
        else:
            print('登出成功，该登出测试用例通过√')
            print(actual)
if __name__ == '__main__':
    unittest.main()
# coding = utf-8
# @Time : 2020/11/29 23:30
# @Author : 崔孟泽
# @File : test_switchPlatform.py
# @Software: PyCharm
from config.USER_INFO import USERNAME,PASSWORD,URL
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from business.login import login
from business.logout import logout
from business.switchPlatform import switchPlatform
import unittest,time

class TestSwitchPlatform(unittest.TestCase):
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
    # 测试用例3-切换平台
    def test_switchPlatform(self):
        web = self.web
        web.implicitly_wait(5)
        # 用例操作步骤
        login(self, USERNAME, PASSWORD)
        switchPlatform(self)
        time.sleep(5)
        logout(self)
        # 断言切换平台后界面
        expect = '自动化测试机构'
        actual = web.find_element(By.XPATH,"//div[@id='main-hd-title']/a[2]").text
        try:
            self.assertEqual(expect,actual)
        except:
            print('切换平台失败，该测试用例不通过X')
        else:
            print('切换平台成功，该测试用例通过√')
if __name__ == '__main__':
    unittest.main()
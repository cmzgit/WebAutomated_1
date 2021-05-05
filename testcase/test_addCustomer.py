# coding = utf-8
# @Time : 2020/11/29 20:03
# @Author : 崔孟泽
# @File : test_addCustomer.py
# @Software: PyCharm
from config.USER_INFO import USERNAME,PASSWORD,URL
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from business.login import login
from business.logout import logout
from business.switchPlatform import switchPlatform
from business.addCustomer import addCustomer
import unittest,time

class TestAddCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:           #整个测试前执行
        pass
    @classmethod
    def tearDownClass(self) -> None:        #整个测试后执行
        pass
    def setUp(self):                        # 每个测试方法前执行
        print('开始测试用例..')
        self.web=WebDriver()                # 启动浏览器
        web=self.web
        web.implicitly_wait(5)              # 创建web后先设置页面加载时长
        web.get(URL)                        # 访问页面
    def tearDown(self):                     # 每个测试方法后执行
        time.sleep(2)
        logout(self)                        # 登出账户
        time.sleep(3)
        self.web.quit()                     # 退出浏览器
        print('结束测试用例..')
    # 测试用例4-新增新客户
    def test_addCustomer(self):
        web = self.web
        web.implicitly_wait(5)
        # 用例操作步骤
        login(self, USERNAME, PASSWORD)
        switchPlatform(self)
        time.sleep(2)
        addCustomer(self)
        time.sleep(2)
        # 切换进frame页面-客户档案
        web.switch_to.frame('iframe402881d260d3d2e90160d4468ae00003')
        # 断言新增后的客户列表界面的客户名称
        expect = '测试客户名称-崔孟泽'
        actual = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[5]/table/tbody/tr[2]/td[7]').text
        try:
            self.assertEqual(expect,actual)
        except:
            print('新增新客户失败，该测试用例不通过X')
        else:
            print('新增新客户成功，该测试用例通过√')
        # 切换回父级初始页面便于'登出'
        web.switch_to.default_content()
if __name__ == '__main__':
    unittest.main()
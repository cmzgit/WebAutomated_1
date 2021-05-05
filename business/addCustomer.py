# coding = utf-8
# @Time : 2020/11/29 17:22
# @Author : 崔孟泽
# @File : addCustomer.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
def addCustomer(self):
    web = self.web
    web.implicitly_wait(5)
    # ‘基础数据’-‘客户档案’
    baseData = web.find_element(By.XPATH, "//ul[@id='nav']/li[1]")
    userDoc = web.find_element(By.XPATH, "//a[@id='402881d260d3d2e90160d4468ae00003']")
    # 鼠标移动到'基础数据'
    action = ActionChains(web)
    action.move_to_element(baseData).perform()
    sleep(3)
    # 点击'客户档案'
    userDoc.click()
    sleep(3)
    # 切换进frame页面-客户档案
    web.switch_to.frame(web.find_element(By.ID,'iframe402881d260d3d2e90160d4468ae00003'))
    # 点击新增
    addBtn=web.find_element(By.LINK_TEXT,'新增')
    addBtn.click()
    sleep(4)
    # 先切换回父级初始页面，否则 NoSuchFrameException: Unable to locate element CustomerFrom2
    web.switch_to.default_content()
    # 再切换进frame页面-新增页面
    web.switch_to.frame('CustomerFrom2')
    ################# 下面是输入新增的内容 #########################
    # 点击”所属注册公司“
    company = web.find_element(By.XPATH,"//div[@id='jcRegistration']/div[@class='ui-select-text']")
    company.click()
    sleep(3)
    # 点击所选公司
    myCompany = web.find_element(By.XPATH,"//div[@title='自动化注册公司']")
    myCompany.click()
    # 点击”结算方式“
    settle = web.find_element(By.XPATH,"//div[@id='settlementType']/div[@class='ui-select-text']")
    settle.click()
    sleep(3)
    # 点击所选方式-月结
    mySettle = web.find_element(By.XPATH,"//li[@data-value='0']")
    mySettle.click()
    # 点击”城市“
    city = web.find_element(By.XPATH,"//div[@id='zone']/div[@class='ui-select-text']")
    city.click()
    sleep(3)
    # 点击所选城市
    myCity = web.find_element(By.XPATH,"//div[@title='苏州市']")
    myCity.click()
    sleep(1)
    # 点击“合同开始时间”
    start = web.find_element(By.XPATH,"//input[@id='startTime']")
    start.click()
    sleep(1)
    # 先从新增页面切换回父级初始页面（此处前须等待，否则 NoSuchElementException 或 NoSuchFrameException）
    web.switch_to.default_content()
    # 再从父级初始页面切换进frame页面-日期页面(该frame无id/name需要用特殊元素定位)
    dateFrame=web.find_element(By.CSS_SELECTOR,'body>div:nth-child(7)>iframe:nth-child(1)')
    web.switch_to.frame(dateFrame)
    # 日期页面里点击'所选日期'
    preBtn=web.find_element(By.XPATH,"//div[@class='navImg NavImgll']/a")
    preBtn.click()
    sleep(1)
    okBtn = web.find_element(By.XPATH,"//input[@id='dpOkInput']")
    okBtn.click()
    sleep(1)
    # 先从日期页面切换回父级初始页面
    web.switch_to.default_content()
    # 再从父级初始页面切换到frame页面-新增CustomerFrom2
    web.switch_to.frame('CustomerFrom2')
    # 点击“合同结束时间”
    end = web.find_element(By.XPATH,"//input[@id='endTime']")
    end.click()
    sleep(1)
    # 先从新增页面切换回父级初始页面
    web.switch_to.default_content()
    # 再从父级初始页面切换进frame页面-日期页面
    web.switch_to.frame(dateFrame)
    # 日期页面里点击'所选日期'
    nxtBtn= web.find_element(By.XPATH, "//div[@class='navImg NavImgrr']/a")
    nxtBtn.click()
    sleep(1)
    okBtn.click()
    # 先从日期页面切换回父级初始页面
    web.switch_to.default_content()
    # 再从父级初始页面切换回frame页面-新增页面
    web.switch_to.frame('CustomerFrom2')
    # 输入“发货客户地址”，并回车，再点击该输入框
    addr = web.find_element(By.ID,'address')
    addr.send_keys('杭州站')
    sleep(1)
    addr.send_keys(Keys.ENTER)
    addr.click()
    # 定位其他纯文本框
    name = web.find_element(By.XPATH, "//input[@id='name']")            # 客户名称
    code = web.find_element(By.XPATH, "//input[@id='code']")            # 合同编号
    person = web.find_element(By.XPATH, "//input[@id='contactperson']") # 发货联系人
    detail = web.find_element(By.XPATH, "//input[@id='detailedAddress']")#详细地址
    iphone = web.find_element(By.XPATH, "//input[@id='iphone']")        # 客户电话
    # 纯文本框输入内容
    name.send_keys('测试客户名称-崔孟泽')
    code.send_keys('hta0001')
    person.send_keys('崔孟泽')
    detail.send_keys('滨江区崔孟泽家')
    iphone.send_keys('12345678900')
    sleep(5)
    # 切换出frame页面-新增页面
    web.switch_to.default_content()
    # 点击确认
    ok=web.find_element(By.XPATH,"//a[@class='layui-layer-btn0']")
    ok.click()
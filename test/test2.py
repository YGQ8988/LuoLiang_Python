from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  #操作过程中休眠
driver = webdriver.Chrome() #使用谷歌浏览器进行调试
driver.maximize_window()  #浏览器最大化
time.sleep(1)
class Guohuai():
    def __init__(self,url='http://139.129.218.57/mydandelion/login.html'):   #完成登录，需手动输入账号密码，若不想手动，将账号密码明文写入相应参数中
        self.url = url
        driver.get(self.url)
        # 完成登录操作
        driver.find_element_by_id("loginAccount").clear()
        user = input('请输入你的账号：')
        driver.find_element_by_id("loginAccount").send_keys(user)  # 用户名
        time.sleep(1)
        driver.find_element_by_id("loginPassword").clear()
        passwd = input('请输入你的账号密码：')
        driver.find_element_by_id("loginPassword").send_keys(passwd)  # 用户密码
        time.sleep(1)
        driver.find_element_by_id("doLogin").click()  # 点击登录按钮
        time.sleep(10)
        print(driver.get_cookies())
    def make(self):  #------------------新增接入者---------------------------#完成点击接入者管理-接入者列表-新增接入者
        driver.find_element_by_xpath('//*[@id="sidebarMenu"]/li[4]/a/span').click()
        time.sleep(1)
        driver.find_element_by_link_text('接入者列表').click()
        time.sleep(1)
        driver.find_element_by_id('accessPersonAdd').click()   #新增接入者
        time.sleep(1)
        #录入数据
        Access =  input('请输入接入者全称：')
        driver.find_element_by_name('fullName').send_keys(Access) #接入者全称
        time.sleep(1)
        Requester = input('请输入接入者简称：')
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[2]/div/div/input').send_keys(Requester)  #接入者简称
        time.sleep(1)
        qualification = input('请输需要赋予的资质（资金端，资产端，增信机构，助贷机构，放款人，协同放款人）：')
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[3]/div/div/span/span[1]/span/ul/li/input').send_keys(qualification)  #接入者资质
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[3]/div/div/span/span[1]/span/ul/li/input').send_keys(Keys.ENTER)
        time.sleep(1)
        qualification2 = input('若多个资质，请再次输入，没有则回车：')
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[3]/div/div/span/span[1]/span/ul/li/input').send_keys(qualification2)  # 接入者资质
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[3]/div/div/span/span[1]/span/ul/li/input').send_keys(Keys.ENTER)
        #time.sleep(1)
        way = input('请输入该接入者接入方式（人工，系统）：')
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[4]/div/div/span/span[1]/span/ul/li/input').send_keys(way)   #接入方式
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[4]/div/div/span/span[1]/span/ul/li/input').send_keys(Keys.ENTER)
        time.sleep(1)
        way2 = input('若多个接入方式，请再次输入，没有则回车：')
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[4]/div/div/span/span[1]/span/ul/li/input').send_keys(way2)  # 接入方式
        driver.find_element_by_xpath('//*[@id="addAccessPersonForm"]/div[4]/div/div/span/span[1]/span/ul/li/input').send_keys(Keys.ENTER)
        time.sleep(1)
        mail = input('请输入接入者邮箱地址：')
        driver.find_element_by_name('email').send_keys(mail)   #接入者邮箱
        time.sleep(1)
        describe = input('请输入接入者描述：')
        driver.find_element_by_name('accessDescription').send_keys(describe)   #接入者描述
        #driver.find_element_by_id('addAccessPersonSubmit').click()  #提交审核
        time.sleep(1)
    def new(self):
        driver.find_element_by_link_text('核心业务管理').click()
        time.sleep(1)
        driver.find_element_by_link_text('新增资产').click()
        try:
            driver.find_element_by_id('select2-assetName-container').is_displayed()
            print('元素存在！')
        except BaseException as f:
            print(f)
            print('元素不存在！')


a = Guohuai()
a.new()




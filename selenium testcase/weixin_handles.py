from appium import webdriver
import time
import os

# 作者：染洛凉 QQ交流群：368639036

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '4.2.2',
                'deviceName': '9050ad0c',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                # 'automationName': 'Uiautomator2',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
                "chromedriverExecutable":'/usr/bin/chromedriver'   #绝对路径浏览器驱动需与手机谷歌内含版本驱动一致
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

# 作者：染洛凉 QQ交流群：368639036
time.sleep(10)
# 点微信首页搜索按钮
driver.find_element_by_accessibility_id("搜索").click()
# 输入内容搜索
time.sleep(3)
driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys("Python")
# 点开公众号
time.sleep(3)
a = 'adb shell input tap 300 230'
os.system(a)

# 点公众号菜单-精品分类
time.sleep(3)
b = 'adb shell input tap 350 800'
os.system(b)

# 切换到webview
time.sleep(2)
print(driver.contexts)
time.sleep(5)
driver.switch_to.context('NATIVE_APP')
time.sleep(5)
# 打印切换后handles内容
print(driver.page_source)
time.sleep(2)
driver.quit()
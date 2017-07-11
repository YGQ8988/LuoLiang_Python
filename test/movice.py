from selenium import webdriver
from time import sleep
baidu = webdriver.Firefox()
baidu.get('http://www.baidu.com')
sleep(2)
baidu.find_element_by_css_selector('a.lb:nth-child(7)').click()
sleep(2)
baidu.find_element_by_id('TANGRAM__PSP_8__userName').clear()
name = input('请输入你的百度账号、手机号、邮箱地址：')
baidu.find_element_by_id('TANGRAM__PSP_8__userName').send_keys(name)
sleep(2)
baidu.find_element_by_id('TANGRAM__PSP_8__password').clear()
passwd = input('请输入你的账号密码:')
baidu.find_element_by_id('TANGRAM__PSP_8__password').send_keys(passwd)
sleep(2)
baidu.find_element_by_id('TANGRAM__PSP_8__submit').submit()
sleep(2)
baidu.find_element_by_id('TANGRAM__PSP_8__verifyCode').clear()
code = input('请输入页面验证码：')
baidu.find_element_by_id('TANGRAM__PSP_8__verifyCode').send_keys(code)
baidu.find_element_by_id('TANGRAM__PSP_8__submit').submit()

cookie = baidu.get_cookies()
print(cookie)



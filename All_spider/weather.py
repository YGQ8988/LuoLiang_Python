import requests
import json
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL



def getweather(url,lat,lon,appcode):
    '''获取近三天天气情况'''
    try:
        headers = {
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Authorization':'APPCODE '+appcode
                   }
        bodys = {
            'lat' : lat,
            'lon' : lon,
            'token' : '''443847fa1ffd4e69d929807d42c2db1b'''
        }

        html = requests.post(url,data=bodys,headers=headers)
        html.encoding = html.apparent_encoding
        # print(html.text)
        html = json.loads(html.text)
        weather = html.get('data').get('forecast')
        city = str(html.get('data').get('city').get('counname')) + str(html.get('data').get('city').get('pname')) + str(html.get('data').get('city').get('name'))
        weathers = []
        for a in weather:
            ygrq = "预告日期：{}".format(a.get('predictDate'))
            btqk = "日间天气情况：{}".format(a.get('conditionDay'))
            wsqk = "晚间天气情况：{}".format(a.get('conditionNight'))
            zdwd = "当天最低温度：{}度".format(a.get('tempNight'))
            zgwd = "当天最高温度：{}度".format(a.get('tempDay'))
            btfx = "日间风向：{}，级数：{}级".format(a.get("windDirDay"),a.get('windLevelDay'))
            wsfx = "晚间风向：{}，级数：{}级".format(a.get("windDirNight"), a.get('windLevelNight'))
            weathers.append(ygrq)
            weathers.append(btqk)
            weathers.append(wsqk)
            weathers.append(zdwd)
            weathers.append(zgwd)
            weathers.append(btfx)
            weathers.append(wsfx)
        return weathers,city
    except BaseException as f:
        return "获取近三天天气情况失败，错误信息为：{}".format(f)

def sendmail(weathers,receiver):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = '3301885103@qq.com'
    # pwd为qq邮箱的授权码
    pwd = 'xxbdadibgpmgchhj'
    # 发件人的邮箱
    sender_qq_mail = '3301885103@qq.com'
    # 收件人邮箱
    receiver = receiver
    hh = '，'
    try:
        # 邮件的正文内容
        today = ''
        tomorrow = ''
        dftomorrow = ''
        for a in weathers[0][0:7]:
        	b = a + hh
        	today +=b
        for a in weathers[0][7:14]:
        	b = a + hh
        	tomorrow +=b
        for a in weathers[0][14:21]:
        	b = a + hh
        	dftomorrow +=b
        mail_content = today + '\n\n' + tomorrow + '\n\n' + dftomorrow
        # 邮件标题
        mail_title = weathers[1] + "近三日天气情况"
        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
    except:
        mail_title = '内容出错了'
        mail_content = weathers
        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()

if __name__ == "__main__":
    url = 'http://apifreelat.market.alicloudapi.com/whapi/json/aliweather/briefforecast3days'
    appcode = '6fd80bf9a8784ed486dfd35b0b82ee36'
    # 可在http://api.map.baidu.com/lbsapi/getpoint/index.html获取某地经纬度
    lat = '''31.251547'''       #纬度
    lon = '''121.233772'''      #经度
    weather = getweather(url,lat,lon,appcode)
    receiver = '898829225@qq.com'       #邮件人邮箱地址
    sendmail(weather,receiver)
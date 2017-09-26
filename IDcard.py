import requests
from time import sleep
import re
import xlwt

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

def gethtml(url):
    '''通过POST提交重新换一批请求'''
    data = {'id':'reload...'}
    try:
        html = requests.post(url,data=data)
        html.encoding = 'utf-8'
        return html.text

    except BaseException as f:
        print('出错了，错误信息为',f)

def getid(html):
    '''正则匹配页面源码内需要的数据'''
    try:
        pat = re.compile('<td>(.{2,3}) (\d{18})</td>', re.S)
        infos = re.findall(pat, html)
        return infos

    except BaseException as f:
        print('出错了，错误信息为',f)


if __name__ == '__main__':

    url = 'http://shenfenzheng.293.net'
    print('======================================================================================')
    print('=====说明：本程序获取的数据将保存在D盘根目录下,如需获取一组新数据请关闭此程序,再运行即可=====')
    print('======================================================================================')
    print('----------正在获取数据，请耐心等待----------')
    html = gethtml(url)
    infolist = getid(html)
    print('----------正在保存数据，请耐心等待----------')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('idcard')
    ws.write(0, 0, '姓名')
    ws.write(0, 1, '身份证号码')
    num = 1
    for a in infolist:
        ws.write(num,0,a[0])
        ws.write(num,1,a[1])
        num+=1
    wb.save('D://IDcard.xls')
    print('----------保存成功，Excel文件请见D盘根目录下----------')
    print('----------本程序将在5秒后自动关闭----------')
    sleep(5)


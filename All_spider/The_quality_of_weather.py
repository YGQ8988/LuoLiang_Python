import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import re
import csv

def getrep(ym):
    '''通过selenium获取HTML并报错'''
    try:
        w = webdriver.Chrome()
        url = 'https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&month={}'.format(ym)
        w.get(url)
        sleep(3)
        r = w.page_source
        filename = 'container{}.html'.format(ym)
        with open(filename,'w',encoding='utf-8')as f:
            f.write(r)
        w.quit()
        return filename
    except BaseException as f:
        print('保存HTML文件失败了，错误信息为：',f)

def getinfo(filename):
    '''通过正则匹配空气质量信息'''
    try:
        soup = BeautifulSoup(open(filename),'lxml')
        h = soup.find('tbody')
        p = re.compile('''<td align="center">(.*?)</td> <td align="center">(.*?)</td> <td align="center"><span style="display:block;width:60px;text-align:center;background-color:.*?;color:black;">(.*?)</span></td> <td align="center">(.*?)</td> <td align="center">(.*?)</td> <td align="center" class="hidden-xs">(.*?)</td> <td align="center" class="hidden-xs">(.*?)</td> <td align="center" class="hidden-xs">(.*?)</td> <td align="center" class="hidden-xs">(.*?)</td> ''',re.S)
        data = re.findall(p,str(h))
        return data
    except BaseException as f:
        print('匹配空气质量详情失败了，错误信息为：',f)

def conversion(data):
    '''将匹配得到的数据内元祖转换为列表'''
    cdata = []
    for a in data:
        a = list(a)
        cdata.append(a)
    return cdata

def savefile(cdata,writer):
    '''写入数据'''
    writer.writerows(cdata)

def main():
    try:
        with open("container.csv","a",newline='',encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            #先写入columns_name
            writer.writerow(["日期","AQI","质量等级",'PM2.5','PM10','SO2','CO','NO2','O3_8h'])
            #写入多行用writerows
            for a in range(1,5):
                ym = '2018-0{}'.format(a)
                print('正在获取{}北京天气质量数据'.format(ym))
                filname = getrep(ym)
                data = getinfo(filname)
                cdata = conversion(data)
                print('_____正在保存{}月份天气质量数据'.format(ym))
                savefile(cdata,writer)
                print('__________成功保存{}月份天气质量数据'.format(ym))
        print('^-^___成功保存所有月份天气质量数据')
    except BaseException as f:
        print('主程序运行出错了，错误信息为：',f)

if __name__ == "__main__":
    main()
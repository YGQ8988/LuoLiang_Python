import requests
from bs4 import BeautifulSoup
import re
import bs4
import os
import threading


headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
           }


def getHtmltext(url):
    '''获取东方财富，百度股市通股票详情页面源码'''
    try:
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print('-----获取股票代码链接打开失败-----')

    return r.text


def getstocklist(html):
    '''获取东方财富网沪深所有股票代码'''
    slist = []
    try:
        pat = r'http://quote.eastmoney.com/s[hz]\d{6}\.html'
        s_list = re.findall(pat,html)
        for stock in s_list:
            stock = stock.split('/')[-1]
            slist.append(stock)
    except:
        print('-----股票代码匹配出错了-----')

    return slist


def getbainfo(urls):
    '''获取股票详细信息'''
    count = 0
    for url in urls:
        url = 'https://gupiao.baidu.com/stock/'+url
        try:
            count+=1
            stock = {}
            html = getHtmltext(url)
            soup = BeautifulSoup(html,'lxml')
            stockinfo = soup.find('div',class_='stock-bets')
            title = stockinfo.text.split()[0]
            stock.update({'股票链接':url})
            stock.update({'股票名称':title})
            keylist = stockinfo.find_all('dt')
            vallist = stockinfo.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = vallist[i].text
                stock[key] = val
            #调用保存信息函数
            saveinfo(stock,count)
        except:
            print('-----该股票在百度股市通未收录-----'+url)


def saveinfo(stock,count):
    '''保存股票信息'''
    path = "D:/baidu/"
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        print('正在保存{}股票信息,当前保存进度为{:.2f}%'.format(stock['股票名称'],count*100/ 898))
        for key,values in stock.items():
            with open(path+'Gupiao.txt','a')as f:
                f.write(key + ':')
                f.write(values + '\t')
                f.close()
        with open(path+'Gupiao.txt','a')as file:
            file.write('\n\n')
            file.close()
    except:
        print('提示：未收录股票无相关信息，当前保存进度为{:.2f}%'.format(count * 100 / 898))


def main():
    '''程序入口'''
    stock_url = 'http://quote.eastmoney.com/stocklist.html'
    html = getHtmltext(stock_url)
    urllist = getstocklist(html)
    #股票代码列表长度为：4487 print(len(urllist))
    #给线程分工，分别执行列表里哪些数据
    ta = threading.Thread(target=getbainfo,args=(urllist[:898],))
    tb = threading.Thread(target=getbainfo,args=(urllist[898:1796],))
    tc = threading.Thread(target=getbainfo, args=(urllist[1796:2694],))
    td = threading.Thread(target=getbainfo, args=(urllist[2694:3592],))
    te = threading.Thread(target=getbainfo, args=(urllist[3592:4487],))
    #开始线程
    ta.start()
    tb.start()
    tc.start()
    td.start()
    te.start()
if __name__ == '__main__':
    main()
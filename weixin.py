import requests
from bs4 import BeautifulSoup
import bs4
import xlwt
from hashlib import md5
import os


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

def gethtml(url):
    '''解析页面源码'''
    try:
        #添加浏览器头，访问超时
        html = requests.get(url,headers=headers,timeout=30)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        return html.text
    except:
        print('获取页面源码失败')


def getchaturls(html):
    '''获取每页信息详情链接'''
    try:
        soup = BeautifulSoup(html,'html.parser')
        chat_url = []
        for chat in soup.find_all('div',class_='border5'):
            chat = chat.a.attrs['href']
            chat_url.append('http://www.weixinqun.com'+chat)
        return chat_url
    except:
        print('获取页面详细详细链接失败')


def getinfo(url,infos):
    '''获取链接详情页面所需信息'''
    try:
        picurls = []
        html = gethtml(url)
        soup = BeautifulSoup(html,'lxml')
        pic = soup.find('div',class_='iframe')
        x = pic.find_all('span',class_='shiftcode')
        #判断是否详情页面是否有群主及群二维码
        if len(x) == 2:
            picurls.append(x[0].img.attrs['src'])
            picurls.append(x[1].img.attrs['src'])
        else:
            picurls.append(pic.img.attrs['src'])
        #找到详情页面需要数据所在的标签
        clearfix = soup.find('div',class_='des_info')
        #在需要的标签内获取标题
        title = clearfix.find('span',class_='des_info_text').get_text().replace('\n','').replace(' ','').replace(':','')
        #获取详细信息
        for info in clearfix.find('ul').children:
            if isinstance(info, bs4.element.Tag):
                other = info('li')
                for a in other:
                    infos.append(a.get_text().replace('\n','').replace(' ',''))
        #获取微信号
        waccount = clearfix.find_all('span',class_='des_info_text2')
        infos.append('微信号：'+waccount[1].get_text().replace('\n','').replace(' ',''))
        #获取热度
        hot = clearfix.find_all('span',class_='Pink')
        infos.append('热度：'+hot[0].get_text().replace('\n','').replace(' ',''))
        print('正常处理的详情标题：{}'.format(title))
        #调用保存二维码方法
        savepic(picurls,title)
    except:
        print('详情页面解析失败')


def saveinfo(infoms):
    '''保存excel文件'''
    wb = xlwt.Workbook()
    ws = wb.add_sheet('wchat')
    ws.write(0, 0, '行业')
    ws.write(0, 1, '时间')
    ws.write(0, 2, '地区')
    ws.write(0, 3, '标签')
    ws.write(0, 4, '微信号')
    ws.write(0, 5, '热度')
    pp = 1
    for b in range(0, len(infoms), 6):
        ws.write(pp, 0, infoms[b])
        ws.write(pp, 1, infoms[b + 1])
        ws.write(pp, 2, infoms[b + 2])
        ws.write(pp, 3, infoms[b + 3])
        ws.write(pp, 4, infoms[b + 4])
        ws.write(pp, 5, infoms[b + 5])
        pp += 1
        wb.save('D://微信群//wchat.xls')


def savepic(picurls,title):
    '''保存群或群主/个人微信二维码'''
    path = 'D://微信群//'
    if not os.path.exists(path):
        os.mkdir(path)
    path1 = path+title+'//'
    if not os.path.exists(path1):
        os.mkdir(path1)
    for url in picurls:
        photo = requests.get(url,headers=headers).content
        filename = md5(photo).hexdigest()
        with open(path1+filename+'.jpg','wb') as f:
            f.write(photo)
            f.close()


def infossplit(infos):
    '''字符串切片操作'''
    infoms = []
    for info in infos:
        info = info.split('：')[1]
        infoms.append(info)
    return infoms


def main():
    '''程序入口'''
    #创建空列表存放详情
    infos = []
    for page in range(0,2): #页面默认第一页为0，请至页面查看最后一页的数字，将最后一页数字加1输入括号第二位置
        #如需其他类型，请至浏览器查看对应类型链接的t值，如微信群链接开头为：http://www.weixinqun.com/group，个人链接开头为：http://www.weixinqun.com/personal
        first_url = 'http://www.weixinqun.com/personal?t=52&p={}'.format(page)
        print('正在处理第{}页，链接为：{}'.format(page,first_url))
        html = gethtml(first_url)
        urls = getchaturls(html)
        for url in urls:
            print('=====分隔符=====')
            print('正在处理第{}页，内容详情链接为：{}'.format(page,url))
            getinfo(url,infos)
    infoa = infossplit(infos)
    saveinfo(infoa)
    print('=====全部处理完成=====')

if __name__=='__main__':
    main()
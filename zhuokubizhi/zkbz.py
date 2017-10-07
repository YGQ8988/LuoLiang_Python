from bs4 import BeautifulSoup
import requests
import re
import os
from Set import *
import multiprocessing

def getHtml(url):
    '''获取HTML文本'''
    try:
        html = requests.get(url,headers=HEADERS,timeout=15,proxies=PROEX)
        html.encoding = html.apparent_encoding
        html.raise_for_status()
        return html.text
    except BaseException as f:
        print('获取HTML文本失败，错误信息为：',f)

def geturl(html,seting):
    '''获取每张图片URL'''
    try:
        soup = BeautifulSoup(html,'lxml')
        urlhtml = soup.find_all('div',class_='bizhiin')
        patten = re.compile('<a href="(.*?)" target="_blank">')
        urllist = re.findall(patten,str(urlhtml))
        for url_b in urllist:
            url = seting + url_b
            yield url
    except BaseException as f:
        print('获取专辑链接失败，错误信息为：',f)

def getimg(url):
    '''获取图片真实URL'''
    try:
        html = getHtml(url)
        soup = BeautifulSoup(html,'lxml')
        imgs = soup.find('div',id='bizhiimg')
        patten = re.compile('<img alt=".*?" id="imageview" name="images1" src="(.*?)"/>')
        imgurl = re.findall(patten,str(imgs))
        return imgurl[0]
    except BaseException as f:
        print('获取图片真实URL失败，错误信息为：',f)

def gettitle(url):
    '''获取专辑标题'''
    try:
        html = getHtml(url)
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('div',id='liebiaom')
        return (title.h1.get_text().split(' ')[0])
    except BaseException as f:
        print('获取专辑链接标题失败，错误信息为：',f)

def spath(title):
    '''创建保存目录'''
    try:
        first_path = PATH
        if not os.path.isdir(first_path):
            os.mkdir(first_path)
        save = PATH+title+BACKSLASH
        if not os.path.isdir(save):
            os.mkdir(save)
        return save
    except BaseException as f:
        print('创建目录失败，错误信息为：',f)

def savaimg(initurl,url,path):
    '''保存图片'''
    try:
        headers = {
                    "Host": "bizhi.zhuoku.com",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
                   "Referer": initurl
                   }
        filename = url.split('/')[-1]
        file = open(path+filename,'wb')
        r = requests.get(url,headers=headers,timeout=15,proxies=PROEX).content
        file.write(r)
        file.close()
    except BaseException as f:
        print('保存图片失败，URL:{},错误信息为：'.format(url),f)
        
def main(page):
    '''主程序'''
    try:
        initialurl = 'http://www.zhuoku.com/zhuomianbizhi/show/index-{}.htm'.format(page)
        html = getHtml(initialurl)
        num = 0
        for url in geturl(html, FIRST):
            iurl = url.split('/', 5)
            html1 = getHtml(url)
            title = gettitle(url)
            savepath = spath(title)
            print('-----正在保存{}专辑链接-----'.format(title))
            for surl in geturl(html1, FENGJING + iurl[4] + SLASH):
                imgurl = getimg(surl)
                savaimg(url, imgurl, savepath)
                num += 1
                print('-----专辑链接：{}，成功保存{}张图片-----'.format(url,num))
    except BaseException as f:
        print('主程序运行出错，错误信息为：',f)

if __name__ == '__main__':
    '''多进程处理'''
    threads = []
    #这里的就是所有index页数，大家可以去页面看总页数在这里填上（加1）。
    for page in range(1,36):
        t = multiprocessing.Process(target=main,args=(page,))
        threads.append(t)
    for a in range(len(threads)):
        threads[a].start()
import requests
import json
from bs4 import BeautifulSoup
import re
import os


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}


def getHTML(keyword,offset):
    '''获取JSON页面源码'''
    date = {
        'offset':offset*20,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1
    }
    url = 'http://www.toutiao.com/search_content/?'
    try:
        r = requests.get(url,headers=headers,params=date)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('JSON页面加载异常')


def get_json(html):
    '''从JSON解析得到需要的链接'''
    try:
        urls = []
        urljs = json.loads(html)
        urljs = urljs.get('data')

        for i in range(0,len(urljs)):
            urls.append(urljs[i]['url'])
        return urls
    except:
        print('JSON内容解析失败')


def getjphtml(url):
    '''获取找到链接源码'''
    try:
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('街拍详情源码获取失败')


def getpicurl(html):
    '''获取街拍标题，页面图片链接'''
    try:
        photos = set()
        pat = 'http://p.{1}\.pstatp\.com/large/.{15,20}|http:\\\/\\\/p.{1}\.pstatp.com\\\/origin\\\/.{15,20}'
        photo = re.findall(pat, html)
        for url in photo:
            url = url.replace('\\', '')
            photos.add(url)
        pat_t = "title: '.*?',"
        titles = re.findall(pat_t,html)
        for title in titles:
            title = title.split(':')
            title = title[1].replace(',','').replace('\'','')
            print('正在保存标题为：{}内图片'.format(title))
            print('-----分隔符-----')
            #调用保存文件函数
            get_photos(title, photos)
    except:
        print('该链接为广告')


def get_photos(title,urllist):
    '''保存文章内图片'''
    try:
        path = 'D:/今日头条/'
        if not os.path.exists(path):
            os.mkdir(path)
        path1 = 'D:/今日头条/'+title+'/'
        if not os.path.exists(path1):
            os.mkdir(path1)
        for url in urllist:
            photo = requests.get(url,headers=headers)
            photo = photo.content
            with open(path1 + url.split('/')[-1] + '.jpg','wb')as f:
                f.write(photo)
                f.close()
    except:
        print('图片保存失败')


def main():

    print('-----如输入内容未成功保存图片，还请谅解，能力有限-----此代码依据大神们爬街拍编写-----')
    key = input('请输入关键字（妹子，美女，街拍）：')
    first = int(input('请输入需要爬取的开始页（从0开始）：'))
    second = int(input('请输入需要爬取的结束页：'))
    for page in range(first,second):
        jshtml = getHTML(key,page)
        get_json(jshtml)
        urls = get_json(jshtml)
        for url in urls:
            print('当前正在处理的链接为：{}'.format(url))
            html = getjphtml(url)
            getpicurl(html)
    print('-----此次运行已完成-----')


if __name__ == '__main__':
    main()
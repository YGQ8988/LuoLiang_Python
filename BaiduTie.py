import requests
from urllib.parse import urlencode
import os
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
           }
def GetFistPage(kw,pn):
    data={
        'kw' : kw ,
        'ie' :'utf-8',
        'pn' : pn
    }
    url = 'http://tieba.baidu.com/f?'+urlencode(data)
    print(url)
    try:
        r = requests.get(url,headers=headers)
        if r.status_code == 200:
            return r.text
        print("连接异常")
        return None
    except RequestException:
        print("其他异常")
        return None

def parser_firstPage(html,pagelists):
    re_href = re.compile('<a href="(/p/\d+?)".+?title="(.+?)"',re.S)
    re_titles = re.findall(re_href,html)
    print(re_titles)
    for i in range(len(re_titles)):
        pagelists.append({
             'title':re_titles[i][1],
             'url'  :re_titles[i][0]
         } )
    return pagelists
def GetPersonPage(urls):
    url='http://tieba.baidu.com' + urls['url']
    print(url,urls['title'])
    try:
        r =requests.get(url)
        if r.status_code==200:
            return r.text
        return None
    except RequestException:
        return None

def  ParserPersonPage(html):
    pageconcentlist=[]
    soup = BeautifulSoup(html,'lxml')
    page_infos = soup.find("div",{"id":"j_p_postlist"})
    for page_info in page_infos.children:
        if page_info.find(class_='d_name')  :
            pageconcentlist.append( {'name':page_info.find(class_='d_name').text.strip(),
                   'concent':page_info.find('cc').text.strip()})
        else:
            continue
    return pageconcentlist
def SaveComputer(pagelist,info):
    path = "D:\\Baidu\\"
    root =pagelist['title']+'.txt'
    paths =path+root
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.isdir(paths):
        try:
            with open(paths,'w',encoding='utf-8') as f:
                    f.write(
                        '帖子标题:'+pagelist['title']+'\t'+
                        '帖子链接:'+'http://tieba.baidu.com' + pagelist['url']
                    )
            with open(paths, 'a', encoding='utf-8') as f:
                for i in range(len(info)):
                    f.write(
                        '\n' + info[i]['name'] + ":" + info[i]['concent']
                    )
        except OSError:
            print("标题有特殊字符")

def main():
    pagelists=[]

    page_kw = input("请输入你要查询的贴吧名称")
    page_pn = input("请输入你要爬取的最大页数")
    page_pn =(int(page_pn)-1)*50
    for page_MaxNum in  range(0,page_pn+1,50):
        html = GetFistPage(page_kw,page_MaxNum)
        parser_firstPage(html,pagelists)


    for  pagelist  in pagelists:
        html = GetPersonPage(pagelist)
        info = ParserPersonPage(html)
        print(99,info)
        SaveComputer(pagelist,info)
         


if __name__ == '__main__':
    main()
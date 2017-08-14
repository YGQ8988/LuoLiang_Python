import requests
from bs4 import BeautifulSoup
import os
import re
from hashlib import md5

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def gethtml(url):
    '''获取房产页面源码'''
    try:
        html = requests.get(url,headers=headers,timeout=30)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        return html.text
    except:
        print('连接出错了')

def getUlrs(html):
    '''从页面源码中获取每个房产的链接'''
    try:
        hurls = []
        soup = BeautifulSoup(html,'lxml')
        Ulist = soup.find('ul',class_='listUl')
        urls = Ulist.find_all('h2')
        for url in urls:
            hurls.append(url.a.attrs['href'])  #获取h2下面a标签href属性值
        return hurls
    except:
        print('获取房源链接错误')

def getinfo(url,count):
    '''获取房产详情页面相关信息'''
    p_url = []
    try:
        html = gethtml(url)  #调用gethtml函数获取房产详情页面源码
        soup = BeautifulSoup(html,'lxml')
        title = soup.find('div',class_='house-title').h1.text  #获取房产标题
        infos = soup.find('div',class_='house-desc-item fl c_333')   #找到房产信息所在的标签
        price = infos.find('span',class_='c_ff552e').text     #获取房产价格
        info = infos.find('ul',class_='f14')
        info1 = info.find_all('li')
        print('正在保存：\t{}\t房屋信息'.format(title))
        save('房产名称：'+title,title)
        save('出租价格：'+price,title)
        save('58链接：'+url,title)
        for li in info1:
            liinfo = li.text.replace('\n','').replace('\t','')
            save(liinfo,title)
        save('\n',title)
        #正则匹配所有图片链接
        pics = soup.find('div', class_='big-pic-list pr')
        pic = pics.find('ul', class_='bigpic-list-wrap pa')
        aa = re.findall('http:\//.+', str(pic))
        for bb in aa:
            bb = bb.split('"')
            p_url.append(bb[0])
        #调用保存图片函数
        savap(p_url,title)

        print('=====成功保存{}条房产信息====='.format(count))
    except:
        print('获取房源详细信息出错了')

def save(text,title):
    '''保存房产信息'''
    path = 'D://58house//'
    if not os.path.exists(path):
    	os.mkdir(path)
    path_o = 'D://58house//'+title+'//'
    if not os.path.exists(path_o):
        os.mkdir(path_o)
    with open(path_o+title+'.txt','a',encoding='utf-8') as f:
        f.write(text+'\n')
        f.close()

def savap(p_list,title):
    '''保存房产图片'''
    path = 'D://58house//'+title+'//'
    if not os.path.exists(path):
        os.mkdir(path)
    for url in p_list:
        pic = requests.get(url,headers=headers).content
        filename = md5(pic).hexdigest()
        with open(path+filename+'.jpg','wb') as f:
            f.write(pic)
            f.close()

def main():
    '''程序入口'''
    try:
        print('=====房产信息TXT文本请见，D盘58house目录内=====')
        count = 0
        num = 0
        for i in range(1,71):  #通过页面观察浦东新区有70页房产信息
            num+=1
            url = "http://sh.58.com/pudongxinqu/zufang/j2/pn{}/?minprice=0_3000&PGTID=0d300008-0058-3829-4ee6-ca3306231907&ClickID=2".format(i)
            print('正在获取第{}页数据，第{}链接为：{}'.format(num,num,url))
            html = gethtml(url)
            urls = getUlrs(html)
            for url in urls:  #遍历所有房产详情链接，并保存房产信息
                count += 1
                getinfo(url,count)
    except:
        print('访问频繁，请稍后再试')

if __name__ == "__main__":
    main()

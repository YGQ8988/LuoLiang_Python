import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
def url_1(page_o,page_t):
    url_s = []
    for page in range(page_o,page_t):
        url = 'http://www.80s.tw/movie/list/-----p'+str(page)
        url_s.append(url)
    return url_s
def html(url_s):
    mv_urls = []
    for url in url_s:
        html = requests.get(url,headers=headers)
        soup = BeautifulSoup(html.text,'lxml')
        for mv in soup.find_all('h3',{'class','h3'}):
            mv_url = mv('a')[0]['href']
            mv_urls.append('http://www.80s.tw'+mv_url)
    return mv_urls
def thlj(mv_urls):
    num = 0
    print('{0:^1}\t{1:^30}\t{2:^60}'.format('排序','电影名称', '迅雷链接或磁力链接'))
    for thurl in mv_urls:
        html = requests.get(thurl,headers=headers)
        soup_t = BeautifulSoup(html.text,'lxml')
        for xlurl in soup_t.find_all('span',{'class',"xunlei dlbutton1"}):
            num+=1
            xl_lj = xlurl('a')[0]['href']
            xl_name = xlurl('a')[0]['thunderrestitle']
            print('{0:^1}\t{1:^30}\t{2:^60}'.format(num,xl_name,xl_lj))
#page_o = int(input('请输入需要爬取的开始页：'))
#page_t = int(input('请输入需要爬取的结束页：'))
thlj(html(url_1(1,2)))
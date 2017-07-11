import requests
from bs4 import BeautifulSoup
User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
headers = {'User-Agent':User_Agent}
url = "http://www.jianshu.com/"
html = requests.get(url)
soup = BeautifulSoup(html.text,"lxml")    #将html对象转化为BeautifulSoup对象
liList = soup.select('.author')    #找到所有li
for li in liList:
    a = 'http://www.jianshu.com/' + li.select('a')[0]['href']
    b = li.select('a')[1].text
    print(a,b)

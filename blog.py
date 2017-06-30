import requests
from bs4 import BeautifulSoup
import bs4
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = 'http://blog.csdn.net/wojiushiwo945you/article/details/53227250'
html = requests.get(url,headers=headers)
soup = BeautifulSoup(html.text,'html.parser')
for title in soup.find('span',{'class':'link_title'}):
    if isinstance(title, bs4.element.Tag):
        print('-----文章标题-----：',title.text)
        file = open('blog.txt','w')
        file.write(str(title.text))
        file.close()
print('-----文章内容-----：\n')
for p in soup.find('div',{'class':'article_content'}).children:
    if isinstance(p, bs4.element.Tag):
        print(p.text)
        file = open('blog.txt', 'a')
        file.write(str(p.text))
        file.close()


import  requests
from bs4 import BeautifulSoup
for a in range(1,6):
    url = 'http://blog.csdn.net/fly_yr/article/list/'+str(a)

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    headers = {'User-Agent':user_agent}

    html = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    for wz in soup.select('.link_title'):
        a = 'http://blog.csdn.net'+wz.select('a')[0]['href']
        b = wz.select('a')[0].text
        print(a,b)
        file = open('boke.txt','a')
        file.write(b+'\n'+a)
        file.close()
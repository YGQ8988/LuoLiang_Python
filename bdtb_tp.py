import urllib.request
import re,os
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html
def get_img(html):
     p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
     imglist = re.findall(p,html)
     try:
         os.mkdir('NewPics')
     except FileExistsError:
         pass
     os.chdir('NewPics')
     for each in imglist:
         filename = each.split('/')[-1]
         urllib.request.urlretrieve(each,filename,None)

url = 'http://tieba.baidu.com/p/3823765471'
a = open_url(url)
get_img(a)
import requests
import hashlib
import re
import os
page_o = int(input('请输入开始爬取的页数：'))
page_t = int(input('请输入结束爬取的页数：'))
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
def mz_url():
    for page in range(page_o,page_t):
        url = 'http://jandan.net/ooxx/page-'+str(page)
    return url
def save_path():
    s_path = 'D:\\mizitu\\'
    if not os.path.isdir(s_path):
        print('----------该目录不存在----------')
        print('----------正在创建该目录----------')
        os.mkdir(s_path)
    else:
        print('----------该目录已存在，不再创建----------')
    return s_path

def s_photo(url,s_path):
    num = 0
    html  = requests.get(url)
    html.encoding = html.apparent_encoding
    photos  = re.findall('wx\d.*?\.jpg',html.text)
    for photo in photos:
        num += 1
        photo_url = 'http://' + photo
        save_photo = requests.get(photo_url, headers=headers).content
        filename = hashlib.md5(save_photo).hexdigest()  
        with open(s_path+ str(filename) + '.jpg', 'wb')as f:
            f.write(save_photo)
            print('----------正在保存第%d图片'%num+photo_url+'----------')
            f.close()
    print('----------成功保存%d张图片----------'%num)
s_photo(mz_url(),save_path())

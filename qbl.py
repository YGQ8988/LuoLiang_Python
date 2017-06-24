import requests,re,os,hashlib  #一次性引入需要用到的模块
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}  #设置user-agent模拟浏览器
range1 = int(input('请输入需要爬取开始的页数（最少从第二页开始）：'))
range2 = int(input('请输入需要爬取结束的页数：'))
url_all = []  #创建一个空列表，后续存放爬取到页面列表的URL链接
def qbl_urls():   #此函数就是获取所有页面上专辑汇总的链接
    for page in range(range1,range2): #使用for迭代获取需要爬取的页面数据
        html = requests.get('https://5555av.co/html/tupian/yazhou/index_'+str(page)+'.html') #这个就不多说了，大家应该都看得懂
        html.encoding = 'utf-8' #设置编码（其实我也没搞懂这是编码还是解码。反正每个模块的使用方法不一样，但是达到的效果都是一样的
        urls = re.findall('.*?\d\d\d\d/\d\d\d\d\d\d\.html',html.text)  #使用正则表达式需要的链接
        for url in urls: 
            h_urls = url.split('"') #将匹配到的数据切片，切成自己需要的数据
            full_url = 'https://5555av.co'+ h_urls[1] #然后用自己需要的链接和网站开头部分拼接（切片后不是完整的链接，所以这里拼接了下
            url_all.append(full_url) #将拼接成功的链接放入，开始创建的空列表
    return url_all #返回该列表，给后面的函数做参数使用
def pic_path():  #此函数为创建目录
    save_path = 'D:\qianbailu'  #首先自己定义一个目录
    if not os.path.isdir(save_path): #判断目录是否存在
        print('----------该目录不存在----------')
        print('----------正在创建该目录----------')
        os.makedirs(save_path) #不存在则创建该目录
    else:
        print('----------该目录已存在----------')
    return save_path #返回该目录，给后面的函数做参数使用
def save_pics(url_all,save_path): #此函数为保存图片的函数
    list_url = [] #创建一个空列表，存放需要保存图片的链接
    sull = 0 #创建一个参数，后面打印信息用到
    for pic_url in url_all: #迭代上面函数返回的专辑链接
        pic = requests.get(pic_url,headers=headers)
        pics = re.findall('//.*?\d\d\d\d\d\d/\d\d/.*\.jpg',pic.text) #正则匹配图片的链接
        for photos_url in pics: #迭代匹配的到的图片链接
            photo_url = photos_url.split('"') #切片匹配的的数据，切成真正的图片链接，大家也可以尝试去掉这行，打印出来。看看匹配到的列表是什么样的
            for save_url in photo_url: #再迭代切片好的图片链接
                if len(save_url) == 46: #放心真的得图片链接在列表里长度都是一致的，所有这里筛选下
                    list_url.append(save_url) #把筛选出来的真正图片链接放入上面创建的空列表中
    list_url = set(list_url) #用集合去重下
    for save_urls in list_url: #由于上面获得的也是一个列表，所以再迭代下访问真正的图片链接
        save_photo = requests.get('http:'+save_urls,headers=headers).content   #使用content方式访问链接
        filename = hashlib.md5(save_photo).hexdigest() #获取链接图片的MD5作为文件名
        with open(save_path+'\\'+str(filename)+'.jpg','wb')as f: #保存文件
            f.write(save_photo) #写入文件
            f.close() #关闭文件
            sull +=1 #每次成功一个此处加1
            print('成功保存第%d张图片：http:'%sull+save_urls) #打印出保存成功的信息
    print('----------成功保存%d张图片----------'%sull) #全部保存成功后打印此行信息
save_pics(qbl_urls(),pic_path()) #运行最后一个函数，里面两个参数就是上面两个函数运行返回的参数

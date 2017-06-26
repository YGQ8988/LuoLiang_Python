from bs4 import BeautifulSoup #导入bs4解析库
import requests,re,os,hashlib #导入全部写在这一行里面了
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
#设置浏览器User-Agent（模拟浏览器访问）

def urls1():   #创建获取页面专辑链接地址
    nums1 = int(input('请输入你要爬取的开始页数：'))
    nums2 = int(input('请输入你要爬取的结束页数：'))
    urls = []   #设置一个空列表，获取后加入到该列表中
    for num in range(nums1,nums2):
        url = 'http://www.zhuoku.com/zhuomianbizhi/star/index-'+str(num)+'.htm'
        #依次访问输入开始至结束的页面
        html = requests.get(url=url,headers=headers)
        html.encoding = 'gb2312' #设置编码，防止获取的页面文本乱码
        soup = BeautifulSoup(html.text,'lxml')
        for a in soup.select('.bizhiin'):
            b = a.select('a')[0]['href'] #获取 div 下bizhiin里所有链接
            c = 'http://www.zhuoku.com'+b  #由于获取到的不是完整的，这里拼接了下
            print('正在获取需要下载的地址链接:',c)
            urls.append(c)
    return urls   #返回需要下载的地址列表，以便后面函数调用
def pathdir():
    e = 'D:\\bizhi'
    if not os.path.isdir(e): #判断目录是否存在，不存在则创建
        print('-----不存在该目录-----')
        print('-----正在创建该目录-----')
        os.makedirs(e)  #使用os模块在本地创建目录
        print('-----目录创建成功-----')
    else:
        print('-----该目录已存在-----')
    return e  #返回创建的目录，后面保存用。
def urls2(urls,e):  #创建获取高清壁纸函数
    photos = []  #创建空列表，后续存放高清壁纸链接
    number = 0  
    for urlss in urls:  #迭代上面返回的专辑链接
        for x in range(1,6):  #只保存一个专辑内5张图片
            y = urlss.split('.')  #将获取的链接切片
            z = y[2]+'('+str(x)+')'+'.'+y[3] #拼接成高清图片后缀链接
            r = 'http://www.zhuoku.'+z    #拼接成完整链接
            print('正在获取专辑汇总链接：',r)
            pic = requests.get(url=r,headers=headers)
            pics = re.findall('http.*/\d{4}/\d{2}/\d{2}.*\.jpg',pic.text) #用RE匹配高清图片下载地址
            for photo in pics:
                if photo not in photos:
                    photos.append(photo)  #去重处理
    for pict in photos:
        pices = requests.get(pict).content  #已content模式访问图片地址
        filename = hashlib.md5(pices).hexdigest()  #获取图片MD5值，作为文件名
        with open(e+'\\'+str(filename)+'.jpg','wb')as f:  #保存图片
            number = number + 1
            print('成功保存%d张图片：'% number,pict)
            f.write(pices)
            f.close()
    print('-----全部下载成功-----')

urls2(urls1(),pathdir())  #调用保存图片函数

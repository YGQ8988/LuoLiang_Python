from bs4 import BeautifulSoup
import requests,re,os,hashlib
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def urls1():
	nums1 = int(input('请输入你要爬取的开始页数：'))
	nums2 = int(input('请输入你要爬取的结束页数：'))
	urls = []
	for num in range(nums1,nums2):
		url = 'http://www.zhuoku.com/zhuomianbizhi/star/index-'+str(num)+'.htm'
		html = requests.get(url=url,headers=headers)
		html.encoding = 'gb2312'
		soup = BeautifulSoup(html.text,'lxml')
		for a in soup.select('.bizhiin'):
			b = a.select('a')[0]['href']
			c = 'http://www.zhuoku.com'+b
			print('正在获取需要下载的地址链接:',c)
			urls.append(c)
	return urls
def pathdir():
	e = 'D:\\bizhi'
	if not os.path.isdir(e):
		print('-----不存在该目录-----')
		print('-----正在创建该目录-----')
		os.makedirs(e)
		print('-----目录创建成功-----')
	else:
		print('-----该目录已存在-----')
	return e
def urls2(urls,e):
	photos = []
	number = 0
	for urlss in urls:
		for x in range(1,6):
			y = urlss.split('.')
			z = y[2]+'('+str(x)+')'+'.'+y[3]
			r = 'http://www.zhuoku.'+z
			print('正在获取专辑汇总链接：',r)
			pic = requests.get(url=r,headers=headers)
			pics = re.findall('http://bizhi.zhuoku.com.*?\.jpg',pic.text)
			for photo in pics:
				if photo not in photos:
					photos.append(photo)
	for pict in photos:
		pices = requests.get(pict).content
		filename = hashlib.md5(pices).hexdigest()  #获取图片MD5值，作为文件名
		with open(e+'\\'+str(filename)+'.jpg','wb')as f:
			number = number + 1
			print('成功保存%d张图片：'% number,pict)
			f.write(pices)
			f.close()
	print('-----全部下载成功-----')

urls2(urls1(),pathdir())
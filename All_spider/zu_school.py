import requests,bs4
from bs4 import BeautifulSoup
def uvlist(url):
	ulist = []  #创建空列表存放大学信息
	url = requests.get(url)
	url.encoding = url.apparent_encoding   #猜取页面编码并进行编码
	soup = BeautifulSoup(url.text,'lxml')  #解析HTML
	for tr in soup.find('tbody').children: #找到tbody下的子标签，并进行遍历
		if isinstance(tr,bs4.element.Tag): #判断是否是tr下的标签
			tds = tr('td')  #获取tr节点下的td标签
			ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])  #截取排名，学校名称，省市，总分，指标得分
	return ulist
def uvprint(ulist):
	print("{0:^10}\t{1:{5}^10}\t{2:{5}^10}\t{3:^10}\t{4:^10}".format('排名','学校名称','地区','总分','指标得分',chr(12288))) #用format打印标题
	for i in range(0,20):  #只截取排名前20名的学校
		u = ulist[i]       #从上面加进去的列表中取值
		print("{0:^10}\t{1:{5}^10}\t{2:{5}^10}\t{3:^13}\t{4:^10}".format(u[0],u[1],u[2],u[3],u[4],chr(12288))) #对应标题打印

url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
info = uvlist(url)
uvprint(info)
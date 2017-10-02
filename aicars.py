# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import threading
import gevent
from gevent import monkey

headers = {
    		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    		}

def gethtml(url):
	'''获取URL HTML文本'''
	proex = {'https':"https://104.225.151.169:26205"}
	try:
		html = requests.get(url,headers=headers,timeout=15,proxies=proex)
		html.encoding = html.apparent_encoding
		html.raise_for_status()
		return html.text
	except BaseException as f:
		print('获取主页源码失败了，错误信息为：',f)

def geturls(html):
	'''匹配所有车辆URL ID'''
	try:
		patten = re.compile('a href="(/\d+/)" target="_blank"')
		urls = re.findall(patten,html)
		return urls
	except BaseException as f:
		print('获取URL失败，错误信息为：',f)

def getpages(url):
	'''获取每款车辆评价数量'''
	try:
		html = gethtml(url)
		soup = BeautifulSoup(html,'lxml')
		page = soup.find(class_='unify_page mt20')
		pat_f = re.compile('''rel="nofollow">(\d+)</a>''')
		pages = re.findall(pat_f,str(page))
		return pages
	except BaseException as f:
		print('获取URL失败，错误信息为：',f)

def getall(pages,url,purposes):
	'''构造Ajax请求参数'''
	try:
		if len(pages) == 0:
			date = getinfo(url,purposes)
			return date
		else:
			date = getinfo(url,purposes)
			id = url.split('/',4)[3] #切片获取车辆URL ID值
			#判断评价页数，大于10页只获取10页数据，小于10全部获取
			if int(pages[-1]) > 10:
				listone = list(range(2,11))
				ta = threading.Thread(target=getmoinfo,args=(listone[:4], id, purposes,))
				tb = threading.Thread(target=getmoinfo, args=(listone[4:6], id, purposes,))
				tc = threading.Thread(target=getmoinfo, args=(listone[6:9], id, purposes,))
				ta.start()
				tb.start()
				tc.start()
			else:
				listone = list(range(2,int(pages[-1])))
				ta = threading.Thread(target=getmoinfo, args=(listone[:int(pages[-1])],id,purposes,))
				ta.start()
			return date
	except BaseException as f:
		print('获取URL失败，错误信息为：',f)

def getmoinfo(page,id,purposes):
	'''遍历所有AjaxURL，并获取购车用途'''
	data = {'r': 'reputation/reputation/GetAjaxKbList3',
			'page': page,
			'pserid': id,
			'jh': '0',
			'wd': '0'}
	f_url = 'http://newcar.xcar.com.cn/auto/index.php'
	url = requests.get(f_url,params=data).url
	try:
		html = gethtml(url)
		soup = BeautifulSoup(html,'lxml')
		#购车用途
		purposee = soup.find_all(class_='purpose clearfix')
		pat_s = re.compile('<em>(.*?)</em>')
		purpose = re.findall(pat_s,str(purposee))
		purposes.append(purpose)	
	except BaseException as f:
		print('获取数据失败，错误信息为：',f)

def getinfo(url,purposes):
	'''获取车辆综合评分'''
	try:
		data = {}
		html = gethtml(url)
		soup = BeautifulSoup(html,'lxml')
		pat_o = re.compile('<p>综合评分：<em>(.*?)</em>分</p>')
		#综合评分
		synthesis = re.findall(pat_o,str(soup))
		#车型
		title = soup.find(class_='tt_h1').get_text()
		#整体评分
		infos = soup.find(class_='column')
		pat_t = re.compile('\d+\.\d+分')
		info = re.findall(pat_t,str(infos))
		#购车用途
		purposee = soup.find_all(class_='purpose clearfix')
		pat_s = re.compile('<em>(.*?)</em>')
		purpose = re.findall(pat_s,str(purposee))
		purposes.append(purpose)
		data['车型'] = title.strip()
		data['综合评分'] = synthesis[0]
		data['外观'] = info[0]
		data['内饰'] = info[1]
		data['空间'] = info[2]
		data['舒适'] = info[3]
		data['耗油'] = info[4]
		data['动力'] = info[5]
		data['操控'] = info[6]
		data['性价比'] = info[7]
		return data
	except BaseException as f:
		print('获取数据失败，错误信息为：',f)

def main(urls,num):
	'''程序入口'''
	try:
		conn = MongoClient('127.0.0.1', 27017)
		db = conn.cars
		cars = db.cars
		for url1 in urls:
			num += 1
			url = 'http://newcar.xcar.com.cn' + url1 + 'review.htm'
			if requests.get(url).url != url:
				print('该车型没有综合评分及购车用途',url)
			else:
				purposes = []
				print('正在处理第{}个链接，URL:{}'.format(num,url))
				pages = getpages(url)
				data = getall(pages,url,purposes)
				clearfix = {}
				call = []
				#将所有购车用途遍历，重新加入新的列表，进行统计出现次数
				for a in purposes:
					for b in a:
						call.append(b)
				for c in set(call):
						clearfix[c] = call.count(c)
				data['购车用途'] = clearfix
				cars.insert(data)
				print('成功保存{}条数据'.format(num))
	except BaseException as f:
		print('主函数运行出错了，错误信息为：',f) 

if __name__ == '__main__':
	url = "http://newcar.xcar.com.cn/price/"
	html = gethtml(url)
	urls = geturls(html)
	monkey.patch_all()
	jobs = []
	num = 0
	for x in range(190):
		job = None
		if x == 0:
			job = gevent.spawn(main, urls[1:(x+1)*10],num)
		elif 0 < x < 189:
			job = gevent.spawn(main, urls[x*10+1:(x+1)*10],num)
		else:
			job = gevent.spawn(main, urls[x*10+1:1891],num)
		jobs.append(job)
	gevent.joinall(jobs)
	print('----------全部保存成功----------')


	
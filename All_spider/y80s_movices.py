import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import gevent
from gevent import monkey

headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
			'Host':'www.80s.tw'
			}

def get_html(url):
	'''获取每页HTML文本'''
	try:
		html = requests.get(url,headers=headers,timeout=30)
		html.encoding = 'utf-8'
		html.raise_for_status()
		return html.text
	except BaseException as f:
		print('获取HTML文本失败，错误信息为',f)


def get_url(html):
	'''获取每页HTML文本内电影链接'''
	try:
		soup = BeautifulSoup(html,'lxml')
		urlslist = soup.find('ul',class_='me1 clearfix')
		patten = re.compile('/movie/\d+')
		urls = re.findall(patten,str(urlslist))
		for url in urls:
			url = 'http://www.80s.tw' + url
			yield url
	except BaseException as f:
		print('获取URL失败，错误信息为',f)


def get_info(url):
	'''获取每个电影链接内需要的数据'''
	try:
		date = {}
		html = get_html(url)
		soup = BeautifulSoup(html,'lxml')
		title = soup.find('h1',class_='font14w').text
		infos = soup.find('ul',class_='dllist1')
		patten = re.compile('href="(.*?)".+?src="(.*?)"',re.S)
		clist = re.findall(patten,str(infos))
		date['电影名称'] = title
		date['电影详情链接'] = url
		for a in set(clist):
			date['迅雷链接'] = a[0]
			date['磁力链接'] = a[1]
		return date
	except BaseException as f:
		print('获取下载链接出错了，错误信息为：',f)


def main(pages):
	'''程序入口'''
	try:
		#数据库连接
		conn = MongoClient('127.0.0.1', 27017)
		db = conn.movies
		movies = db.movies
		for page in pages:
			first_url = 'http://www.80s.tw/movie/list/-----p{}'.format(str(page))
			print('正常处理：{}'.format(first_url))
			html = get_html(first_url)
			for url in set(get_url(html)):
				print('正在保存链接：{}的数据'.format(url))
				date = get_info(url)
				movies.insert(date)
	except BaseException as f:
		print('主程序运行出错了，错误信息为：',f)

if __name__=='__main__':
	'''主程序'''
	urllist = list(range(402))
	#多线程处理
	monkey.patch_all()
	jobs=[]
	for x in range(41):
		job=None
		if x==0:
			job=gevent.spawn(main, urllist[1:(x+1)*10])
		elif 0 < x < 40:
			job=gevent.spawn(main, urllist[x*10+1:(x+1)*10])
		else:
			job=gevent.spawn(main, urllist[x*10+1:402])
		jobs.append(job)
	gevent.joinall(jobs)
	print('----------全部保存成功----------')

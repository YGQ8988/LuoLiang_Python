import requests
import json
import os
from seting import *
import multiprocessing

headers = {
	'Cookie':'newpuid=150772674763615998; beans_dmp=%7B%22admaster%22%3A1507726748%2C%22shunfei%22%3A1507726748%2C%22reachmax%22%3A1507726748%2C%22lingji%22%3A1507726748%2C%22yoyi%22%3A1507726748%2C%22ipinyou%22%3A1507726748%2C%22ipinyou_admaster%22%3A1507726748%2C%22jingzan%22%3A1507726748%2C%22miaozhen%22%3A1507726748%2C%22aodian%22%3A1507726748%2C%22diantong%22%3A1507726748%2C%22huayang%22%3A1507726748%7D; vjuids=1291dbccb3.15f0b846a85.0.216feab1d521; IPLOC=CN3101; SUV=1710071456004699; ppinf=2|1507726836|1508936436|bG9naW5pZDowOnx1c2VyaWQ6NDQ6NTdBMjM4QUUzOUE2NkY4NkE3M0ZBODUzRjVDQzQyNzlAcXEuc29odS5jb218c2VydmljZXVzZTozMDowMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDB8Y3J0OjA6fGVtdDoxOjB8YXBwaWQ6NDoxMDc0fHRydXN0OjE6MXxwYXJ0bmVyaWQ6MTowfHJlbGF0aW9uOjA6fHV1aWQ6MTY6ZTI5MzcxN2M1ODgzNDAweHx1aWQ6MTY6ZTI5MzcxN2M1ODgzNDAweHx1bmlxbmFtZToyNzolRTclQkQlOTElRTUlOEYlOEI1NjYwNzQ1OTZ8cmVmdXNlcmlkOjMyOjU3QTIzOEFFMzlBNjZGODZBNzNGQTg1M0Y1Q0M0Mjc5fHJlZm5pY2s6MTM6TWVsb2R5IC0g5a6I5oqkIOKXjnw; pprdig=GyOblAuDaVdoa8tvAtLjHh9Ej-rGCgck9THBTR858wBWNKux4av1sqN-KnnNsG0KwaEIEGo20lguWiY1JVc_8rjwe8IrjtSVfN6WqFrur0xTXRib8u6KReT_hZVeOEa6L0N0m7eNrxJI7doo61smXTYtJNDWnYZwtkbmcsqv6Zk; spinfo=c29odXw1N0EyMzhBRTM5QTY2Rjg2QTczRkE4NTNGNUNDNDI3OUBxcS5zb2h1LmNvbXw0MTM3ODE5NDA=; puid=15077269408678789765; ifoxinstalled=false; beans_dmp_done=1; vjlast=1507726748.1507817755.13; ppmdig=1507820929000000240ae8840a2505e53a9052f325c6a0ec; ppmdig=1507820939000000c8498997eb561773f1eaa1bb47dfe428; fuid=15077269407693445774',
	'Host':'my.tv.sohu.com',
	'Referer':'http://edu.tv.sohu.com/info/course/play.do?vid=91595455&plat=1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	'X-Requested-With':'ShockwaveFlash/27.0.0.159'
}

def getHtml(url):
	'''获取每个视频URL，HTML文本'''
	try:
		r = requests.get(url,headers=headers)
		r.encoding = r.apparent_encoding
		r.raise_for_status()
		return r.text
	except BaseException as f:
		print('获取HTML文本失败，错误信息为：',f)

def getSu(html):
	'''解析HTML文本内视频URL后缀'''
	try:
		jsons = json.loads(html)
		sulist = jsons.get('data').get('su')
		return sulist
	except BaseException as f:
		print('获取视频SU失败，错误信息为：',f)

def mkpath():
	'''创建保存目录'''
	path = 'D:\\videos\\'
	if not os.path.isdir(path):
		os.mkdir(path)
		return path
	else:
		return path

def svideos(sulist,name,path):
	'''保存视频'''
	try:
		for b in range(len(sulist)):
			vurl = 'http://al.vod.tv.itc.cn' + sulist[b]
			v = requests.get(vurl).content
			filename = name + '_'+ str(b)
			file = open(path + filename + '.mp4', 'wb')
			file.write(v)
			file.close()
			print("成功保存视频第{}部分：文件名为：{}，储存路径为：{}".format(b + 1, filename, path))
	except BaseException as f:
		print('保存视频失败，错误信息为：',f)

def main(index,path):
	'''主函数'''
	try:
		url = URLS[index]
		html = getHtml(url)
		sulist = getSu(html)
		name = ARTICLENAMES[index]
		svideos(sulist,name,path)
		print('=====全部保存成功=====')
	except BaseException as f:
		print('主函数运行失败，错误信息为：',f)

if __name__=='__main__':
    '''多进程处理'''
	path = mkpath()
	threads = []
	for index in range(61):
		t = multiprocessing.Process(target=main,args=(index,path,))
		threads.append(t)
	for a in range(len(threads)):
		threads[a].start()
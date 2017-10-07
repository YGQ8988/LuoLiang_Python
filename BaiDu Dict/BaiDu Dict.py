import requests
import json


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}


def translate(Choice,word):
	'''判断用户输入内容，传递相应翻译参数'''
	date = ['en','zh']
	if Choice == '1':
		data = {
				'from':date[0],
				'to':date[1],
				'query':word,
				'simple_means_flag':'3'
				}
		return data
	else:
		data = {
				'from':date[1],
				'to':date[0],
				'query':word,
				'simple_means_flag':'3'
				}
		return data


def getjs(data):
	'''通过POST传递参数，并返回页面源码'''
	try:
		url = 'http://fanyi.baidu.com/v2transapi'
		html = requests.post(url=url,data=data,headers=headers)
		html.raise_for_status()
		html.encoding = 'utf-8'
		return html.text
	except:
		print('\n=====哎呀，是不是断网了！=====')


def jstext(html):
	'''将页面源码解析，获取需要的内容'''
	try:
		js = json.loads(html)
		translation = js['trans_result']['data'][0]['dst']
		print('\n您需要查询的译文内容为：',translation)
		if 'keywords' in js["trans_result"].keys():
			print('\n以下为重点词汇，还请参考')
			for content in js['trans_result']['keywords']:
				print('\n重点词汇中单词：',content['word'],'\t重点词汇中解释：',content['means'],'\n')
		else:
			print('\n查询的原文中无重点词汇\n')
	except:
		print('\n未查询到翻译内容\n')

def main():
	'''程序入口'''
	print('=====本程序使用的是百度翻译接口，在这里感谢百度免费提供，请勿用于商用=====\n')
	print('=====本程序由：Python自学技术交流（QQ群号：368639036）：洛凉制作=====\n')
	print('=====如发现缺陷，还请邮件发送至：898829225@qq.com，本人会第一时间排除，修复，发布=====\n')
	binngo = False
	while binngo == False:
		Choice = input('请选择您需要的功能（1：代表英译中，2：代表中译英。如需退出请输入：q），回车进入下一步：')
		if Choice == '1' or Choice == '2':
			keyword=input('\n请输入您需要翻译的内容,回车查看结果:')
			data = translate(Choice,keyword)
			html = getjs(data)
			jstext(html)
		elif Choice == 'q':
			break
		else:
			print('\n你输入的内容有误，请重新输入：\n')
			continue

if __name__ == '__main__':
	main()
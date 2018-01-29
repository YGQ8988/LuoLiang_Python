import requests
import json


headers = {
			'Accept':'*/*',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'zh-CN,zh;q=0.9',
			'Connection':'keep-alive',
			# 'Content-Length':'153',
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie':'BAIDUID=36A32AA55A73F0257F5C0EE2BF99FA49:FG=1; BIDUPSID=36A32AA55A73F0257F5C0EE2BF99FA49; PSTM=1514444021; PSINO=5; H_PS_PSSID=1420_21094_25178_20930; locale=zh; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1514944269; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1514944269; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
			'Host':'fanyi.baidu.com',
			'Origin':'https://fanyi.baidu.com',
			'Referer':'https://fanyi.baidu.com/',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
			'X-Requested-With':'XMLHttpRequest'
}


def translate(Choice,word):
	'''判断用户输入内容，传递相应翻译参数'''
	date = ['en','zh']
	if Choice == '1':
		data = {
				'from':date[0],
				'to':date[1],
				'query':word,
				'simple_means_flag':'3',
				'sign':'238168.475497',
				'token':'083321317d5b0199679f0629956413ec'
				}
		return data
	else:
		data = {
				'from':date[1],
				'to':date[0],
				'query':word,
				'simple_means_flag':'3',
				'sign':'238168.475497',
				'token':'083321317d5b0199679f0629956413ec'
				}
		return data


def getjs(data):
	'''通过POST传递参数，并返回页面源码'''
	try:
		url = 'https://fanyi.baidu.com/v2transapi'
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
			print(html)
			# jstext(html)
		elif Choice == 'q':
			break
		else:
			print('\n你输入的内容有误，请重新输入：\n')
			continue

if __name__ == '__main__':
	main()
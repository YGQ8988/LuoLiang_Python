import random
import time


def regiun():
	'''生成身份证前六位'''
	#列表里面的都是一些地区的前六位号码
	first_list = ['362402','362421','362422','362423','362424','362425','362426','362427','362428','362429','362430','362432','110100','110101','110102','110103','110104','110105','110106','110107','110108','110109','110111']
	first = random.choice(first_list)
	return first

def year():
	'''生成年份'''
	now = time.strftime('%Y')
	#1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
	second = random.randint(1948,int(now)-18)
	age = int(now) - second
	print('随机生成的身份证人员年龄为：'+str(age))
	return second


def month():
	'''生成月份'''
	three = random.randint(1,12)
	#月份小于10以下，前面加上0填充
	if three < 10:
		three = '0' + str(three)
		return three
	else:
		return three


def day():
	'''生成日期'''
	four = random.randint(1,31)
	#日期小于10以下，前面加上0填充
	if four < 10:
		four = '0' + str(four)
		return four
	else:
		return four


def randoms():
	'''生成身份证后四位'''
	#后面序号低于相应位数，前面加上0填充
	five = random.randint(1,9999)
	if five < 10:
		five = '000' + str(five)
		return five
	elif 10 < five < 100:
		five = '00' + str(five)
		return five
	elif 100 < five < 1000:
		five = '0' + str(five)
		return five
	else:
		return five


def main():
	first = regiun()
	second = year()
	three = month()
	four = day()
	last = randoms()
	IDcard = str(first)+str(second)+str(three)+str(four)+str(last)
	print('随机生成的身份证号码为：'+IDcard)


if __name__ == '__main__':
	main()


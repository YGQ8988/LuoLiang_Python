import requests
import re


def geturl(page,key):
    '''获取搜索商品后的页面源码'''

    data = {
        'q':key,
        's':page*44
    }
    url = 'https://s.taobao.com/search?'
    try:
        html = requests.get(url,params=data)
        html.raise_for_status()
    except:
        print('-----初始链接获取失败-----')

    return html.text


def gethtml(html):
    '''匹配源码里需要的数据'''

    try:
        goods = []
        #商品标题，价格，付款人数正则表达式
        pat1 = r'\"price\":\"\d{1,5}\"'
        pat2 = r'\"title\":\".*?\"'
        pat3 = r'\"month_sales\":\"\d{1,9}\"'
    
        prices = re.findall(pat1,html)
        titles = re.findall(pat2,html)
        sales = re.findall(pat3,html)

        for i in range(len(titles)):
            #eval去掉字符串两边双引号，以分好切片获取后面要的信息
            price = eval(prices[i].split(':')[1])
            title = eval(titles[i].split(':')[1])
            sale = eval(sales[i].split(':')[1])
            #将每个商品的价格，标题，付款人数以表格形式存入到一个空列表
            goods.append([title,sale,price])
    except:
        print('-----信息获取失败-----')

    return goods


def printinfo(slist):
    '''打印获取到的商品信息'''
    #format打印格式
    law = '{:^4}\t{:^8}\t{:^8}\t{:^16}'
    print(law.format('序号','商品价格','已付款人数','商品名称'))
    num = 0 #初始化序号
    for x in slist:
        num+=1
        print(law.format(num,x[2],x[1],x[0]))


def main():
    '''程序运行入口'''
    pages = int(input('请输入要查询的页数：'))
    good_name = input('请输入需要查找的商品类型：')
    for page in range(pages):
        try:
            html = geturl(page,good_name)
            slist = gethtml(html)
            printinfo(slist)
        except:
            print('-----程序运行出错-----')


if __name__ == '__main__':
    main()

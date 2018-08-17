import requests
from urllib.parse import quote,urlencode
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import string
import time

def get_theme(keyword):
    '''获取主题栏目下信息'''
    try:
        referer = quote(keyword, safe = string.printable)
        url = 'https://wows-api.wallstreetcn.com/v3/search/plus/plate'
        h_d = {
            'Host': 'wows-api.wallstreetcn.com',
            'Connection':'keep-alive',
            'Accept':'application/json, text/plain, */*',
            'Origin':'https://xuangubao.cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer':'https://xuangubao.cn/search/{}?tab=0'.format(referer),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
        data = {
            'q': keyword,
            'page': '1',
            'limit': '1000'
        }
        datas = urlencode(data)
        r = requests.get(url,params=datas,headers=h_d,verify=False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        infos = r.json()
        print('找到“{}”相关结果{}条'.format(keyword,infos.get('data').get('total')))
        return infos.get('data')

    except BaseException as e:
        print('获取主题栏目下资讯出错，请检测网络，或手动检测该接口是否更变',e)

def get_stock(keyword):
    '''获取股票栏目下信息'''
    try:
        url = 'https://wows-api.wallstreetcn.com/v3/search/plus/stock'
        referer = quote(keyword, safe=string.printable)
        h_d = {
            'Host': 'wows-api.wallstreetcn.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://xuangubao.cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://xuangubao.cn/search/{}?tab=0'.format(referer),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
        data = {
            'q': keyword,
            'page': '1',
            'limit': '10',
            'fields': 'prod_name, px_change, last_px, px_change_rate, related_plates, stock_labels'
        }
        datas = urlencode(data)
        r = requests.get(url, params=datas, headers=h_d, verify=False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        infos = r.json()
        print('找到“{}”相关结果{}条'.format(keyword, infos.get('data').get('total')))
        return infos
    except BaseException as e:
        print('获取股票栏目下资讯出错，请检测网络，或手动检测该接口是否更变', e)
def get_article(keyword):
    '''获取文章栏目下信息'''
    try:
        url = 'https://api.xuangubao.cn/api/pc/search/msgs'
        referer = quote(keyword, safe=string.printable)
        h_d = {
            'Host': 'api.xuangubao.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://xuangubao.cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://xuangubao.cn/search/{}?tab=0'.format(referer),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
        data = {
            'keyword': keyword,
            'limit': '50',
            'offset': '100',
            'subjsexclude': 'true'
        }
        datas = urlencode(data)
        s = requests.Session()
        s.options('https://xuangubao.cn/search/%E9%A3%9E%E6%9C%BA?tab=0', headers=h_d, verify=False)
        r = s.get(url, params=datas, headers=h_d, verify=False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        infos = r.json()
        print('找到“{}”相关结果{}条'.format(keyword, infos.get('Total')))
        return infos
    except BaseException as e:
        print('获取文章栏目下资讯出错，请检测网络，或手动检测该接口是否更变', e)

def get_flash(keyword,from_date,end_date):
    try:
        from_date = '{} 00:00:00'.format(from_date)
        end_date = '{} 00:00:00'.format(end_date)
        start = time.strptime(from_date, "%Y-%m-%d %H:%M:%S")
        start_time = int(time.mktime(start))
        end = time.strptime(end_date, "%Y-%m-%d %H:%M:%S")
        end_time = int(time.mktime(end))
        url = 'https://api.xuangubao.cn/api/pc/search/msgs'
        referer = quote(keyword, safe=string.printable)
        h_d = {
            'Host': 'api.xuangubao.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://xuangubao.cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://xuangubao.cn/search/{}?tab=0'.format(referer),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
        data = {
            'keyword': keyword,
            'limit': '50',
            'offset': '100',
            'fromdate': str(start_time),
            'enddate':str(end_time),
            'subjectids':'9,10,723,35,469,821'
        }
        datas = urlencode(data)
        s = requests.Session()
        s.options('https://xuangubao.cn/search/%E9%A3%9E%E6%9C%BA?tab=0', headers=h_d, verify=False)
        r = s.get(url, params=datas, headers=h_d, verify=False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        infos = r.json()
        print('找到“{}”相关结果{}条'.format(keyword, infos.get('Total')))
        return infos
    except BaseException as e:
        print('获取快讯栏目下资讯出错，请检测网络，或手动检测该接口是否更变', e)

def main(num):
        if num == 1:
            key_word = input('请输入你要查询主题的关键字并回车：')
            for info in get_theme(key_word).get('hits'):
                print(info.get('description'))
                # for b in info.get('description'):
                #     print(b)
                for a in info.get('stocks'):
                    # if a.get('description').get('description'):
                    #     print(a.get('description').get('description'))
                    # else:
                    print(a.get('description'))
                    # pass
        elif num == 2:
            key_word = input('请输入你要查询股票的关键字并回车：')
            print(get_stock(key_word))
        elif num == 3:
            key_word = input('请输入你要查询文章的关键字并回车：')
            print(get_article(key_word))
        elif num == 4:
            key_word = input('请输入你要查询快讯的关键字并回车：')
            start_date = input('请输入查询开始时间(格式为:2018-01-01)：')
            end_date = input('请输入查询结束时间(格式为:2018-12-30)：')
            print(get_flash(key_word,start_date,end_date))

if __name__ == "__main__":
    first = True
    try:
        while True:
            num = int(input('请输入数字进入相应的查询功能:1-主题，2-股票，3-文章，4-快讯：'))
            if num == 1 or num == 2 or num == 3 or num == 4:
                main(num)
                break
            else:
                print('你输入的输入有误，请重新输入:')
                continue
    except:
        print('你输入的内容为非数字，请重新运行程序~')
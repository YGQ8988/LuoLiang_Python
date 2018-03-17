import requests
import re


def gethtml(url):
    '''获取页面HTML文本'''
    try:
        h = {
            'Referer':'https://jingwei.supfree.net/kongzi.asp?id=3300',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
             }
        r = requests.get(url,headers=h)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except BaseException as f:
        print('页面请求失败了，错误信息为：{}'.format(f))

def getid(r,patten):
    '''从页面HTML文本内匹配ID'''
    try:
        p = re.compile(patten,re.S)
        provincesid = re.findall(p,r)
        return provincesid
    except BaseException as f:
        print('匹配ID失败了，错误信息为：{}'.format(f))

def getdicts(ids,iddicts):
    '''通过城市名获取城市ID'''
    for province in iddicts:
        ids[province[1]] = province[0]
    return ids

def geturl(cid,name,base_prefix):
    '''构造URL'''
    url = '{}{}'.format(base_prefix,cid[name])
    return url

def main():
    '''主程序'''
    base_url = 'https://jingwei.supfree.net/'
    base_r = gethtml(base_url)
    province_p = """<a href="kongzi.asp\?id=(.*?)">(.*?)</a>"""
    province_prefix = 'https://jingwei.supfree.net/kongzi.asp?id='
    provines = getid(base_r,province_p)
    p_dicts = {}
    province_ids = getdicts(p_dicts,provines)
    for a,b in zip(province_ids.keys(),range(1,len(province_ids)+1)):
        print(b,a)
    binngo = False
    while binngo == False:
        cityname = input('\n请从以上省市中完整输入您所在的城市(如需退出请输入：q）：')
        if cityname in province_ids.keys():
            city_url = geturl(province_ids,cityname,province_prefix)

            city_r = gethtml(city_url)
            county_p = """<a href="mengzi.asp\?id=(.*?)" title=".*?">(.*?)</a>"""
            county_prefix = 'https://jingwei.supfree.net/mengzi.asp?id='
            countyids = getid(city_r,county_p)
            c_dicts = {}
            city_ids = getdicts(c_dicts,countyids)
            for a,b in zip(city_ids.keys(),range(1,len(city_ids)+1)):
                print(b,a)
            countyname = input('\n请从以上市县中完整输入您所在的市或县：')
            if countyname in city_ids.keys():
                county_url = geturl(city_ids,countyname,county_prefix)

                county_r = gethtml(county_url)
                patten = """<p>经度：<span class="bred botitle18">(.*?) </span><br>纬度：<span class="bred botitle18">(.*?)</span></p>"""
                lola = re.findall(patten,county_r)
                return lola
            elif countyname == 'q':
                break
            else:
                print('\n您输入的县市有误，请重新输入:')
                continue
        elif cityname == 'q':
            break
        else:
            print('\n您输入的省市有误，请重新输入:')
            continue

if __name__ == "__main__":
    main()


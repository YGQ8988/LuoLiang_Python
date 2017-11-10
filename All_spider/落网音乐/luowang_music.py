import requests
from bs4 import BeautifulSoup
import bs4
import os
def getHtmlText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return '连接异常'

def getMusic_list(html,musiclist):

    soup = BeautifulSoup(html,'html.parser')
    alist = soup.find('div',attrs={'class':'pagenav-wrapper'}).children
    for a in alist:
        if isinstance(a, bs4.element.Tag):
            musicdict = {}
            a_href = a['href']
            a_text = a.text
            musicdict[a_href] = a_text
            musiclist.append(musicdict)

def  music_style(num,musiclist):
    msg = ''
    if num.isdigit():
        num = int(num)
        if num<len(musiclist):
            page = input("你想听得页数")
            a_href = list(musiclist[num].keys())[0]+'?p=%s'%page
            msg = getHtmlText(a_href)
            return msg
        else:
            msg = '超过最大目录'
            return msg
    else:
        msg = '请输入正确的数字'
        return msg

def style_info(style_html,albumlist):
    soup = BeautifulSoup(style_html,'html.parser')
    for div_vollist in soup.select('.vol-list'):
        a = div_vollist("a",attrs={'class':'cover-wrapper'})
        if a ==[]:
            return "超过最大页数"

    for a_title in a:
        music_album = {}
        music_album[a_title['title']] = a_title['href']
        albumlist.append(music_album)

def music_loads(num, albumlist,artistlist):
    msg = ''
    if num.isdigit():
        num = int(num)
        if num < len(musiclist):
            url = list(albumlist[num].values())[0]
            html = getHtmlText(url)
            soup = BeautifulSoup(html, 'html.parser')

            vol_num=soup.select('.vol-number')[0].text+"|"+soup.select('.vol-title')[0].text
            for class_player in soup.select(".player-wrapper"):
                name = class_player.select('.name')[0].text
                artist = class_player.select('.artist')[0].text
                artistlist[name]=artist
                print(name+"||"+artist)
            return  vol_num
        else:
            msg = '超过最大目录'
            return msg

def loding(artistlist,vol_num):
    url_num,url_root=vol_num.split('|')
    url="http://mp3-cdn2.luoo.net/low/luoo/radio{}/"
    root = "D:\\taobao_haibao\\" + url_root + '\\'
    patha=[]
    for k_name, v_artist in artistlist.items():
        paths=root+str(k_name)+str(".mp3")
        patha.append(paths)
    if not os.path.isdir(root):
        os.mkdir(root)
    for i,p in enumerate(patha):
        url1=" "
        if not os.path.exists(p):
            if i<9:
                a=str(i+1)+".mp3"
                url1=url.format(str(url_num))+"0"+a
                print(url1)
                r = requests.get(url1)
                with open(p,"wb") as f:
                    f.write(r.content)
            else :
                a = str(i + 1) + ".mp3"
                url1 = url.format(str(url_num))+a
                print(url1)
                r = requests.get(url1)
                with open(p, "wb") as f:
                    f.write(r.content)

if __name__ == '__main__':
    artistlist={}
    info = "{0:^10}\t{1:{2}^5}"
    musiclist=[]
    albumlist=[]
    url="http://www.luoo.net/music/"
    html = getHtmlText(url)
    getMusic_list(html, musiclist)
    for index,i in enumerate(musiclist):
        print(info.format(index,list(i.values())[0],chr(12288)))
    num = input("请输入你想听得类型序号")
    style_html = music_style(num, musiclist)
    if style_html == '请输入正确的数字' or style_html == '超过最大目录':
        print(style_html)
    else:
        style_html = style_html
        style_info(style_html,albumlist)
        for index, i in enumerate(albumlist):
            print(info.format(index,list(i.keys())[0],chr(12288)))

        num = input("请输入你想听得类型序号")
        vol_num=music_loads(num, albumlist,artistlist)
        loding(artistlist, vol_num)

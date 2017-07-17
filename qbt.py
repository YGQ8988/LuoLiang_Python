import requests,re,hashlib,os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def taobao_url(page_o,page_t):
    taobao_lists = []
    for page in range(page_o,page_t):
        tb_urls = "http://www.58pic.com/piccate/3-0-0-"+str(page)+".html"
        taobao_lists.append(tb_urls)
    return taobao_lists

def taobao_urls(taobao_lists):
    hb_lists = []
    for tb_url in taobao_lists:
        html = requests.get(tb_url,headers=headers)
        html.encoding = html.apparent_encoding
        hb_urls = re.findall("http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/.*?\.jpg",html.text)
        for hb_url in hb_urls:
            url_o = hb_url.split('.')
            url_l = url_o[0] + '.' +  url_o[1] + '.' + url_o[2] + '_1024' + '.' + url_o[3]
            hb_lists.append(url_l)
    return hb_lists

def path():
    path_save = 'D://taobao_haibao//'
    if not os.path.isdir(path_save):
        os.mkdir(path_save)
    else:
        pass
    return path_save

def save_hb(hb_lists,path_save):
    num = 0
    for tbhb_url in hb_lists:
        num += 1
        save_pic = requests.get(tbhb_url).content
        filename = hashlib.md5(save_pic).hexdigest()
        with open(path_save + str(filename) + '.jpg', 'wb')as f:
            f.write(save_pic)
            print('----------正在保存第%d图片' % num + tbhb_url + '----------')
            f.close()
    print('----------成功保存%d张图片----------' % num)

def main():
    page_1 = int(input('请输入开始爬取的页数：'))
    page_2 = int(input('请输入结束爬取的页数：'))
    taobao = taobao_url(page_1, page_2)
    tb_urls = taobao_urls(taobao)
    sava_path = path()
    save_hb(tb_urls, sava_path)

if __name__ == "__main__":

    main()
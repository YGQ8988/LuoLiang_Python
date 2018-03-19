import requests
import json
from time import sleep

def getlalo():

    result = False
    while result == False:
        address = input('\n请输入您所在的城市(注：地址中请包含城市名称）：')
        url = 'http://apis.map.qq.com/ws/geocoder/v1/?address={}&key=DSUBZ-WYJCX-Z4A46-ZIDMM-X5WSZ-2SFQ7'.format(
            address)
        r = requests.get(url=url)
        d = json.loads(r.text)
        if d.get('message') == 'query ok':
            return d.get('result').get('location')
        elif address == 'q':
            print('\n您已选择退出，感谢您的使用，再见！(五秒后自动关闭)')
            sleep(5)
            break
        elif d.get('message') == '查询无结果':
            print('\n您输入的地址有误，请重新输入：')
            continue

if __name__ == "__main__":
    getlalo()
    ll = getlalo()
    print(ll.get('lng'))
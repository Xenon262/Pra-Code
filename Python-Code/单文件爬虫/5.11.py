# 2022.5.11     python登录请求
import requests
url = 'https://www.douban.com/'

headervalue = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
               'Cookie':'ll="108289"; bid=5aSJEMI0XiE; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; ct=y; dbcl2="255311020:g1t7Gu0OAgE"; ck=02Xo'}

r = requests.get(url,headers=headervalue)

print(r.text)
import requests
from bs4 import BeautifulSoup
url = 'https://accounts.douban.com/j/login/basic'

datavalue = {
    'remember':'true',
    'name':'17694806832',
    'password':'w668811561'
}

headervalue = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
Cookie = 'll="108289"; bid=5aSJEMI0XiE; push_noty_num=0; push_doumail_num=0; ct=y; dbcl2="255311020:F/1Iw9cWTr4"; ck=--Js; gr_user_id=76400a34-6ea7-4708-866b-cbad0a6b3808; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=80b59499-e9e5-45b8-b232-ca882857f313; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_80b59499-e9e5-45b8-b232-ca882857f313=false; gr_cs1_80b59499-e9e5-45b8-b232-ca882857f313=user_id:1; ap_v=0,6.0'

cookie = {}
for i in Cookie.split(';'):
    key,value = i.split('=',1)
    cookie[key]=value

s = requests.session()
s.headers = headervalue
s.cookies.update(cookie)

r = s.post (url,data=datavalue)
r1 = s.get('https://book.douban.com/')
soup = BeautifulSoup(r1.text,'lxml')
name = soup.select('.bn-more')[0].text

print(r1.status_code)
print(name)
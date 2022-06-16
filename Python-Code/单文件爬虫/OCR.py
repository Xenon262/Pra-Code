from io import BytesIO
import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
import re

url= 'http://www.daimg.com/member/login.php'
s = requests.session()
r = s.get(url)

soup = BeautifulSoup(r.text,'lxml')
pic = soup.select('#vdimgck')[0]['src']
pic_url = 'http://www.daimg.com/' + pic[3:]
r = s.get(pic_url)
image = Image.open(BytesIO(r.content))
image.show()

image = image.convert('L')
image.show()

th = 127
table = []
for j in range(256):
    if j < 127:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
image.show()

code = pytesseract.image_to_string(image)
print(code)
result = ''.join(re.findall(r'\w',code))
print(result)


url = 'http://www.daimg.com/member/index_do.php'
datavalue = {
    'fmdo': 'login',
    'dopost': 'login',
    'gourl': '',
    'userid': 'aou668811',
    'pwd': 'w668811561',
    'vdcode': result
}
r = s.post(url,data=datavalue)
r = s.get('http://www.daimg.com/member/index.php')
soup = BeautifulSoup(r.text,'lxml')
jifen = soup.select('.mb_jf')[0].text
print(jifen)
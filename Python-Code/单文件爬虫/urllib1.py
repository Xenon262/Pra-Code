from urllib import response
import urllib.request

url = 'https://fanyi.youdao.com/'
response = urllib.request.urlopen(url)

print('响应状态：',type(response))
print('响应状态码：',response.getcode())

print('编码方式：',response.getheader('Content-Type'))
print('请求的URL：',response.geturl())
resp = response.read().decode('utf-8')
print('网页内容：\n',resp)
#Hanlder处理器和自定义 opener
#urllib.request.Request 可以定制请求头部
#高级功能，使用代理，使用cookie
import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3650.0 Safari/537.36'
}
#创建handler
handler = urllib.request.HTTPHandler()
#通过handler创建opener
#opener是一个对象，发送请求时，直接使用opener里边的方法。
opener = urllib.request.build_opener(handler)
request= urllib.request.Request(url = url, headers = headers)
response = opener.open(request)

print(response.read().decode())